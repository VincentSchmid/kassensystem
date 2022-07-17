# Generated by Django 4.0.5 on 2022-07-17 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('pos', '0002_remove_order_menu_items_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.waiter'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='pos.order'),
        ),
    ]
