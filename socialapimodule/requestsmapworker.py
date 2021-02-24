"""
Class for working with the request file requestsmap.py
"""
from settings import requestsmap


class RequestMapWorker:

    def __init__(self):
        self.requestsmap = requestsmap

    def get_url_for_task(self, key: str):
        pass
