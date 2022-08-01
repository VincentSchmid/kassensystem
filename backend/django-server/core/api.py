from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

from domain.pos.api import (
    TableController,
    PaymentMethodController,
    OrderController,
)

from domain.product_catalogue.api import (
    SalesTaxController,
    CategoryController,
    MenuItemController,
)

from domain.employee.api import WaiterController


api = NinjaExtraAPI()
api.register_controllers(
    MenuItemController,
    CategoryController,
    SalesTaxController,
    TableController,
    PaymentMethodController,
    OrderController,
    WaiterController,
    NinjaJWTDefaultController,
)
