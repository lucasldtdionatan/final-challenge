from fastapi import status
from src.exceptions import CustomException


class UserNotFound(CustomException):
    default_message = "User not found."
    status_code = status.HTTP_404_NOT_FOUND


class AddressNotFound(CustomException):
    default_message = "Address not found."
    status_code = status.HTTP_404_NOT_FOUND