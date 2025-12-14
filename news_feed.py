class NewsFeed:
    def __init__(self):
        # Ініціалізація черги новин
        self._queue = []

    def add_news(self, title: str, content: str) -> bool:
        # Додає новину в кінець черги (ТЕСТ)
        # Валідація: заголовок і зміст не можуть бути порожніми
        if not title or not content:
            raise ValueError("Заголовок або зміст не можуть бути порожніми")
        
        news_item = {"title": title, "content": content}
        self._queue.append(news_item)
        return True

    def publish_news(self) -> dict:
        # Повертає та видаляє першу новину (FIFO)
        # Якщо черга порожня — викидає IndexError
        if len(self._queue) == 0:
            raise IndexError("Стрічка новин порожня, немає чого публікувати")
        
        return self._queue.pop(0)

    def count_news(self) -> int:
        # Повертає кількість новин у черзі
        return len(self._queue)

    def clear_feed(self):
        # Очищає всю стрічку новин
        self._queue.clear()
