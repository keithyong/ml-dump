from PIL import Image
import numpy as np

im = Image.open("dango.jpg")

m = []
for x in range(0, im.size[0]):
    m.append([])
    for y in range(0, im.size[1]):
        pixel = im.getpixel((x, y))
        m[x].append(list(pixel))

img_vec = np.array(m)
shape = img_vec.shape

# Cut the image in half vertically
img_vec_1st_half = img_vec[0:np.floor(shape[0]/2)]
img_vec_2nd_half = img_vec[0:np.ceil(shape[0]/2)]

im1 = Image.fromarray(img_vec_1st_half.tolist())
