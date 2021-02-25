import time
import uuid
import random

from settings import instadata
from settings.devices import DEVICES


class InitHeaders:

    def __init__(self, params: object):
        self.initialization_headers = dict()
        self.params = params
        self.default_headers = instadata.DEFAULT_HEADERS
        self.make_headers()

    def get_headers(self) -> dict:
        print(type(self.initialization_headers["X-IG-Device-ID"]))
        return self.initialization_headers

    def make_headers(self):
        self.initialization_headers["User-Agent"] = self.init_user_agent()
        self.initialization_headers["X-MID"] = self.params.mid
        self.initialization_headers["X-IG-Device-ID"] = self.params.uuid
        self.initialization_headers["X-IG-Android-ID"] = self.params.device_id
        self.initialization_headers["Host"] = self.default_headers['Host']
        self.initialization_headers["X-IG-App-Locale"] = self.default_headers['X-IG-App-Locale']
        self.initialization_headers["X-IG-Device-Locale"] = self.default_headers['X-IG-Device-Locale']
        self.initialization_headers["X-IG-Mapped-Locale"] = self.default_headers['X-IG-Mapped-Locale']
        self.initialization_headers["X-Pigeon-Session-Id"] = self.generate_uuid()
        self.initialization_headers["X-Pigeon-Rawclienttime"] = str(round(time.time() * 1000) / 1000)
        self.initialization_headers["X-IG-Connection-Speed"] = str(random.randint(1000, 3700)) + "-1kbps"
        self.initialization_headers["X-CM-Bandwidth-KBPS"] = "-1.000"
        self.initialization_headers["X-IG-Bandwidth-Speed-KBPS"] = str(random.randint(2900000, 10000000) / 1000)
        self.initialization_headers["X-IG-Bandwidth-TotalBytes-B"] = '0'
        self.initialization_headers["X-IG-Bandwidth-TotalTime-MS"] = '0'
        self.initialization_headers["X-Bloks-Version-Id"] = instadata.BLOKS_VERSION_ID
        self.initialization_headers["X-CM-Latency"] = "-1.000"
        self.initialization_headers["Accept-Encoding"] = self.default_headers["Accept-Encoding"]
        self.initialization_headers["Accept-Language"] = self.default_headers["Accept-Language"]
        self.initialization_headers["X-FB-HTTP-Engine"] = self.default_headers["X-FB-HTTP-Engine"]
        self.initialization_headers["X-Bloks-Is-Layout-RTL"] = self.default_headers["X-Bloks-Is-Layout-RTL"]
        self.initialization_headers["X-IG-Connection-Type"] = self.default_headers["X-IG-Connection-Type"]
        self.initialization_headers["X-IG-Capabilities"] = self.default_headers["X-IG-Capabilities"]
        self.initialization_headers['X-IG-App-ID'] = instadata.FACEBOOK_ANALYTICS_APPLICATION_ID

    def init_user_agent(self):
        return f"Instagram {instadata.APP_VERSION} Android {self.generate_build_device()}; {instadata.LANGUAGE };" \
               f" {instadata.APP_VERSION_CODE} "

    def generate_build_device(self):
        count = len(DEVICES)
        index = random.randint(0, count)

        return DEVICES[index]

    def generate_uuid(self) -> str:
        return str(uuid.uuid4())
