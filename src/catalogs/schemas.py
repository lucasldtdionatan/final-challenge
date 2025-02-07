from decimal import Decimal
from uuid import UUID
from sqlmodel import SQLModel
from .models import Category, Product


class CategoryUpdateSchema(SQLModel):
    name: str


class ListCategorySchema(SQLModel):
    count: int
    items: list[Category]


class ProductBaseSchema(SQLModel):
    name: str
    price: Decimal
    stock: int
    is_active: bool | None = False    
    category_id: int


class ProductCreateSchema(ProductBaseSchema):
    seller_id: UUID


class ProductPartialUpdateSchema(ProductBaseSchema):
    name: str | None = None
    price: Decimal | None = None
    stock: int | None = None
    is_active: bool | None = False    
    category_id: int | None = None


class ProductUpdateSchema(ProductBaseSchema):
    pass


class ListProductsSchema(SQLModel):
    count: int
    items: list[Product]
