class HomeworkKeyException(Exception):
    """Проверка доступности ключей в запросе."""

    def __init__(self, key):
        """Инициализация класса."""
        self.key = key
        self.message = f'Ключ "{key}" в запросе недоступен'
        super().__init__(self.message)

    def __str__(self):
        """Сообщение об ошибке."""
        return f'{self.message}'


class TokenNoExistException(Exception):
    """Проверка доступности переменных окружения."""

    def __init__(self):
        """Инициализация класса."""
        self.message = 'Переменные окружения недоступны'
        super().__init__(self.message)

    def __str__(self):
        """Сообщение об ошибке."""
        return f'{self.message}'


class EndpointNotAccessException(Exception):
    """Проверка доступности ednpoint'a."""

    def __init__(self, endpoint):
        """Инициализация класса."""
        self.endpoint = endpoint
        self.message = f'endpoint {endpoint} недоступен'
        super().__init__(self.message)

    def __str__(self):
        """Сообщение об ошибке."""
        return f'{self.message}'


class StatusNotChangeException(Exception):
    """Проверка статуса endpoint'a."""

    def __init__(self, endpoint):
        """Инициализация класса."""
        self.endpoint = endpoint
        self.message = f'endpoint {endpoint} недоступен'
        super().__init__(self.message)

    def __str__(self):
        """Сообщение об ошибке."""
        return f'{self.message}'


class BotSendMeassageException(Exception):
    """Проверка доступности endpoint'a телеграмма."""

    def __init__(self):
        """Инициализация класса."""
        self.message = 'Ошибка при отправки сообщения'
        super().__init__(self.message)

    def __str__(self):
        """Сообщение об ошибке."""
        return f'{self.message}'