import cv2
import matplotlib.pyplot as plt

img_indoor_bgr = cv2.imread("/Users/mustafabookwala/Desktop/Drexel/Pre-Junior/Winter 2025/CS 435/HW1/indoor.png")
img_outdoor_bgr = cv2.imread("/Users/mustafabookwala/Desktop/Drexel/Pre-Junior/Winter 2025/CS 435/HW1/outdoor.png")

img_indoor_rgb  = cv2.cvtColor(img_indoor_bgr,  cv2.COLOR_BGR2RGB)
img_outdoor_rgb = cv2.cvtColor(img_outdoor_bgr, cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(1,3, figsize=(12,4))
axs[0].imshow(img_indoor_rgb[...,0], cmap="gray")
axs[0].set_title("Indoor - R channel")
axs[1].imshow(img_indoor_rgb[...,1], cmap="gray")
axs[1].set_title("Indoor - G channel")
axs[2].imshow(img_indoor_rgb[...,2], cmap="gray")
axs[2].set_title("Indoor - B channel")
for ax in axs:
    ax.axis('off')
plt.show()

fig, axs = plt.subplots(1,3, figsize=(12,4))
axs[0].imshow(img_outdoor_rgb[...,0], cmap="gray")
axs[0].set_title("Outdoor - R channel")
axs[1].imshow(img_outdoor_rgb[...,1], cmap="gray")
axs[1].set_title("Outdoor - G channel")
axs[2].imshow(img_outdoor_rgb[...,2], cmap="gray")
axs[2].set_title("Outdoor - B channel")
for ax in axs:
    ax.axis('off')
plt.show()

img_indoor_lab  = cv2.cvtColor(img_indoor_rgb,  cv2.COLOR_RGB2LAB)
img_outdoor_lab = cv2.cvtColor(img_outdoor_rgb, cv2.COLOR_RGB2LAB)

fig, axs = plt.subplots(1,3, figsize=(12,4))
axs[0].imshow(img_indoor_lab[...,0], cmap="gray")
axs[0].set_title("Indoor - L channel")
axs[1].imshow(img_indoor_lab[...,1], cmap="gray")
axs[1].set_title("Indoor - A channel")
axs[2].imshow(img_indoor_lab[...,2], cmap="gray")
axs[2].set_title("Indoor - B channel")
for ax in axs:
    ax.axis('off')
plt.show()

fig, axs = plt.subplots(1,3, figsize=(12,4))
axs[0].imshow(img_outdoor_lab[...,0], cmap="gray")
axs[0].set_title("Outdoor - L channel")
axs[1].imshow(img_outdoor_lab[...,1], cmap="gray")
axs[1].set_title("Outdoor - A channel")
axs[2].imshow(img_outdoor_lab[...,2], cmap="gray")
axs[2].set_title("Outdoor - B channel")
for ax in axs:
    ax.axis('off')
plt.show()