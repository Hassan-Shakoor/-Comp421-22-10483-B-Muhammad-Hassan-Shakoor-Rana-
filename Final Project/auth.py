#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase
import rsa
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

class MyAuth(AuthBase):
    """
    A custom basic authentication class for requests, that takes into account the organisation header
    """
    def __init__(self, *args):
        if len(args) == 3:
            self.username = args[0]
            self.password = args[1]
            self.organisation = args[2]

        elif len(args) == 2:
            self.api_key = args[0]
            self.organisation = args[1]

    ## Generate Public and Private Keys and save to file
    def generate_keys():
        new_key = RSA.generate(2048)       ## generating public key using rsa library built-in method newkeys
        public_key = new_key.publickey().exportKey("PEM")
    	##(pubkey , privkey) = rsa.newkeys(1024)
    	return public_key

    ## Encrypting the Plain Text using Public Key
    def encrypt(message , pubkey):
    	return rsa.encrypt(message.encode('utf8') , pubkey)		## encrypting the plain text to cipher text using RSA library built-in method 'encrypt'

    def __call__(self, req):
        pbkey = generate_keys();
        if len(args) == 3:
            user = encrypt(self.username , pbkey)
            passw = encrypt(self.password , pbkey)
            req.headers['Authorization'] = requests.auth._basic_auth_str(user, pasw)
        elif len(args) == 2:
            api_k = encrypt(self.api_key , pbkey)
            req.headers['Authorization'] = 'Bearer {}'.format(api_k)
        if self.organisation is not None:
            req.headers['X-Organisation'] = self.organisation

        return req
