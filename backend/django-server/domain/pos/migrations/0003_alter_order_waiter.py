# Generated by Django 4.0.5 on 2022-07-10 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import domain.pos.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pos', '0002_order_waiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, validators=[domain.pos.models.validate_is_waiter]),
        ),
    ]