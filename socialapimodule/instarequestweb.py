"""
A class for making requests to the social network Instagram used web API
"""
from interfaces.apisocialinter import BaseSocialRequests


class InstagramRequestsWeb(BaseSocialRequests):

    def __init__(self, host_proxy, port_proxy):
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy

    def make_request(self):
        pass

    def login(self, login, password, url, params):
        pass

    def flipping_tape(self, url, params):
        pass