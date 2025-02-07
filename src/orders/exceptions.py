from src.exceptions import CustomException
from fastapi import status


class OrderNotFound(CustomException):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = "Order not found."


class OrderItemNotFound(CustomException):
    status_code = status.HTTP_404_NOT_FOUND
    default_message = "Order Item not found."
