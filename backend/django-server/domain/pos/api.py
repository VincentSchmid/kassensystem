from typing import List
from uuid import UUID, uuid4

from django.http import HttpResponse
from ninja import Router

from .dtos import TableWriteDto, TableReadDto
from .commands import create_table_command, delete_table_command
from .queries import get_table, get_tables


router = Router()

@router.get("/tables", response=List[TableReadDto])
def handle_get_tables(request):
    return get_tables()

@router.get('/tables/{table_id}', response=TableReadDto)
def get_table_detail(request, table_id: UUID):
    return get_table(table_id)

@router.post('/tables')
def create_table(request, payload: TableWriteDto):
    id = uuid4()
    create_table_command.send(sender=None, id=id, number=payload.number)
    return {'id': id}

@router.delete('/tables/{table_id}')
def delete_table(request, table_id: UUID):
    delete_table_command.send(sender=None, id=table_id)
    return HttpResponse(status=204)
