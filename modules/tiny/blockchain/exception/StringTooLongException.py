class StringTooLongException(Exception):
    def __init__(self, message):
        self.message = message
    def __init__(self):
        self.message = "String exceeds allowed limit of 255 chars"