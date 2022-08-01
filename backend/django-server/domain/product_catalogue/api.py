from typing import List
from uuid import UUID, uuid4

from ninja_extra import api_controller, http_get, http_post, http_delete
from ninja_jwt.authentication import JWTAuth
from django.http import HttpResponse

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


@api_controller("/sales_taxes", tags=["Sales Taxes"], auth=JWTAuth())
class SalesTaxController:
    @http_get("/", response=List[SalesTaxReadDto])
    def handle_get_sales_taxes(request):
        return get_sales_taxes()

    @http_get("/{sales_tax_id}", response=SalesTaxReadDto)
    def handle_get_sales_tax_detail(request, sales_tax_id: UUID):
        return get_sales_tax(sales_tax_id)

    @http_post("/")
    def handle_create_sales_tax(request, payload: SalesTaxWriteDto):
        id = uuid4()
        create_sales_tax_command.send(
            sender=None, id=id, name=payload.name, rate=payload.rate
        )
        return {"id": id}

    @http_delete("/{sales_tax_id}")
    def handle_delete_sales_tax(request, sales_tax_id: UUID):
        delete_sales_tax_command.send(sender=None, id=sales_tax_id)
        return HttpResponse(status=204)


@api_controller("/categories", tags=["Categories"], auth=JWTAuth())
class CategoryController:
    @http_get("/", response=List[CategoryReadDto])
    def handle_get_categories(request):
        return get_categories()

    @http_get("/{category_id}", response=CategoryReadDto)
    def handle_get_category_detail(request, category_id: UUID):
        return get_category(category_id)

    @http_post("/")
    def handle_create_category(request, payload: CategoryWriteDto):
        id = uuid4()
        create_category_command.send(sender=None, id=id, name=payload.name)
        return {"id": id}

    @http_delete("/{category_id}")
    def handle_delete_category(request, category_id: UUID):
        delete_category_command.send(sender=None, id=category_id)
        return HttpResponse(status=204)


@api_controller("/menu_items", tags=["Menu Items"], auth=JWTAuth())
class MenuItemController:
    @http_get("/", response=List[MenuItemReadDto])
    def handle_get_menu_items(request):
        return get_menu_items()

    @http_get("/{menu_item_id}", response=MenuItemReadDto)
    def handle_get_menu_item_detail(request, menu_item_id: UUID):
        return get_menu_item(menu_item_id)

    @http_post("/")
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

    @http_delete("/{menu_item_id}")
    def handle_delete_menu_item(request, menu_item_id: UUID):
        delete_menu_item_command.send(sender=None, id=menu_item_id)
        return HttpResponse(status=204)
