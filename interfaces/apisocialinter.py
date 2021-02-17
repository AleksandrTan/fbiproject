from abc import ABCMeta, abstractmethod


class BaseSocialRequests(metaclass=ABCMeta):

    @abstractmethod
    def request(self):
        pass

    @abstractmethod
    def login(self, login, password, url, params):
        pass

    @abstractmethod
    def flipping_tape(self, url, params):
        pass
