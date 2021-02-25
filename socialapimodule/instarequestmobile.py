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

    def make_request_post(self, main_url: str, uri: str, params: dict, headers: dict) -> dict:
        """
        :param headers:
        :param main_url: str
        :param uri: str
        :param params: dict
        :return: dict
        """
        try:
            response = self.request.post(main_url + uri, data=params, headers=headers)
        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return {"status": data["status"], "data": data}
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
            response = self.make_request_post(self.requests_map["main_url"], self.requests_map["login"]["uri"],
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
        response = self.make_request_post(self.requests_map["main_url"], self.requests_map["like"]["uri"], params,
                                          authorization_data)
        print(4000, authorization_data)
        return response

    def flipping_tape(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self.make_request_post(self.requests_map["main_url"], self.requests_map["flipping_type"]["uri"],
                                          params,
                                          authorization_data)
        print(4000, authorization_data)
        return response

    def subscribe(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self.make_request_post(self.requests_map["main_url"], self.requests_map["subscribe"]["uri"], params,
                                          authorization_data)
        print(4000, authorization_data)
        return response

    def run_pre_requests(self, params: object) -> bool:
        """
        Emulation mobile app behaivor before login
        Run pre requests
        :return: bool
        """
        self.read_msisdn_header(params)
        self.msisdn_header_bootstrap()
        self.token_result()
        self.contact_point_prefill()
        self.pre_login_sync()
        self.sync_login_experiments()
        self.log_attribution()
        self.get_prefill_candidates()

        return True

    def read_msisdn_header(self, params: object):
        url = self.requests_map["main_url"]
        uri = self.requests_map["read_msisdn_header"]["uri"]
        headers = {'X-DEVICE-ID': params.uuid}
        data = {"mobile_subno_usage": "default", "device_id": params.uuid}
        result = self.make_request_post(url, uri, data, headers)

        if not params.csrftoken:
            params.csrftoken = self.request.cookies.get_dict().get("csrftoken", '')
            params.mid = self.request.cookies.get_dict().get("mid", '')
            params.ig_did = self.request.cookies.get_dict().get("ig_did", '')

        if result["status"]:
            return True

        return False

    def msisdn_header_bootstrap(self):
        print(self.request.cookies)

        pass

    def token_result(self):
        pass

    def contact_point_prefill(self):
        pass

    def pre_login_sync(self):
        pass

    def sync_login_experiments(self):
        pass

    def log_attribution(self):
        pass

    def get_prefill_candidates(self):
        pass
