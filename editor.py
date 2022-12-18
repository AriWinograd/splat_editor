import imageio.v3 as iio
import numpy as np
from PIL import Image
import io
print("Hello Splatoon World")

import imageio.v3 as iio

# read a single frame
frame = iio.imread(
    "splat_66_il.mp4",
    index=333,
    plugin="pyav",
)
im = Image.fromarray(frame)
im.show()

#print(frame)
print(frame.shape, frame.dtype)
print(frame.size)
print(frame[0].size)
print(frame[0][0].size)
print(frame[0][0][0].size)

#for col in frame:
#     for rgb in col:
#        if not (np.array_equal(rgb, [0, 0, 0])):
#            print(rgb)

# bulk read all frames
# Warning: large videos will consume a lot of memory (RAM)
#frames = iio.imread("imageio:cockatoo.mp4", plugin="pyav")

# iterate over large videos
#for frame in iio.imiter("splat_66_il.mp4", plugin="pyav"):
    #None
    #print(frame)