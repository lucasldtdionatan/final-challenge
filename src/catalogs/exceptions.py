from fastapi import status
from src.exceptions import CustomException


class CategoryNotFound(CustomException):
    default_message = "Category not found."
    status_code = status.HTTP_404_NOT_FOUND


class ProductNotFound(CustomException):
    default_message = "Product not found."
    status_code = status.HTTP_404_NOT_FOUND
