"""
String generation class for post request using HMAC Engine
"""
import hashlib
import hmac
import urllib

from settings.instadata import SIG_KEY_VERSION


class HMACGenerate:
    def __init__(self, data):
        self.data = data

    def generate_signature(self):
        """
        Generate signature of POST data for Private API
        """
        body = hmac.new(SIG_KEY_VERSION.encode("utf-8"), self.data.encode("utf-8"), hashlib.sha256).hexdigest()

        return f"signed_body={body}.{urllib.parse.quote(self.data)}&ig_sig_key_version={SIG_KEY_VERSION}"
