"""
Parameter generation (enc_password) class for login action
"""
import base64
import datetime
import secrets

from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
import rsa


class EncGenerate:
    def __init__(self, public_key: str, public_key_id: int, password: str):
        self.public_key = public_key
        self.public_key_id = public_key_id
        self.password = password

    def enc_password(self) -> str:
        randKey = get_random_bytes(32)
        iv = get_random_bytes(12)
        # iv = bytearray(12)
        time = str(int(datetime.datetime.now().timestamp()))

        decoded_public = base64.b64decode(self.public_key.encode())
        recipient_key = RSA.import_key(decoded_public)
        cipher_rsa = PKCS1_v1_5.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(randKey)

        cipher_aes = AES.new(randKey, AES.MODE_GCM, iv)
        cipher_aes.update(time.encode())

        ciphertext, tag = cipher_aes.encrypt_and_digest(self.password.encode("utf8"))
        payload = base64.b64encode((b"\x01\x00" + self.public_key_id.to_bytes(2, byteorder='big') + iv + len(
            enc_session_key).to_bytes(2, byteorder='big') + enc_session_key + tag + ciphertext))

        return f"#PWD_INSTAGRAM:4:{time}:{payload.decode()}"

        # return f"#PWD_INSTAGRAM:0:{time}:{self.password}"

    def encrypt_password(self):
        IG_LOGIN_ANDROID_PUBLIC_KEY = self.public_key
        IG_LOGIN_ANDROID_PUBLIC_KEY_ID = self.public_key_id

        key = secrets.token_bytes(32)
        iv = secrets.token_bytes(12)
        time = str(int(datetime.datetime.now().timestamp()))

        base64_decoded_device_public_key = base64.b64decode(
            IG_LOGIN_ANDROID_PUBLIC_KEY.encode()
        )

        public_key = RSA.importKey(base64_decoded_device_public_key)

        encrypted_aes_key = rsa.encrypt(key, public_key)

        cipher = AES.new(key, AES.MODE_GCM, iv)
        cipher.update(time.encode())
        encrypted_password, tag = cipher.encrypt_and_digest(self.password.encode())

        payload = (
                b"\x01"
                + str(IG_LOGIN_ANDROID_PUBLIC_KEY_ID).encode()
                + iv
                + b"0001"
                + encrypted_aes_key
                + tag
                + encrypted_password
        )

        base64_encoded_payload = base64.b64encode(payload)

        return f"#PWD_INSTAGRAM:4:{time}:{base64_encoded_payload.decode()}"

