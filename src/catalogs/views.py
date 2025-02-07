from fastapi import APIRouter, status, Response
from src.catalogs.schemas import CategoryUpdateSchema, ListCategorySchema, ListProductsSchema, ProductCreateSchema, ProductPartialUpdateSchema, ProductUpdateSchema
from src.dependencies import DBSession
from src.catalogs import controllers
from .models import Category, Product

router = APIRouter(prefix="/catalog", tags=["catalog"])


@router.post("/categories", response_model=Category)
async def create_category(data: Category, session: DBSession) -> Category:
    category = await controllers.create_category(data=data, session=session)
    return category


@router.get("/categories/{id}", response_model=Category)
async def get_category(id: int, session: DBSession) -> Category:
    category = await controllers.get_category(id=id, session=session)
    return category


@router.get("/categories", response_model=ListCategorySchema)
async def get_categories(session: DBSession) -> ListCategorySchema:
    categories = await controllers.get_categories(session=session)
    return ListCategorySchema(count=len(categories), items=categories)


@router.put("/categories/{id}", response_model=Category)
async def partial_update_category(id: int, data: CategoryUpdateSchema, session: DBSession) -> Category:
    category = await controllers.update_category(id=id, data=data, session=session)
    return category


@router.patch("/categories/{id}", response_model=Category)
async def partial_update_category(id: int, data: CategoryUpdateSchema, session: DBSession) -> Category:
    category = await controllers.update_category(id=id, data=data, session=session)
    return category


@router.delete("/categories/{id}")
async def remove_category(id: int, session: DBSession) -> Response:
    await controllers.remove_category(id=id, session=session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post("/products/", response_model=Product)
async def create_product(data: ProductCreateSchema, session: DBSession) -> Product:
    product = await controllers.create_product(data=data, session=session)
    return product


@router.get("/products/{id}", response_model=Product)
async def get_product(id: int, session: DBSession) -> Product:
    product = await controllers.get_product(id=id, session=session)
    return product


@router.get("/products/", response_model=ListProductsSchema)
async def get_products(session: DBSession) -> ListProductsSchema:
    products = await controllers.get_products(session=session)
    return ListProductsSchema(count=len(products), items=products)


@router.patch("/products/{id}", response_model=Product)
async def partial_update_product(id: int, data: ProductPartialUpdateSchema, session: DBSession) -> Product:
    product = await controllers.update_product(id=id, data=data, session=session)
    return product


@router.put("/products/{id}", response_model=Product)
async def update_product(id: int, data: ProductUpdateSchema, session: DBSession) -> Product:
    product = await controllers.update_product(id=id, data=data, session=session)
    return product


@router.delete("/products/{id}", response_model=Product)
async def remove_product(id: int, session: DBSession):
    await controllers.remove_product(id=id, session=session)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
