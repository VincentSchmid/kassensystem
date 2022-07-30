from django.dispatch import Signal, receiver
from .models import Table


create_table_command = Signal()
delete_table_command = Signal()

@receiver(create_table_command)
def handle_create_table(**kwargs):
    table = Table.objects.create(id=kwargs['id'], number=kwargs['number'])

@receiver(delete_table_command)
def handle_delete_table(**kwargs):
    table = Table.objects.get(id=kwargs['id'])
    table.delete()
