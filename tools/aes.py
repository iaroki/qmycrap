#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import base64
import hashlib
import argparse
from Crypto import Random
from Crypto.Cipher import AES

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encrypt", help="encrypt input message", action="store_true")
parser.add_argument("-d", "--decrypt", help="decrypt input AES code", action="store_true")
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
inputFile = args.input
outputFile = args.output

f = open('/home/max/passkey.aes', 'r')
passphrase = f.read()
f.close()
passhash = hashlib.sha256(passphrase).digest()

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[0:-ord(s[-1])]

class AESCipher:
    def __init__(self, pwd):
        self.passphrase = pwd

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.passphrase, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.passphrase, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))

aescipher = AESCipher(passhash)

if args.encrypt:
    f = open(inputFile, 'rb')
    message = f.read()
    f.close()
    encrypted = aescipher.encrypt(message)
    f = open(outputFile, 'wb')
    f.write(encrypted)
    f.close()
    print encrypted
elif args.decrypt:
    f = open(inputFile, 'rb')
    message = f.read()
    f.close()
    decrypted = aescipher.decrypt(message)
    f = open(outputFile, 'wb')
    f.write(decrypted)
    f.close()
    print decrypted
else:
    print "wrong key"
