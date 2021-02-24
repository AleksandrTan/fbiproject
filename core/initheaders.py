from settings import instadata


class InitHeaders:

    def __init__(self, params: dict):
        self.initialization_headers = dict()
        self.params = params
        self.default_headers = instadata.DEFAULT_HEADERS

    def get_headers(self) -> dict:
        return self.default_headers

    def make_headers(self):
        self.init_user_agent()

    def init_user_agent(self):
        pass
