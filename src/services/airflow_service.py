import boto3
import requests


class AirflowService:
    """
        This class is just example you can modify and use it in your package-cli commands.
    """
    @staticmethod
    def fetch_dags(web_server_host_name, web_token):
        # Your service logic here ...
        return {"dags": [web_server_host_name, web_token]}

    @staticmethod
    def authenticate_user():
        # Your service logic here ...

        return "abc def ghi jkl", "https://abcd.com"
