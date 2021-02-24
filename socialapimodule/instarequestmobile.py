"""
A class for making requests to the social network Instagram used mobile API
"""
import requests
import json
from logsource.logconfig import logger
from settings import requestsmap


class InstagramRequestsMobile:

    def __init__(self, host_proxy: str, port_proxy: int):
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
            response = requests.post(main_url + uri, data=params, headers=headers)
        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"]:
                return {"status": data["status"]}
        logger.warning(f"Error response code - {response.status_code}")
        return {"status": False, "error": True, "error_type": response.status_code}

    def make_request_authorization(self, main_url: str, uri: str, params: dict) -> dict:
        """
        :param main_url: str
        :param uri: str
        :param params: dict
        :return: dict
        """
        try:
            headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/88.0.4324.150 Safari/537.36'
                       }
            response = requests.post(main_url + uri, params=params, headers=headers)
        except requests.exceptions.ConnectionError as error:
            logger.warning(f"Authorization instagram error - {error}")
            return {"status": False, "error": True, "error_type": error}
        except KeyError as error:
            logger.warning(f"Authorization instagram error - {error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 200:
            authorization_data = dict()
            data = json.loads(response.text)
            print(data)
            headers = response.headers

            if headers['csrftoken']:
                authorization_data['id_did'] = headers['id_did']
                authorization_data['csrftoken'] = headers['csrftoken']
                authorization_data['mid'] = headers['mid']
                authorization_data['ig_nrcb'] = headers['ig_nrcb']
                return {"status": True, "error": False, 'authorization_data': authorization_data}
        logger.warning(f"Authorization instagram error - {response.text}")
        logger.warning(f"Error response code - {response.status_code}")
        return {"status": False, "error": True, "error_type": response.status_code}

    def authorization(self, params: dict) -> dict:
        """
        :param params: dict
        :return: dict
        """
        response = self.make_request_authorization(self.requests_map["main_url"],
                                                   self.requests_map["authorization"]["uri"], params)

        return response

    def login(self, account_data: dict, initialization_parameters: dict, initialization_headers: dict) -> dict:
        """
        :param initialization_headers: dict
        :param account_data: dict
        :param initialization_parameters: dict
        :return: dict
        """
        authorization_data = self.authorization(initialization_parameters)
        print('Auth data', authorization_data)
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