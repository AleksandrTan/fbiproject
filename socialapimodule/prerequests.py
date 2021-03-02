"""
Class for make pre requests
"""
import json
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError

from settings import instadata
from logsource.logconfig import logger
from supportingmodule.signgenerate import HMACGenerate


class PreRequestWorker:

    def __init__(self, params: object, headers: object, headers_dict: dict, request: object, requests_map):

        self.params = params
        self.headers = headers
        self.headers_dict = headers_dict
        self.request = request
        self.requests_map = requests_map

    def run_pre_requests(self) -> bool:
        """
        Emulation mobile app behaivor before login
        Run pre requests
        :return: bool
        """
        status = self._read_msisdn_header(self.params, self.headers, self.headers_dict)
        self._msisdn_header_bootstrap(self.params, self.headers_dict)
        self._token_result(self.params, self.headers_dict)
        self._contact_point_prefill(self.params, self.headers_dict)
        self._pre_login_sync(self.params, self.headers_dict)
        self._sync_login_experiments(self.params, self.headers_dict)
        self._log_attribution(self.params, self.headers_dict)
        self._get_prefill_candidates(self.params, self.headers_dict)

        return status

    def _make_request_post(self, main_url: str, uri: str, params: dict, headers: dict) -> dict:
        """
        :param headers:
        :param main_url: str
        :param uri: str
        :param params: dict
        :return: dict
        """
        data = {"status": False}

        try:
            response = self.request.post(main_url + uri, data=params, headers=headers)
            try:
                data = response.json()
                print(main_url + uri, response.status_code, data, response.headers)
            except JSONDecodeError as error:
                logger.warning(f"Error decode json - {error}, {response}")
                return {"status": False, "error": True, "error_type": error, "error_message": data}
        except ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code in [403, 404, 429, 408]:
            if data["message"] == 'bad request':
                logger.warning(f"Error server status - code {response.status_code}, {data}")

                return {"status": False, "error_type": response.status_code, "error_message": data}

        if response.status_code == 400:
            logger.warning(f"Error server status - code {response.status_code}, {data}")

            return {"status": False, "error_type": response.status_code, "error_message": data}

        if response.status_code == 200:
            if data["status"] == 'ok':
                return {"status": True, "data": data, "headers": response.headers}

        return {"status": False, "error": True, "error_type": response.status_code, "error_message": data}

    def _read_msisdn_header(self, params: object, headers_data: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["read_msisdn_header"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        data = {"mobile_subno_usage": "default",
                "device_id": params.uuid}

        result = self._make_request_post(url, uri, data, headers)

        if params.csrftoken == '':
            params.csrftoken = self.get_cookie_param("csrftoken")
            params.mid = self.get_cookie_param("mid")
            params.ig_did = self.get_cookie_param("ig_did")
            params.ds_user_id = self.get_cookie_param("ds_user_id")
            headers_data.set_attribute_headers("X-MID", params.mid)

        if result["status"] and params.csrftoken:
            return True

        return False

    def _msisdn_header_bootstrap(self, params: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["msisdn_header_bootstrap"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        data = {"mobile_subno_usage": "default",
                "device_id": params.uuid}

        result = self._make_request_post(url, uri, data, headers)

        if result["status"]:
            return True

        return False

    def _token_result(self, params: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["token"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        data = {
            "token_hash": "",
            "device_id": params.device_id,
            "custom_device_id": params.uuid,
            "fetch_reason": 'token_expired'
        }

        result = self._make_request_post(url, uri, data, headers)

        if result["status"]:
            return True

        return False

    def _contact_point_prefill(self, params: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["contact_point_prefill"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        data = {"mobile_subno_usage": "default",
                "device_id": params.uuid}

        result = self._make_request_post(url, uri, data, headers)

        if result["status"]:
            return True

        return False

    def _pre_login_sync(self, params: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["launcher_sync"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        data = {
            "id": params.uuid,
            "configs": instadata.PRE_LOGIN_STRING
        }

        result = self._make_request_post(url, uri, data, headers)

        if result["status"]:
            return True

        return False

    def _sync_login_experiments(self, params: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["qe_sync"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        try:
            data = {
                "_csrftoken": params.csrftoken,
                "id": self.request.cookies["ds_user_id"],
                "_uid": self.request.cookies["ds_user_id"],
                "_uuid": params.uuid,
                "experiments": instadata.LOGIN_EXPERIMENTS
            }
        except KeyError as error:
            logger.warning(f"Error  - {error}")
            data = {
                "id": params.uuid,
                "experiments": instadata.LOGIN_EXPERIMENTS
            }

        result = self._make_request_post(url, uri, data, headers)

        if result["status"]:
            # set initialization_parameters for login action(generate enc_password)
            # if type(result["headers"]["x-ig-set-www-claim"]) == str:
            #     params.igWWWClaim = result["headers"]["x-ig-set-www-claim"]
            #
            # if type(result["headers"]["ig-set-authorization"]) == str:
            #     params.authorization = result["headers"]["ig-set-authorization"]

            if type(result["headers"]["ig-set-password-encryption-key-id"]) == str:
                params.passwordEncryptionKeyId = int(result["headers"]["ig-set-password-encryption-key-id"])

            if type(result["headers"]["ig-set-password-encryption-pub-key"]) == str:
                params.passwordEncryptionPubKey = result["headers"]["ig-set-password-encryption-pub-key"]

            return True

        return False

    def _log_attribution(self, params: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["log_attribution"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        data = {
            "adid": params.adid
        }

        result = self._make_request_post(url, uri, data, headers)

        if result["status"]:
            return True

        return False

    def _get_prefill_candidates(self, params: object, headers_dict: dict):
        url = self.requests_map["main_url"]
        uri = self.requests_map["get_prefill_candidates"]["uri"]

        headers = {'X-DEVICE-ID': headers_dict["X-IG-Device-ID"],
                   "User-Agent": headers_dict["User-Agent"]}

        data = {
            "android_device_id": params.device_id,
            "usages": '["account_recovery_omnibox"]',
            "device_id": params.uuid
        }

        result = self._make_request_post(url, uri, data, headers)

        if result["status"]:
            return True

        return False

    def get_cookie_param(self, key):
        return self.request.cookies.get_dict().get(key, '')
