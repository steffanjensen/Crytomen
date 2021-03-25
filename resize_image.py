from PIL import Image

from resizeimage import resizeimage



def resize_image(image, token):
    with open(image, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [128, 128])
            cover.save('128/' + token, image.format)
            cover = resizeimage.resize_cover(image, [64, 64])
            cover.save('64/' + token, image.format)
            cover = resizeimage.resize_cover(image, [32, 32])
            cover.save('32/' + token, image.format)


token = "***.png"
image = "original/" + token

resize_image(image, token)
