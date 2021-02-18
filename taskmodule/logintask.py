"""
Performs the task of implementing a login on a social network
"""
from socialapimodule.requestsmapworker import RequestMapWorker


class LoginTask:

    def __init__(self, social_api):
        self.social_api = social_api

    def run(self):
        print("Task start working!!!")
