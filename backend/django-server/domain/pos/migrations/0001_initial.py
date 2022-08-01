# Generated by Django 4.0.5 on 2022-07-31 15:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("employee", "0001_initial"),
        ("product_catalogue", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("status", models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PaymentMethod",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Table",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("number", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("amount", models.FloatField()),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="pos.order"
                    ),
                ),
                (
                    "payment_method",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="pos.paymentmethod",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "menu_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product_catalogue.menuitem",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="pos.order",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="table",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="pos.table"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="waiter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="employee.waiter"
            ),
        ),
    ]
