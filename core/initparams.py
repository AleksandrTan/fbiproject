import hashlib
import random
import uuid
import json

from settings import instadata
from settings.devices import DEVICES


class InitParams:

    def __init__(self, account_data: dict, initialization_parameters: dict):
        # if initialization_parameters are passed to the bot constructor
        if initialization_parameters:
            self.csrftoken = initialization_parameters["csrftoken"]
            self.mid = initialization_parameters["mid"]
            self.ig_did = initialization_parameters["id_did"]
            self.ds_user_id = initialization_parameters["ds_user_id"]
        else:
            self.csrftoken = ''
            self.mid = ''
            self.ig_did = ''
            self.ds_user_id = ''
        self.account_data = account_data
        self.initialization_parameters = dict()
        self.device_settings = instadata.DEVICE_SETTINGS
        self.username = self.account_data["username"]
        self.password = self.account_data["password"]
        self.phone_id = self.generate_uuid()
        self.enc_password = ''
        self.adid = ''
        self.google_tokens = '[]'
        self.login_attempt_count = 0
        self.country_codes = json.dumps({"country_code": '1', "source": 'default'})
        self.jazoest = self.generate_jazoest(self.phone_id)
        self.uuid = self.generate_uuid()
        self.client_session_id = self.generate_uuid()
        self.advertising_id = self.generate_uuid()
        self.device_id = self.generate_device_id()
        self.build_device = self.generate_build_device()
        self.ds_user_id = ''
        self.igWWWClaim = ''
        self.authorization = ''
        self.passwordEncryptionKeyId = ''
        self.passwordEncryptionPubKey = ''

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def generate_uuid(self) -> str:
        return str(uuid.uuid4())

    def generate_device_id(self) -> str:
        return "android-%s" % hashlib.md5(
            bytes(random.randint(1, 1000))
        ).hexdigest()[:16]

    def generate_build_device(self):
        count = len(DEVICES)
        index = random.randint(0, count)

        return DEVICES[index]

    def generate_jazoest(self, phone_id):
        buffer = bytearray(phone_id, 'ascii')
        data = 0
        for elem in buffer:
            data += elem

        return '2' + str(data)

    def get_dict(self):
        return self.__dict__
