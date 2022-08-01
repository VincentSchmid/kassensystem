from storages.backends.azure_storage import AzureStorage
import environ

env = environ.Env()


class AzureMediaStorage(AzureStorage):
    account_name = env(
        "AZURE_ACCOUNT_NAME"
    )  # Must be replaced by your <storage_account_name>
    account_key = env(
        "AZURE_ACCOUNT_KEY"
    )  # Must be replaced by your <storage_account_key>
    azure_container = "media"
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = env(
        "AZURE_ACCOUNT_NAME"
    )  # Must be replaced by your storage_account_name
    account_key = env(
        "AZURE_ACCOUNT_KEY"
    )  # Must be replaced by your <storage_account_key>
    azure_container = "static"
    expiration_secs = None
