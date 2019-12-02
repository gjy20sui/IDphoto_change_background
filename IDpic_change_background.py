# 此程序基于grabcut算法，可以将证件照中的背景颜色替换成蓝色或者红色。
# 但是原图的分辨率对算法的抠图效果有一定影响，推荐使用700*550左右分辨率的图片
# 如果仍然失真严重的话，可以将原图截图成此分辨率再处理试试。
# This program is based on the grabcut algorithm,
# which can replace the background color in the photo of the document with blue or red.
# However, the resolution of the original image has a certain impact on the matting effect of the algorithm.
# It is recommended to use an image with a resolution of about 700 * 550.
# If the distortion is still serious, you can take a screenshot of the original image to this resolution and try again.
import numpy as np
import cv2
from matplotlib import pyplot as plt

filename = "C:/Users/11078/Desktop/ZJZ.png"
img = cv2.imread(filename)
height, width = img.shape[:2]
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.title("org pic")
plt.imshow(img)
plt.show()

mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (10, 10, width, height)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 10, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img_seg = img * mask2[:, :, np.newaxis]

# set the background color
blue = img
blue[:, :, 0] = 1
blue[:, :, 1] = 190
blue[:, :, 2] = 255

red = img
red[:, :, 0] = 159
red[:, :, 1] = 10
red[:, :, 2] = 11

# change the background color with information from img_seg
img_redback = np.where((img_seg != 0), img_seg, red)[:, 10:, :]
img_blueback = np.where((img_seg != 0), img_seg, blue)[:, 10:, :]
plt.subplot(122)

# show results and save
plt.title('back_changed')
plt.imshow(img_redback)
plt.show()
img_redback = cv2.cvtColor(img_redback, cv2.COLOR_BGR2RGB)
cv2.imwrite(path, img_redback)