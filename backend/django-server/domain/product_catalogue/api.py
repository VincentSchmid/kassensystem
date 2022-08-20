from typing import List
from uuid import UUID, uuid4

from ninja_extra import api_controller, http_get, http_post, http_delete
from ninja_jwt.authentication import JWTAuth
from django.http import HttpResponse

from authentication.permissions import ModelPermission

from .read.dtos import (
    SalesTaxReadDto,
    CategoryReadDto,
    MenuItemReadDto,
)
from .write.dtos import (
    SalesTaxWriteDto,
    CategoryWriteDto,
    MenuItemWriteDto,
)
from .write.commands import (
    create_sales_tax_command,
    delete_sales_tax_command,
    create_category_command,
    delete_category_command,
    create_menu_item_command,
    delete_menu_item_command,
)

from .read.queries import (
    get_sales_tax,
    get_sales_taxes,
    get_category,
    get_categories,
    get_menu_item,
    get_menu_items,
)


@api_controller(
    "/sales_taxes", tags=["Sales Taxes"], auth=JWTAuth(), permissions=[ModelPermission]
)
class SalesTaxController:
    app_label = "read"
    model_name = "salestax"

    @http_get("/", response=List[SalesTaxReadDto])
    def handle_get_sales_taxes(self, request):
        return get_sales_taxes()

    @http_get("/{sales_tax_id}", response=SalesTaxReadDto)
    def handle_get_sales_tax_detail(self, request, sales_tax_id: UUID):
        return get_sales_tax(sales_tax_id)

    @http_post("/")
    def handle_create_sales_tax(self, request, payload: SalesTaxWriteDto):
        id = uuid4()
        create_sales_tax_command.send(
            sender=None, id=id, name=payload.name, rate=payload.rate
        )
        return {"id": id}

    @http_delete("/{sales_tax_id}")
    def handle_delete_sales_tax(self, request, sales_tax_id: UUID):
        delete_sales_tax_command.send(sender=None, id=sales_tax_id)
        return HttpResponse(status=204)


@api_controller(
    "/categories", tags=["Categories"], auth=JWTAuth(), permissions=[ModelPermission]
)
class CategoryController:
    app_label = "read"
    model_name = "category"

    @http_get("/", response=List[CategoryReadDto])
    def handle_get_categories(self, request):
        return get_categories()

    @http_get("/{category_id}", response=CategoryReadDto)
    def handle_get_category_detail(self, request, category_id: UUID):
        return get_category(category_id)

    @http_post("/")
    def handle_create_category(self, request, payload: CategoryWriteDto):
        id = uuid4()
        create_category_command.send(sender=None, id=id, name=payload.name)
        return {"id": id}

    @http_delete("/{category_id}")
    def handle_delete_category(self, request, category_id: UUID):
        delete_category_command.send(sender=None, id=category_id)
        return HttpResponse(status=204)


@api_controller(
    "/menu_items", tags=["Menu Items"], auth=JWTAuth(), permissions=[ModelPermission]
)
class MenuItemController:
    app_label = "read"
    model_name = "menuitem"

    @http_get("/", response=List[MenuItemReadDto])
    def handle_get_menu_items(self, request):
        return get_menu_items()

    @http_get("/{menu_item_id}", response=MenuItemReadDto)
    def handle_get_menu_item_detail(self, request, menu_item_id: UUID):
        return get_menu_item(menu_item_id)

    @http_post("/")
    def handle_create_menu_item(self, request, payload: MenuItemWriteDto):
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
    def handle_delete_menu_item(self, request, menu_item_id: UUID):
        delete_menu_item_command.send(sender=None, id=menu_item_id)
        return HttpResponse(status=204)
