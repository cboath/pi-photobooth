from PIL import Image

img2 = '/home/pi/ttr/Projects/Python/photobooth/img(1).jpg'
img1 = '/home/pi/ttr/Projects/Python/photobooth/img(0).jpg'

def merge_images(img1, img2):
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    
    (width1, height1) = image1.size
    (width2, height2) = image2.size
    
    result_width = width1 #+ width2
    result_height = max(height1, height2)
    
    result = Image.new('RGB', (result_width, (result_height * 2)))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(0, height1))
    return result

def smash():
    merge = merge_images(img1, img2)
    merge.save('imgmerge.jpg')