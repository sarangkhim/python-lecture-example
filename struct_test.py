import struct

f = open("sample.data", "r+b")
ft = struct.unpack('6s', f.read(6))[0]
if ft == b'STM32F':
    moder = struct.unpack('I', f.read(4))[0]
    idr = struct.unpack('I', f.read(4))[0]
    odr = struct.unpack('I', f.read(4))[0]
    print("origin\n\tmoder = {}\n\t  idr = {} \n\t  odr = {}".format(bin(moder), bin(idr), bin(odr)))

    moder |= 0b01 << 8 * 2
    odr |= 0b1 << 8
    print("modity\n\tmoder = {}\n\t  idr = {} \n\t  odr = {}".format(bin(moder), bin(idr), bin(odr)))
