"""
A class for making requests to the social network Instagram used mobile API
"""
from interfaces.apisocialinter import BaseSocialRequests
import requestsmap


class InstagramRequestsMobile(BaseSocialRequests):

    def __init__(self, host_proxy, port_proxy):
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.requests_map = requestsmap.INSTAGRAM_MOBILE_DATA

    def make_request(self, main_url, uri, params):
        pass

    def login(self, login, password):
        pass

    def flipping_tape(self, url, params):
        pass
