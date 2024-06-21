import keyring


class ConfigManager:
    SERVICE_NAME = "aws_airflow_sdk"

    @classmethod
    def set_config_value(cls, key, value):
        keyring.set_password(cls.SERVICE_NAME, key, value)

    @classmethod
    def get_config_value(cls, key):
        return keyring.get_password(cls.SERVICE_NAME, key)
