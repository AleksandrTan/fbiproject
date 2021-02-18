"""
A class for making requests to the social network Instagram used web API
"""
import requests
import json

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
            response = requests.post(main_url + uri, data=params)
        except requests.exceptions.ConnectionError as error:
            print(error)
            return {"status": False}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return {"status": data["status"]}

        return {"status": False}

    def login(self, params: dict) -> dict:
        """
        :param params:
        :param login: str
        :param password: str
        :return: dict
        """
        response = self.make_request(self.requests_map["main_url"], self.requests_map["login"]["uri"], params)
        print(response, 3500)
        return dict()

    def flipping_tape(self, url, params):
        pass