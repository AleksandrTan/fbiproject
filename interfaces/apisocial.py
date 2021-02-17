from abc import ABCMeta, abstractmethod


class BaseSocial(metaclass=ABCMeta):

    @abstractmethod
    def login(self, login, password):
        pass

    @abstractmethod
    def flipping_tape(self):
        pass
