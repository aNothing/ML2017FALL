from PIL import Image

# open the image
img = Image.open('westbrook.jpg')

# use point() method to deal with pixels
out = img.point(lambda i: int(i*0.5))

# save image
out.save('Q2.jpg')