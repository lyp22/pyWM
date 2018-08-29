from PIL import Image


def makeImageEven(image):
    pixels = list(image.getdata())
    # with open('Pixels.txt','w') as f:
    #     for line in pixels:
    #         f.write(str(line))
    evenPixels = [(r>>1<<1,g>>1<<1,b>>1<<1) for [r,g,b] in pixels]
    evenImage = Image.new(image.mode, image.size)
    evenImage.putdata(evenPixels)
    return evenImage


def constLenBin(int):
    binary = "0"*(8-(len(bin(int))-2))+bin(int).replace('0b','')
    return binary


def encodeDataInImage(imageUrl, data, saveUrl):
    image = Image.open(imageUrl)
    evenImage = makeImageEven(image)
    binary = ''.join(list(map(constLenBin,bytearray(data, 'utf-8'))))
    # print(binary)
    if len(binary) > len(image.getdata()) * 3:
        raise Exception("Error: Can't encode more than " + len(evenImage.getdata()) * 3 + " bits in this image. ")
    # encodedPixels = [(r+int(binary[index*3+0]),g+int(binary[index*3+1]),b+int(binary[index*3+2])) if index*3 < len(binary) else (r,g,b) for index,(r,g,b) in enumerate(list(evenImage.getdata()))]
    encodedPixels = [(r+int(binary[index*2+0]),g+int(binary[index*2+1]),b) if index*2 < len(binary) else (r,g,b) for index,(r,g,b) in enumerate(list(evenImage.getdata()))]
    # with open('encodedPixels.txt','w') as f:
    #     for line in encodedPixels:
    #         f.write(str(line))
    encodedImage = Image.new(evenImage.mode, evenImage.size)
    encodedImage.putdata(encodedPixels)
    encodedImage.save(saveUrl)


def binaryToString(binary):
    index = 0
    string = []
    rec = lambda x, i: x[2:8] + (rec(x[8:], i-1) if i > 1 else '') if x else ''
    # rec = lambda x, i: x and (x[2:8] + (i > 1 and rec(x[8:], i-1) or '')) or ''
    fun = lambda x, i: x[i+1:8] + rec(x[8:], i-1)
    while index + 1 < len(binary):
        chartype = binary[index:].index('0')
        length = chartype*8 if chartype else 8
        string.append(chr(int(fun(binary[index:index+length],chartype),2)))
        index += length
    return ''.join(string)


def decodeImage(imageUrl):
    image = Image.open(imageUrl)
    pixels = list(image.getdata())
    # binary = ''.join([str(int(r-(r>>1<<1)))+str(int(g-(g>>1<<1)))+str(int(b-(b>>1<<1))) for (r,g,b) in pixels])
    binary = ''.join([str(int(r-(r>>1<<1)))+str(int(g-(g>>1<<1))) for (r,g,b) in pixels])
    # print(binary)
    locationDoubleNull = binary.find('0000000000000000')
    endIndex = locationDoubleNull+(8-(locationDoubleNull % 8)) if locationDoubleNull%8 != 0 else locationDoubleNull
    # print(binary[0:endIndex])
    data = binaryToString(binary[0:endIndex])

    return data
