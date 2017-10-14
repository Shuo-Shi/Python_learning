#!/sur/bin/python3
#-*- coding: utf-8 -*-

import sys
import struct

#struct.pack(fmt, v1, v2, ...)
#struct.unpack(fmt, buffer)

#format
#<      little-endian
#>      big-endian
#c      char            (1 byte)
#I      unsigned int    (4 bytes)
#H      unsigned short  (2 bytes)

#If check_bmp.py can check File is't BMP,
#Yes, print BMP's size and colors,
#No, print This File is unnkown.

def readBmpFile(file):
    f = open(file, 'rb')
    bs = f.read()
    f.close()
    return bs[0:30]

def checkBmp(info):
    # bypes to Corresponding data type    
    ts = struct.unpack('<ccIIIIIIHH', info)

    if ts[0] == b'B' and ts[1] == b'M':
        print('File Type: bmp')
        print('size: %d * %d' % (ts[6], ts[7]))
        print('colors: %d' % ts[9])
    else:
        print('File Type: unknown')
    print('--------------------------\n')

if __name__=='__main__':
    if len(sys.argv) == 2:
        info = readBmpFile(sys.argv[1])
        checkBmp(info)
    else:
        print('Please input two parameter: python3 check_bmp.py ***')