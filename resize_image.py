from PIL import Image

from resizeimage import resizeimage

def change_pixel():
    im = Image.open("cryptopink.png")
    pixels = im.load()

    # Change pixel from x to y 
    for i in range(100, 300): 
        pixels[i, 50] = (255, 0, 0)

    im.save("pixel_grid.png")

def image_layer():
  
    # Opening the primary image (used in background)
    img1 = Image.open(r"cryptopink.png")
  
    # Opening the secondary image (overlay image)
    img2 = Image.open(r"view2.png")
  
    # Pasting img2 image on top of img1 
    # starting at coordinates (0, 0)
    img1.paste(img2, (0,0), mask = img2)
  
    # Displaying the image
    img1.show()


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
image_layer()
