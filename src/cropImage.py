from PIL import Image

# mengambil gambar
origin = Image.open("./peppers.tif")

# menampilkan gambar
origin.show() 

# get orginal dimensions
width, height = origin.size 

# crop image by coordinate (x,y) = (left, upper), (x,y) = (right, lower)
imgCr11 = origin.crop((0,0,width/2,height/2));
imgCr12 = origin.crop((width/2,0,width,height/2));
imgCr21 = origin.crop((0,height/2,width/2,height));
imgCr22 = origin.crop((width/2,height/2,width,height));

# save image
imgCr11.save('./imgCr11.jpg');
imgCr12.save('./imgCr12.jpg');
imgCr21.save('./imgCr21.jpg');
imgCr22.save('./imgCr22.jpg');

# show croppedImage
imgCr11.show()
imgCr12.show()
imgCr21.show()
imgCr22.show()