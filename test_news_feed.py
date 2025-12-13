import unittest
from news_feed import NewsFeed

class TestNewsFeed(unittest.TestCase):

    def setUp(self):
        # Підготовка: створюємо стрічку та додаємо дві новини
        self.feed = NewsFeed()
        self.feed.add_news("Test News 1", "Content 1")
        self.feed.add_news("Test News 2", "Content 2")

    def tearDown(self):
        # Прибирання після тестів
        self.feed = None

    # ТЕСТ 1 — Перевіряємо успішне додавання новини
    def test_add_news_success(self):
        result = self.feed.add_news("New Title", "New Content")
        self.assertTrue(result)
        self.assertEqual(self.feed.count_news(), 3)

    # ТЕСТ 2 — Перевірка роботи черги FIFO
    def test_publish_fifo_order(self):
        item = self.feed.publish_news()
        self.assertEqual(item["title"], "Test News 1")
        self.assertEqual(self.feed.count_news(), 1)

    # ТЕСТ 3 — Перевірка, чи піднімається ValueError при пустих даних
    def test_add_empty_data_exception(self):
        with self.assertRaises(ValueError):
            self.feed.add_news("", "xxx")

    # ТЕСТ 4 — Перевірка виключення при публікації з порожньої черги
    def test_publish_from_empty_queue(self):
        self.feed.clear_feed()
        with self.assertRaises(IndexError):
            self.feed.publish_news()

    # ТЕСТ 5 — Негативний сценарій з expectedFailure
    @unittest.expectedFailure
    def test_publish_news_wrong_behavior(self):
        item = self.feed.publish_news()
        self.assertIsNone(item)

if __name__ == "__main__":
    unittest.main()
