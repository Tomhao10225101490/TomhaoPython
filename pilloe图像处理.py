import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('Lena.png')
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.imshow(img)

plt.subplot(122)
img_region = img.crop((100,100,500,500))
plt.imshow(img_region)

plt.show()

plt.subplot(122)
img_region = img.crop((100,100,500,500))
plt.imshow(img_region)

plt.show()