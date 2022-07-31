from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

from domain.pos.api import router as pos_router
from domain.product_catalogue.api import router as product_catalogue_router
from domain.employee.api import router as employee_router


api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

api.add_router("/pos/", pos_router)
api.add_router("/product_catalogue/", product_catalogue_router)
api.add_router("/employees/", employee_router, tags=["Employees"])
