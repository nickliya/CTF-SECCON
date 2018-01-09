# coding=utf-8
# create by 401219180 2017/01/09

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"


def _l(idx, s):
    return s[idx:] + s[:idx]


def main(p, k1, k2):
    t = [[_l((i + j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    i1 = 0
    i2 = 0
    c = ""
    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        d = t[18][27][32]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return c


# print main(sys.argv[1], sys.argv[2], sys.argv[2][::-1])
# print main("SECCON{", "AAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAA")


'''
$ python Vigenere3d.py SECCON{**************************} **************
POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9
'''

# 解法1 把密文当明文，之前的明文就成了密文，根据前七位推出新key，然后加密，加密后的密文就是以前的明文
cipher = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
key = "AAAAAAAAAAAAAA"
# key = "Dtobe3DAAAAAAA"
plain_head = "SECCON{"

for i in range(7):
    target_char = plain_head[i:i + 1]
    j = 0
    while main(cipher, key, key[::-1])[i:i + 1] != target_char:
        key = key[:i] + s[j:j + 1] + key[i + 1:]
        j += 1

print main(cipher, key, key[::-1])


# 解法2 暴力爆破
def sa(s1, s2):
    # 找比值，用密文减去明文得key的比值
    c = []
    for i in range(7):
        i1 = s.find(s1[i])
        i2 = s.find(s2[i])
        c.append(i1 - i2)
    return c


def dec(src, key):
    # 用得到比值和密文反推明文
    c = ""
    keyall = key + key[::-1]
    for i in range(len(src)):
        c = c + s[(s.find(src[i]) + keyall[i % len(keyall)]) % len(s)]  # %求余数
    return c


key = sa("SECCON{", "POR4dny")
answser = dec("POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9", key)
print answser
