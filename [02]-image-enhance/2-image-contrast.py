from PIL import Image
from PIL import ImageEnhance

image = Image.open('./fox.jpg')
image.show()

contrast = 3.0
contrastImage = ImageEnhance.Contrast(image)
imageNew = contrastImage.enhance(contrast)
imageNew.show()
imageNew.save('./30.jpg')