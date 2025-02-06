from app.domain.dtos.events import VisitorDTO


class NotificationProviderClient:
    """Кдиент для интеграции с Notification Service"""

    async def send_notification(self, visitor: VisitorDTO): ...
