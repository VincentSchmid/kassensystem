from typing import List
from uuid import UUID, uuid4

from django.http import HttpResponse
from ninja import Router

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


router = Router()

table_router = Router()
router.add_router("/tables", table_router, tags=["Tables"])

payment_method_router = Router()
router.add_router("/payment_methods", payment_method_router, tags=["Payment Methods"])

order_router = Router()
router.add_router("/orders", order_router, tags=["Orders"])


@table_router.get("/", response=List[TableReadDto])
def handle_get_tables(request):
    return get_tables()


@table_router.get("/{table_id}", response=TableReadDto)
def handle_get_table_detail(request, table_id: UUID):
    return get_table(table_id)


@table_router.post("/")
def handle_create_table(request, payload: TableWriteDto):
    id = uuid4()
    create_table_command.send(sender=None, id=id, number=payload.number)
    return {"id": id}


@table_router.delete("/{table_id}")
def handle_delete_table(request, table_id: UUID):
    delete_table_command.send(sender=None, id=table_id)
    return HttpResponse(status=204)


@payment_method_router.get("/", response=List[PaymentMethodReadDto])
def handle_get_payment_methods(request):
    return get_payment_methods()


@payment_method_router.get("/{payment_method_id}", response=PaymentMethodReadDto)
def handle_get_payment_method_detail(request, payment_method_id: UUID):
    return get_payment_method(payment_method_id)


@payment_method_router.post("/")
def handle_create_payment_method(request, payload: PaymentMethodWriteDto):
    id = uuid4()
    create_payment_method_command.send(sender=None, id=id, name=payload.name)
    return {"id": id}


@payment_method_router.delete("/{payment_method_id}")
def handle_delete_payment_method(request, payment_method_id: UUID):
    delete_payment_method_command.send(sender=None, id=payment_method_id)
    return HttpResponse(status=204)


@order_router.get("/{oder_id}/payment", response=PaymentReadDto)
def handle_get_payment_detail(request, oder_id: UUID):
    return get_payment(oder_id)


@order_router.post("/{order_id}/payment")
def handle_create_payment(request, order_id: UUID, payload: PaymentWriteDto):
    id = uuid4()
    create_order_command.send(
        sender=None,
        order_id=order_id,
        id=id,
        amount=payload.amount,
        payment_method_id=payload.payment_method.id,
    )
    return {"id": id}


@order_router.get("/", response=List[OrderReadDto])
def handle_get_orders(request):
    return get_orders()


@order_router.get("/{order_id}", response=OrderReadDto)
def handle_get_order_detail(request, order_id: UUID):
    return get_order(order_id)


@order_router.post("/")
def handle_create_order(request, payload: OrderWriteDto):
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


@order_router.delete("/{order_id}")
def handle_delete_order(request, order_id: UUID):
    delete_order_command.send(sender=None, id=order_id)
    return HttpResponse(status=204)
