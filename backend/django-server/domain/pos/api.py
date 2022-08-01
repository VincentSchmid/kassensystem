from math import perm
from typing import List
from uuid import UUID, uuid4

from django.http import HttpResponse
from ninja_extra import api_controller, http_get, http_post, http_delete
from ninja_jwt.authentication import JWTAuth
from authentication.permissions import ModelPermission

from .dtos import (
    TableWriteDto,
    TableReadDto,
    PaymentMethodReadDto,
    PaymentMethodWriteDto,
    OrderReadDto,
    OrderWriteDto,
    PaymentReadDto,
    PaymentWriteDto,
)
from .commands import (
    create_table_command,
    delete_table_command,
    create_payment_method_command,
    delete_payment_method_command,
    create_order_command,
    delete_order_command,
)
from .queries import (
    get_table,
    get_tables,
    get_payment_method,
    get_payment_methods,
    get_payment,
    get_order,
    get_orders,
)


@api_controller(
    "/pos/tables", tags=["Tables"], auth=JWTAuth(), permissions=[ModelPermission]
)
class TableController:
    app_label = "pos"
    model_name = "table"

    @http_get("/", response=List[TableReadDto])
    def handle_get_tables(self, request):
        return get_tables()

    @http_get("/{table_id}", response=TableReadDto)
    def handle_get_table_detail(self, request, table_id: UUID):
        return get_table(table_id)

    @http_post("/")
    def handle_create_table(self, request, payload: TableWriteDto):
        id = uuid4()
        create_table_command.send(sender=None, id=id, number=payload.number)
        return {"id": id}

    @http_delete("/{table_id}")
    def handle_delete_table(self, request, table_id: UUID):
        delete_table_command.send(sender=None, id=table_id)
        return HttpResponse(status=204)


@api_controller(
    "/pos/payment_methods",
    tags=["Payment Methods"],
    auth=JWTAuth(),
    permissions=[ModelPermission],
)
class PaymentMethodController:
    app_label = "pos"
    model_name = "payment_method"

    @http_get("/", response=List[PaymentMethodReadDto])
    def handle_get_payment_methods(self, request):
        return get_payment_methods()

    @http_get("/{payment_method_id}", response=PaymentMethodReadDto)
    def handle_get_payment_method_detail(self, request, payment_method_id: UUID):
        return get_payment_method(payment_method_id)

    @http_post("/")
    def handle_create_payment_method(self, request, payload: PaymentMethodWriteDto):
        id = uuid4()
        create_payment_method_command.send(sender=None, id=id, name=payload.name)
        return {"id": id}

    @http_delete("/{payment_method_id}")
    def handle_delete_payment_method(self, request, payment_method_id: UUID):
        delete_payment_method_command.send(sender=None, id=payment_method_id)
        return HttpResponse(status=204)


@api_controller(
    "/pos/orders", tags=["Orders"], auth=JWTAuth(), permissions=[ModelPermission]
)
class OrderController:
    app_label = "pos"
    model_name = "order"

    @http_get("/", response=List[OrderReadDto])
    def handle_get_orders(self, request):
        return get_orders()

    @http_get("/{order_id}", response=OrderReadDto)
    def handle_get_order_detail(self, request, order_id: UUID):
        return get_order(order_id)

    @http_get("/{order_id}/payment", response=PaymentReadDto)
    def handle_get_order_payment(self, request, order_id: UUID):
        return get_payment(order_id)

    @http_post("/{order_id}/payment")
    def handle_create_payment(self, request, order_id: UUID, payload: PaymentWriteDto):
        id = uuid4()
        create_order_command.send(
            sender=None,
            order_id=order_id,
            id=id,
            amount=payload.amount,
            payment_method_id=payload.payment_method.id,
        )
        return {"id": id}

    @http_post("/")
    def handle_create_order(self, request, payload: OrderWriteDto):
        id = uuid4()
        create_order_command.send(
            sender=None,
            id=id,
            order_items=payload.order_items,
            table=payload.table,
            status=payload.status,
            waiter=payload.waiter,
            payment=payload.payment,
        )
        return {"id": id}

    @http_delete("/{order_id}")
    def handle_delete_order(self, request, order_id: UUID):
        delete_order_command.send(sender=None, id=order_id)
        return HttpResponse(status=204)
