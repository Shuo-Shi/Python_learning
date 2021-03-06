# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    if len(s)%4 == 0:
        return base64.b64decode(s)
    else:
        i = (int(len(s)/4)+1)*4-len(s)
        num = 0
        while num < i:
            s += b'='
            num += 1
        return base64.b64decode(s)



# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')