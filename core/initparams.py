import hashlib
import random
import uuid

from settings import instadata


class InitParams:
    def __init__(self):
        self.uuids = dict()
        self.device_settings = dict()
        self.initialization_parameters = dict()
        self.device_settings = instadata.DEVICE_SETTINGS

    def get_params(self) -> dict:
        self.initialization_parameters["uuids"] = self.set_uuids()
        self.initialization_parameters["device_settings"] = self.device_settings

        return self.initialization_parameters

    def set_uuids(self):
        self.uuids["phone_id"] = self.generate_uuid()
        self.uuids["uuid"] = self.generate_uuid()
        self.uuids["client_session_id"] = self.generate_uuid()
        self.uuids["advertising_id"] = self.generate_uuid()
        self.uuids["device_id"] = self.generate_device_id()
        return self.uuids

    def generate_uuid(self) -> str:
        return str(uuid.uuid4())

    def generate_device_id(self) -> str:
        return "android-%s" % hashlib.md5(
            bytes(random.randint(1, 1000))
        ).hexdigest()[:16]
