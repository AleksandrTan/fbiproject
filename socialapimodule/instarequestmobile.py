"""
A class for making requests to the social network Instagram used mobile API
"""
import requests
import json
from logsource.logconfig import logger
from settings import requestsmap


class InstagramRequestsMobile:

    def __init__(self, host_proxy: str, port_proxy: int):
        self.request = requests.Session()
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.requests_map = requestsmap.INSTAGRAM_MOBILE_DATA

    def make_request(self, main_url: str, uri: str, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param main_url: str
        :param uri: str
        :param params: dict
        :return: dict
        """
        try:
            headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/88.0.4324.150 Safari/537.36',
                       }
            response = self.request.post(main_url + uri, data=params, headers=headers)
        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return {"status": data["status"]}
        logger.warning(f"Error response code - {response.status_code}")
        return {"status": False, "error": True, "error_type": response.status_code}

    def login(self, account_data: dict, initialization_parameters: dict, initialization_headers: dict) -> dict:
        """
        :param initialization_headers: dict
        :param account_data: dict
        :param initialization_parameters: dict
        :return: dict
        """
        authorization_data = {"status": "ok", "ok": 3500, "authorization_data": dict()}

        if authorization_data['status']:
            user_data = dict()
            user_data['username'] = initialization_parameters['username']
            user_data['password'] = initialization_parameters['password']
            user_data['queryParams'] = {}
            user_data['optIntoOneTap'] = False
            response = self.make_request(self.requests_map["main_url"], self.requests_map["login"]["uri"],
                                         user_data, authorization_data['authorization_data'])

            if response["status"]:
                if response["response_data"]["status"] == 'ok' and response["response_data"]['authenticated'] == 'true':
                    return {"status": True, "response_data": response,
                            'authorization_data': authorization_data['authorization_data']}

        return {"status": False}

    def like(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self.make_request(self.requests_map["main_url"], self.requests_map["like"]["uri"], params,
                                     authorization_data)
        print(4000, authorization_data)
        return response

    def flipping_tape(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self.make_request(self.requests_map["main_url"], self.requests_map["flipping_type"]["uri"], params,
                                     authorization_data)
        print(4000, authorization_data)
        return response

    def subscribe(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self.make_request(self.requests_map["main_url"], self.requests_map["subscribe"]["uri"], params,
                                     authorization_data)
        print(4000, authorization_data)
        return response

    def run_pre_requests(self, params: object):
        """
        Emulation mobile app behaivor before login
        Run pre requests
        :return: bool
        """

        # /api/v1/accounts/get_prefill_candidates
        self.get_prefill_candidates(True)
        # /api/v1/qe/sync (server_config_retrieval)
        self.sync_device_features(True)
        # /api/v1/launcher/sync/ (server_config_retrieval)
        self.sync_launcher(True)
        # /api/v1/accounts/contact_point_prefill/
        self.set_contact_point_prefill("prefill")

        return True

    def get_prefill_candidates(self, login: bool = False) -> dict:
        # "android_device_id":"android-f14b9731e4869eb",
        # "phone_id":"b4bd7978-ca2b-4ea0-a728-deb4180bd6ca",
        # "usages":"[\"account_recovery_omnibox\"]",
        # "_csrftoken":"9LZXBXXOztxNmg3h1r4gNzX5ohoOeBkI",
        # "device_id":"70db6a72-2663-48da-96f5-123edff1d458"
        data = {
            "android_device_id": self.device_id,
            "phone_id": self.phone_id,
            "usages": '["account_recovery_omnibox"]',
            "device_id": self.device_id,
        }
        if login is False:
            data["_csrftoken"] = self.token
        return self.private_request(
            "accounts/get_prefill_candidates/", data, login=login
        )

    def sync_device_features(self, login: bool = False) -> dict:
        data = {
            "id": self.uuid,
            "server_config_retrieval": "1",
            "experiments": "config.LOGIN_EXPERIMENTS",
        }
        if login is False:
            data["_uuid"] = self.uuid
            data["_uid"] = self.user_id
            data["_csrftoken"] = self.token
        return self.private_request(
            "qe/sync/", data, login=login, headers={"X-DEVICE-ID": self.uuid}
        )

    def sync_launcher(self, login: bool = False) -> dict:
        data = {
            "id": self.uuid,
            "server_config_retrieval": "1",
        }
        if login is False:
            data["_uid"] = self.user_id
            data["_uuid"] = self.uuid
            data["_csrftoken"] = self.token
        return self.private_request("launcher/sync/", data, login=login)

    def set_contact_point_prefill(self, usage: str = "prefill") -> dict:
        data = {"phone_id": self.phone_id, "usage": usage}
        return self.private_request("accounts/contact_point_prefill/", data, login=True)