import hashlib
import random
import uuid
import json

from settings import instadata
from settings.devices import DEVICES


class InitParams:
    def __init__(self):
        self.uuids = dict()
        self.device_settings = dict()
        self.initialization_parameters = dict()

    def get_params(self, account_data: dict) -> dict:
        self.initialization_parameters["uuids"] = self.set_uuids(account_data)
        self.initialization_parameters["device_settings"] = instadata.DEVICE_SETTINGS

        return self.initialization_parameters

    def set_uuids(self, account_data):
        self.uuids["username"] = account_data["username"]
        self.uuids["password"] = account_data["password"]
        self.uuids["phone_id"] = self.generate_uuid()
        self.uuids["enc_password"] = ''
        self.uuids["_csrftoken"] = ''
        self.uuids["mid"] = ''
        self.uuids["ig_did"] = ''
        self.uuids["adid"] = ''
        self.uuids["google_tokens"] = '[]'
        self.uuids["login_attempt_count"] = 0
        self.uuids["country_codes"] = json.dumps({"country_code": '1', "source": 'default'})
        self.uuids["jazoest"] = self.generate_jazoest(self.uuids["phone_id"])
        self.uuids["uuid"] = self.generate_uuid()
        self.uuids["client_session_id"] = self.generate_uuid()
        self.uuids["advertising_id"] = self.generate_uuid()
        self.uuids["device_id"] = self.generate_device_id()
        self.uuids["build_device"] = self.generate_build_device()

        return self.uuids

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
