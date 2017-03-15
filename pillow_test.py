from PIL import Image

with Image.open("iu.png") as im:
    rgb = im.convert('RGB')
    gray = im.convert('1')
    w, h = im.size
    for y in range(h):
        for x in range(w):
            p = list(rgb.getpixel((x, y)))
            p[1], p[2] = 0, 0
            p = tuple(p)
            rgb.putpixel((x, y), p)
    gray.show()
    rgb.show()
