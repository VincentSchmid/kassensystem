from django.apps import AppConfig


class ProductCatalogueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "domain.product_catalogue.read"

    class Meta:
        verbose_name = "Product Catalogue"
        verbose_name_plural = "Product Catalogue"
