from typing import List
from uuid import UUID, uuid4

from ninja_jwt.authentication import JWTAuth
from django.http import HttpResponse
from ninja import Router

from .dtos import (
    SalesTaxReadDto,
    SalesTaxWriteDto,
    CategoryReadDto,
    CategoryWriteDto,
    MenuItemReadDto,
    MenuItemWriteDto,
)
from .commands import (
    create_sales_tax_command,
    delete_sales_tax_command,
    create_category_command,
    delete_category_command,
    create_menu_item_command,
    delete_menu_item_command,
)
from .queries import (
    get_sales_tax,
    get_sales_taxes,
    get_category,
    get_categories,
    get_menu_item,
    get_menu_items,
)


router = Router()

sales_tax_router = Router()
router.add_router("/sales_taxes", sales_tax_router, tags=["Sales Taxes"])

category_router = Router()
router.add_router("/categories", category_router, tags=["Categories"])

menu_item_router = Router()
router.add_router("/menu_items", menu_item_router, tags=["Menu Items"])


@sales_tax_router.get("/", response=List[SalesTaxReadDto], auth=JWTAuth())
def handle_get_sales_taxes(request):
    return get_sales_taxes()


@sales_tax_router.get("/{sales_tax_id}", response=SalesTaxReadDto, auth=JWTAuth())
def handle_get_sales_tax_detail(request, sales_tax_id: UUID):
    return get_sales_tax(sales_tax_id)


@sales_tax_router.post("/", auth=JWTAuth())
def handle_create_sales_tax(request, payload: SalesTaxWriteDto):
    id = uuid4()
    create_sales_tax_command.send(
        sender=None, id=id, name=payload.name, rate=payload.rate
    )
    return {"id": id}


@sales_tax_router.delete("/{sales_tax_id}", auth=JWTAuth())
def handle_delete_sales_tax(request, sales_tax_id: UUID):
    delete_sales_tax_command.send(sender=None, id=sales_tax_id)
    return HttpResponse(status=204)


@category_router.get("/", response=List[CategoryReadDto], auth=JWTAuth())
def handle_get_categories(request):
    return get_categories()


@category_router.get("/{category_id}", response=CategoryReadDto, auth=JWTAuth())
def handle_get_category_detail(request, category_id: UUID):
    return get_category(category_id)


@category_router.post("/", auth=JWTAuth())
def handle_create_category(request, payload: CategoryWriteDto):
    id = uuid4()
    create_category_command.send(sender=None, id=id, name=payload.name)
    return {"id": id}


@category_router.delete("/{category_id}", auth=JWTAuth())
def handle_delete_category(request, category_id: UUID):
    delete_category_command.send(sender=None, id=category_id)
    return HttpResponse(status=204)


@menu_item_router.get("/", response=List[MenuItemReadDto], auth=JWTAuth())
def handle_get_menu_items(request):
    return get_menu_items()


@menu_item_router.get("/{menu_item_id}", response=MenuItemReadDto, auth=JWTAuth())
def handle_get_menu_item_detail(request, menu_item_id: UUID):
    return get_menu_item(menu_item_id)


@menu_item_router.post("/", auth=JWTAuth())
def handle_create_menu_item(request, payload: MenuItemWriteDto):
    id = uuid4()
    create_menu_item_command.send(
        sender=None,
        id=id,
        name=payload.name,
        price=payload.price,
        category_id=payload.category_id,
    )
    return {"id": id}


@menu_item_router.delete("/{menu_item_id}", auth=JWTAuth())
def handle_delete_menu_item(request, menu_item_id: UUID):
    delete_menu_item_command.send(sender=None, id=menu_item_id)
    return HttpResponse(status=204)
