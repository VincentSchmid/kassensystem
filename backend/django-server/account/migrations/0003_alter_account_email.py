# Generated by Django 4.0.5 on 2022-08-06 13:48

import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=django.contrib.postgres.fields.citext.CIEmailField(
                error_messages={"unique": "A user with that email already exists."},
                max_length=60,
                null=True,
                unique=True,
                verbose_name="email",
            ),
        ),
    ]
