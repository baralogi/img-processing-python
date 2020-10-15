from PIL import Image

origin = Image.open("./peppers.tif")

# get original size
width, height = origin.size 

# image background configuration
mTop = 5
mBottom = 5
mLeft = 5
mRight = 5
mode = 'RGB'
size = ((width + mLeft + mRight + 5) , (height + mTop + mBottom + 5))
# size = (600,600)
color = (255, 255, 0)

# pick background image
background = Image.new(mode, size, color)

# show background image
background.show()

# copy background image
backgroundCopy = background.copy()

# pick 1,1 image
imgCr11 = Image.open("./imgCr11.jpg")
# pick 1,2 image
imgCr12 = Image.open("./imgCr12.jpg")
# pick 2,1 image
imgCr21 = Image.open("./imgCr21.jpg")
# pick 2,2 image
imgCr22 = Image.open("./imgCr22.jpg")


# combine image to backgroundImage
backgroundCopy.paste(imgCr11,(mLeft, mTop))
backgroundCopy.paste(imgCr12,(int((width + mLeft + mRight)/2)+5,mRight))
backgroundCopy.paste(imgCr21,(mLeft,int((height + mTop + mBottom)/2)+5))
backgroundCopy.paste(imgCr22,(int((width + mLeft + mRight)/2)+5,int((height + mTop + mBottom)/2)+5))
backgroundCopy.show()

