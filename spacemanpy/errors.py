class SpacemanBaseException(Exception):

    pass


class NotFound(SpacemanBaseException):
    def __init__(self, _id):
        message = f"Object with id <{_id}> was not found."
        super().__init__(message)


class InvalidHTTPMethod(SpacemanBaseException):
    def __init__(self):
        message = "GET is the only supported method."
        super().__init__(message)
