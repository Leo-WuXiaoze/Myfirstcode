import numpy as np
from PIL import Image

image = Image.open("../data/特征值与目标值.jpg")
print(image,type(image))

im = np.array(image)
print("原始矩陣：",type(im),im.shape,im.dtype)
im = np.arange(487*1067).reshape(487,1067)
im = [255] - im
print("新矩陣：",type(im),im.shape,im.dtype)
im = Image.fromarray(im.astype(np.uint8))
im.save("../data/123.jpg")

