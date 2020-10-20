from PIL import Image 
from PIL import ImageEnhance 

gambar4 = Image.open('./assets/demo_2.jpg')
gambar4.show()
gambar4 = gambar4.convert('RGBA')
r,g,b,alpha = gambar4.split()
img = Image.merge('RGBA', (b,g,r,alpha))


img.show()
img.save('./b-r.png')