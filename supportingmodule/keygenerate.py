"""
Parameter generation (enc_password) class for login action
"""
import base64
import datetime

from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA


class EncGenerate:
    def __init__(self, public_key: str, public_key_id: int, password: str):
        self.public_key = public_key
        self.public_key_id = public_key_id
        self.password = password

    def enc_password(self) -> str:
        session_key = get_random_bytes(32)
        iv = bytearray(12)
        time = str(int(datetime.datetime.now().timestamp()))
        decoded_publicey = base64.b64decode(self.public_key.encode())
        recipient_key = RSA.import_key(decoded_publicey)
        cipher_rsa = PKCS1_v1_5.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
        cipher_aes.update(time.encode())
        ciphertext, tag = cipher_aes.encrypt_and_digest(self.password.encode("utf8"))
        payload = base64.b64encode((b"\x01\x00" + self.public_key_id.to_bytes(2, byteorder='big') + iv + len(
            enc_session_key).to_bytes(2, byteorder='big') + enc_session_key + tag + ciphertext))

        return f"#PWD_INSTAGRAM:4:{time}:{payload.decode()}"
