"""
A class for making requests to the social network Instagram used web API
"""
import requests
import json

from logsource.logconfig import logger
from interfaces.apisocialinter import BaseSocialRequests
import requestsmap


class InstagramRequestsWeb(BaseSocialRequests):

    def __init__(self, host_proxy, port_proxy):
        """
        :param host_proxy: str
        :param port_proxy: int
        """
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.requests_map = requestsmap.INSTAGRAM_WEB_DATA

    def make_request(self, main_url: str, uri: str, params: dict) -> dict:
        """
        :param main_url: str
        :param uri: str
        :param params: dict
        :return: dict
        """
        try:
            headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/88.0.4324.150 Safari/537.36',
                       }
            response = requests.post(main_url + uri, data=params, headers=headers)
        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return {"status": data["status"]}
        logger.warning(f"Error response code - {response.status_code}")
        return {"status": False, "error": True, "error_type": response.status_code}

    def login(self, params: dict) -> dict:
        """
        :param params: dict
        :return: dict
        """
        response = self.make_request(self.requests_map["main_url"], self.requests_map["login"]["uri"], params)

        return response

    def flipping_tape(self, url, params):
        pass
