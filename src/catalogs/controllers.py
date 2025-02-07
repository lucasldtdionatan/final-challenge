from sqlmodel import select, Session

from src.catalogs import exceptions
from src.users.models import User
from src.users import exceptions as user_exceptions

from .models import Category, Product


async def create_category(data: Category, session: Session) -> Category:
    session.add(data)
    session.commit()
    session.refresh(data)
    return data


async def get_category(id: int, session: Session) -> Category:
    category = session.get(Category, id)
    if not category:
        raise exceptions.CategoryNotFound()
    
    return category


async def get_categories(session: Session) -> list[Category]:
    categories = session.exec(select(Category)).all()
    return categories


async def remove_category(id: int, session: Session) -> None:
    category = session.get(Category, id)
    if not category:
        raise exceptions.CategoryNotFound()
    
    session.delete(category)
    session.commit()


async def update_category(id: int, data: Category, session: Session) -> Category:
    category = session.get(Category, id)
    if not category:
        raise exceptions.CategoryNotFound()
    
    category.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return category


async def create_product(data: Product, session: Session) -> Product:
    product = Product(**data.model_dump())

    if not session.get(User, product.seller_id):
        raise user_exceptions.UserNotFound()

    if product.category_id:
        category = session.get(Category, product.category_id)
        if not category:
            raise exceptions.CategoryNotFound()

    session.add(product)
    session.commit()
    session.refresh(product)
    
    return product


async def get_product(id: int, session: Session) -> Product:
    product = session.get(Product, id)
    if not product:
        raise exceptions.ProductNotFound()
    
    return product


async def get_products(session: Session) -> list[Product]:
    categories = session.exec(select(Product)).all()
    return categories


async def remove_product(id: int, session: Session) -> None:
    product = session.get(Product, id)
    if not product:
        raise exceptions.ProductNotFound()
    
    session.delete(product)
    session.commit()


async def update_product(id: int, data: Product, session: Session) -> Product:
    product = session.get(Product, id)
    if not product:
        raise exceptions.ProductNotFound()
    
    product.sqlmodel_update(data.model_dump(exclude_unset=True))
    session.add(product)
    session.commit()
    session.refresh(product)
    
    return product