# Generated by Django 4.0.5 on 2022-06-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_catalogue', '0002_remove_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ManyToManyField(to='product_catalogue.category'),
        ),
    ]