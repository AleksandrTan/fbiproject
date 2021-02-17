"""
The class describes a bot object that simulates user behavior on the Instagram social network.
It is launched from the worker process, initialized, and then, using api,
receives tasks that it performs, accompanying its work with logging at the database level,
a file on the standard output stream.
"""


class InstaBot:

    def __init__(self, host_proxy, port_proxy, instagram_api, source_api):
        """
        Bot object initialization
        :param host_proxy: str
        :param port_proxy: int
        :param instagram_api: object
        :param source_api: object
        """
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.instagram_api = instagram_api
        self.source_api = source_api

