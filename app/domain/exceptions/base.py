class ApplicationException(Exception):
    @property
    def message(self):
        return "An error occurred while the application was running"
