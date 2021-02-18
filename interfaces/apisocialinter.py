"""
Social requests classes interface
"""
from abc import ABCMeta, abstractmethod


class BaseSocialRequests(metaclass=ABCMeta):

    @abstractmethod
    def make_request(self, main_url: str, uri: str, params: dict):
        pass

    @abstractmethod
    def login(self, params: dict):
        pass

    @abstractmethod
    def flipping_tape(self, url: str, params: dict):
        pass
