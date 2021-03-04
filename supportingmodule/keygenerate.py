"""
Parameter generation (enc_password) class for login action
"""
import base64
import binascii
import datetime
import struct
from urllib.parse import quote_plus

from Cryptodome import Random
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from nacl.public import PublicKey, SealedBox


class EncGenerate:
    def __init__(self, public_key: str, public_key_id: int, password: str):
        self.public_key = public_key
        self.public_key_id = public_key_id
        self.password = password

    def enc_password(self) -> str:
        key = get_random_bytes(32)
        iv = get_random_bytes(12)
        # iv = bytearray(12)
        time = str(int(datetime.datetime.now().timestamp()))

        decoded_public = base64.b64decode(self.public_key.encode())
        recipient_key = RSA.import_key(decoded_public)
        cipher_rsa = PKCS1_v1_5.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(key)

        cipher_aes = AES.new(key, AES.MODE_GCM, iv)
        cipher_aes.update(time.encode())

        ciphertext, tag = cipher_aes.encrypt_and_digest(self.password.encode("utf8"))
        payload = base64.b64encode((b"\x01\x00" + self.public_key_id.to_bytes(2, byteorder='big') + iv + len(
            enc_session_key).to_bytes(2, byteorder='big') + enc_session_key + tag + ciphertext)).decode()

        return f"#PWD_INSTAGRAM:4:{time}:{payload}"

        # return f"#PWD_INSTAGRAM:0:{time}:{self.password}"

    def encrypt_password(self):
        key = Random.get_random_bytes(32)
        iv = Random.get_random_bytes(12)
        time = int(datetime.datetime.now().timestamp())

        pubkey = base64.b64decode(self.public_key)
        rsa_key = RSA.importKey(pubkey)
        rsa_cipher = PKCS1_v1_5.new(rsa_key)
        encrypted_key = rsa_cipher.encrypt(key)

        aes = AES.new(key, AES.MODE_GCM, nonce=iv)
        aes.update(str(time).encode())

        encrypted_password, tag = aes.encrypt_and_digest(bytes(self.password, 'utf-8'))

        encrypted = bytes([1,
                           self.public_key_id,
                           *list(iv),
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(tag),
                           *list(encrypted_password)])
        encrypted = base64.b64encode(encrypted).decode()

        return f'#PWD_INSTAGRAM:4:{time}:{encrypted}'

    def encrypt_password_v2(self, key_id, pub_key, password, version=10):
        key = Random.get_random_bytes(32)
        iv = bytes([0] * 12)

        time = int(datetime.datetime.now().timestamp())

        aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
        aes.update(str(time).encode('utf-8'))
        encrypted_password, cipher_tag = aes.encrypt_and_digest(password.encode('utf-8'))

        pub_key_bytes = binascii.unhexlify(pub_key)
        seal_box = SealedBox(PublicKey(pub_key_bytes))
        encrypted_key = seal_box.encrypt(key)

        encrypted = bytes([1,
                           key_id,
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(cipher_tag),
                           *list(encrypted_password)])
        encrypted = base64.b64encode(encrypted).decode('utf-8')

        return quote_plus(f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}')

