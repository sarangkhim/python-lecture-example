"""
name packing done
write watermark done
read watermark done
convert to string NY
"""
import struct
from PIL import Image


def main():
    name = struct.pack('10s', b'sarangkhim')
    bin_name = [b for b in name]
    out_name = []
    len_name = len(bin_name)

    print("[in]")
    for b in bin_name:
        print(bin(b))

    print("---")

    with Image.open("iu.png") as im:
        rgb = im.convert('RGB')
        for j in range(len_name):
            b = bin_name[j]
            for i in range(7):
                p = list(rgb.getpixel((i + j * 8, 0)))
                if b >> i & 1 == 1:
                    if p[2] & 0b1 == 0:
                        p[2] += 1
                else:
                    if p[2] & 0b1 == 1:
                        p[2] -= 1
                p = tuple(p)
                rgb.putpixel((i + j * 8, 0), p)

        for j in range(len_name):
            out_b = 0b0
            for i in range(7):
                p = list(rgb.getpixel((i + j * 8, 0)))
                if p[2] & 0b1 == 1:
                    out_b |= 1 << i
                else:
                    out_b |= 0 << i
            out_name.append(out_b)

        print("[out]")
        for b in out_name:
            print(bin(b))

        rgb.show()
        rgb.save("iu_new.png")

if __name__ == "__main__":
    main()


