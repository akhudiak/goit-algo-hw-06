class PhoneFormatError(Exception):
    def __init__(self, message="The phone number must be 10 digits long"):
        self.message = message
        super().__init__(self.message)