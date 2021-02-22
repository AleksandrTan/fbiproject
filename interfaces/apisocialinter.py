"""
Social requests classes interface
"""
from abc import ABCMeta, abstractmethod


class BaseSocialRequests(metaclass=ABCMeta):

    @abstractmethod
    def make_request_authorization(self, main_url: str, uri: str, params: dict):
        pass

    @abstractmethod
    def make_request(self, main_url: str, uri: str, params: dict):
        pass

    @abstractmethod
    def autorization(self, params: dict):
        pass

    @abstractmethod
    def login(self, params: dict):
        pass

    @abstractmethod
    def like(self, params: dict):
        pass

    @abstractmethod
    def flipping_tape(self, params: dict):
        pass

    @abstractmethod
    def subscribe(self, params: dict):
        pass
