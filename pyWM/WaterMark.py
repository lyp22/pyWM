import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#文字水印
class WordDraw:
    def __init__(self,Url,content="",generateUrl="target.jpg",toLeft=0,toTop=0,font=0):
        WordDraw.Url = Url
        WordDraw.generateUrl = generateUrl
        WordDraw.content = content
        WordDraw.toLeft = toLeft
        WordDraw.toTop = toTop
        WordDraw.font = font

    def generate(self):
        # 设置所使用的字体
        font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)

        # 打开图片
        imageFile = WordDraw.Url
        im1 = Image.open(imageFile)

        # 画图
        draw = ImageDraw.Draw(im1)
        draw.text((WordDraw.toLeft, WordDraw.toTop), WordDraw.content, (255, 0, 0), font=font)  # 设置文字位置/内容/颜色/字体
        draw = ImageDraw.Draw(im1)

        # 另存图片
        im1.save(WordDraw.generateUrl)

#图片水印
class PicDraw:
    def __init__(self,Url,Mask,generateUrl="target.jpg",toLeft=0,toTop=0,font=0):
        PicDraw.Url = Url
        PicDraw.generateUrl = generateUrl
        PicDraw.Mask = Mask
        PicDraw.toLeft = toLeft
        PicDraw.toTop = toTop
        PicDraw.font = font

    def generate(self):
        image = Image.open(PicDraw.Url)
        mark = Image.open(PicDraw.Mask)
        layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
        layer.paste(mark, (PicDraw.toLeft, PicDraw.toTop))
        out = Image.composite(layer, image, layer)
        out.save(PicDraw.generateUrl, 'jpeg')
