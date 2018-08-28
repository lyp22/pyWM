# -*- coding: utf-8 -*-
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64

def getSignature(message):
    with open('master-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode("utf8"))
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
    with open('signature.pem', 'wb+') as f:
        f.write(signature)
    return signature