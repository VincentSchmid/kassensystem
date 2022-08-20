from typing import Type
from typing import cast

from django.apps import AppConfig, apps
from eventsourcing.system import System, Runner, SingleThreadedRunner

from .application import ProductCatalogue, ProductCatalogueProcess


def get_runner() -> Runner:
    app_config = cast(
        ProductCatalogueConfig,
        apps.get_app_config("write"),
    )
    return app_config.es_runner


def get_product_catalogue() -> ProductCatalogue:
    return get_runner().get(ProductCatalogue)


class ProductCatalogueConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "domain.product_catalogue.write"
    es_runner: Runner

    def ready(self) -> None:
        self.make_runner()

    def make_runner(self,
        runner_cls: Type[Runner] = SingleThreadedRunner) -> Runner:
        self.es_runner = runner_cls(
            System(pipes=[[ProductCatalogue, ProductCatalogueProcess]]))
        self.es_runner.start()
