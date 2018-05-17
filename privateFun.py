# -*- coding:utf-8 -*-
import zipfile
import threading
import itertools as its
import string
import base64
import hashlib
import rarfile


def base64dec(msg):
    return base64.b64decode(msg)


def base64enc(msg):
    return base64.b64encode(msg)


def createDic(words, repeatcnt):
    """
    生成密码字典
    :param words: 字符组合
    :param repeatcnt: 字符组合
    :return:
    """
    r = its.product(words, repeat=repeatcnt)
    dic = open(u"D:\\软件\\dictionary.txt", 'w')
    for i in r:
        dic.write("".join(i) + "\n")
    dic.close()


def pojie_zip(path, password):
    """
    解压zip文件
    :param path: 文件地址
    :param password: 解压密码
    :return:
    """
    zip = zipfile.ZipFile(path, 'r')
    print zip.namelist()

    try:
        zip.extractall(path=u'D:\\软件\\pojie', pwd=password)
    except:
        pass
    print ' ----success!,The password is %s' % password
    zip.close()


def pojie_rar(path, password):
    """
    解压zip文件
    :param path: 文件地址
    :param password: 解压密码
    :return:
    """
    rar = rarfile.RarFile(path, 'r')
    try:
        rar.extractall(path='D:\\软件\\pojie', pwd=password)
    except rarfile.RarWrongPassword:
        print ' ----fail!,The password is not %s' % password
    else:
        print ' ----success!,The password is %s' % password
        rar.close()
        return True
    rar.close()
    return False


def strsplit(mystr, number):
    """
    等比切割字符串
    :param mystr: 原字符串
    :param number: 按number切
    :return:
    """
    return [mystr[i:i + number] for i in xrange(0, len(mystr), number)]


def issushu(x):
    """判断是否是素数"""
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


def caesarDecrypt(cipertext, n):
    """
    凯撒解密，或加密，输入一串字符，通过+n或者+(-n)，变成新的一串字符
    :param cipertext: 一串待转换字符
    :param n: 移位的数，例如1或-1
    :return: 移位后的字符串
    """
    plaintext = ""
    for x in cipertext:
        if x in string.uppercase:
            ascindex = 65 + (ord(x) - 65 + n) % 26
            plaintext = plaintext + chr(ascindex)
        elif x in string.lowercase:
            ascindex = 97 + (ord(x) - 97 + n) % 26
            plaintext = plaintext + chr(ascindex)
        else:
            plaintext = plaintext + x
    return plaintext


def get_d(p, q, e):
    """
    仅限不是long的整数
    RSA算法取私钥d
    d满足公式:e*d-1=(p-1)(q-1)
    :param p:一个素数
    :param q:一个素数
    :param e:一个随机数，可以从公钥拿到,公钥可以拿到e和n,n=p*q
    :return:
    """
    d = ((p - 1) * (q - 1) + 1) / e
    return d


def creatediymd5():
    """生成指定的md5"""
    for i in range(1, 99999999):
        if hashlib.md5(i).hexdigest().startswith('e4df2f'):
            print i
            break


def intToAsicc(msg):
    cipertext = msg
    i = 0
    plaintext = ""
    while i < len(cipertext)-1:
        plaintext += chr(int(cipertext[i:i + 2], 16)) + " "
        i += 2
    return plaintext


s = "69742773206561737921"
print intToAsicc(s)
