from fastapi import HTTPException


class CustomException(HTTPException):
    default_message = "An error occured."

    def __init__(self, detail: str = None):
        if not detail:
            detail = self.default_message

        super().__init__(status_code=self.status_code, detail=detail)