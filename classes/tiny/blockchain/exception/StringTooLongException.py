class StringTooLongException(BaseException):
    def __init__(self):
        self.limit = 255
        self.message = "String exceeds allowed limit of " + str(self.limit) + " chars"