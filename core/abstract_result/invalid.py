class InvalidRequestData(Exception):
    status_code = -1

    def __init__(self, status_code, message):
        super(InvalidRequestData, self).__init__()
        self.status_code = status_code
        self.message = message
