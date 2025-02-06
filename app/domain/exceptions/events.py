from app.domain.exceptions.base import ApplicationException


class EventListRequestException(ApplicationException):
    def __init__(self, status_code: int, response_content: str):
        self.status_code = status_code
        self.response_content = response_content

    @property
    def message(self):
        return "Failed to get event list"


class EventRegisterRequestException(ApplicationException):
    def __init__(self, status_code: int, response_content: str):
        self.status_code = status_code
        self.response_content = response_content

    @property
    def message(self):
        return "Error when registering for the event"
