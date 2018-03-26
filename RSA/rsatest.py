# -*- coding: utf-8 -*-
import rsa
from Crypto.PublicKey import RSA


def get_d(p, q, e):
    """
    仅限于不是long的整数
    RSA算法取私钥d
    d满足公式:e*d-1=(p-1)(q-1)
    :param p:一个素数
    :param q:一个素数
    :param e:一个随机数，可以从公钥拿到,公钥可以拿到e和n,n=p*q
    :return:
    """
    d = ((p - 1)(q - 1) + 1) / e
    return d


def creatprivatekey(p, q, e):
    """
    根据p,q,e生成d，然后再填充生成最终的秘钥
    :param p:
    :param q:
    :param e:
    :return:
    """
    keypair = RSA.generate(1024)

    keypair.p = p
    keypair.q = q
    keypair.e = e

    keypair.n = keypair.p * keypair.q
    Qn = long((keypair.p - 1) * (keypair.q - 1))

    i = 1
    while True:
        x = (Qn * i) + 1
        if x % keypair.e == 0:
            keypair.d = x / keypair.e
            break
        i += 1

    private = open('D:\\YQworckspace\\CTF\\RSA\\private.pem', 'w')
    private.write(keypair.exportKey())
    private.close()


def createkey():
    """自动随机生成一对密钥，然后保存.pem格式文件，当然也可以直接使用"""
    (pubkey, privkey) = rsa.newkeys(1024)

    pub = pubkey.save_pkcs1().decode()
    pubfile = open('public.pem', 'w+')
    pubfile.write(pub)
    pubfile.close()

    pri = privkey.save_pkcs1().decode()
    prifile = open('private.pem', 'w+')
    prifile.write(pri)
    prifile.close()

# load公钥和密钥
with open('public.pem', 'r') as publickfile:
    p = publickfile.read()
    pubkey = rsa.PublicKey.load_pkcs1(p.encode())

with open('private.pem', 'r') as privatefile:
    p = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(p.encode())

print type(privkey)
#
#
# file1 = open("C:\\Users\\fuzhi\\Desktop\\flag.enc", "r")
# message = file1.read()
message = '57R9S980RNOS49973S757PQO9S80Q36P'

# 用公钥加密、再用私钥解密
crypto = rsa.encrypt(message, pubkey)

message = rsa.decrypt(message, privkey)
print message

# sign 用私钥签名认真、再用公钥验证签名
# signature = rsa.sign(message, privkey, 'SHA-1')
# rsa.verify('hello', signature, pubkey)
