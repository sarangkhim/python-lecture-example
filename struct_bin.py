import struct


def main():
    a = -0.1
    b = struct.pack('f', a)
    for d in b[-1::-1]:
        print("%02X" % d, end='')
    print()

    f = struct.unpack('f', b)
    print(f[0])

if __name__ == "__main__":
    main()

