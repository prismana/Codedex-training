import imageio.v3 as iio

# Store the image in var
filenames = ['dino/dino1.png', 
             'dino/dino2.png',
             'dino/dino3.png',
             'dino/dino4.png',]
images = []

# Load image using imread from imageio module
for filename in filenames:
    images.append(iio.imread(filename))

# Turn image to gif using imwrite method
iio.imwrite('dino.gif', images, duration=500, loop=0)