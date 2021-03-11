import os
from PIL import Image

for filename in os.listdir("images"):
    #print(filename)
    imgin = "images/"+filename
    imgout = "opt/icons/"+filename+".jpg"
    try:
        im = Image.open(imgin).convert("RGB").rotate(270).resize((128,128)).save(imgout)
        #print(im.format,im.size,im.mode)
    except OSError:
        pass
