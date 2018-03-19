# -*- coding:utf-8 -*-
import zipfile
import threading
import itertools as its


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
    dicfile = open(u"D:\\软件\\dictionary.txt","r")
    info = dicfile.readlines()
    for i in info:
        print i
        try:
            zip.extractall(path=u'D:\\软件\\pojie', pwd=i)
        except:
            pass
    print ' ----success!,The password is %s' % password
    zip.close()


# zippath = u"D:\\软件\\dsad.rar"
# pojie_zip(zippath, "asdf")
# createDic()
