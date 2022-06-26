import cv2
import skimage
import numpy as np
from skimage.filters.thresholding import threshold_otsu
from skimage import io

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def obstacle_map(img, outer_iteration, inner_iteration=0):
    current_image = img
    object_map = np.zeros(img.shape)

    for i in range(outer_iteration):
        img_denoise = skimage.restoration.denoise_tv_chambolle(
            current_image, max_num_iter=inner_iteration)
        img_map = current_image - img_denoise
        img_map[img_map < 0] = 0
        object_map = object_map + img_map
        current_image = img_denoise

    current_image = 255 - img

    for j in range(outer_iteration):
        img_denoise = skimage.restoration.denoise_tv_chambolle(
            current_image, max_num_iter=inner_iteration)
        img_map = current_image - img_denoise
        img_map[img_map < 0] = 0
        object_map = object_map + img_map
        current_image = img_denoise

    return object_map


def best_path(object_map, min_path_dist, min_path_width):
    distance_map = np.ones(180)


while True:
    ret, raw_img = cam.read()
    grayscale_img = skimage.color.rgb2gray(raw_img)
    img_obstacle_map = obstacle_map(
        img=grayscale_img, outer_iteration=8, inner_iteration=8)
    denoised_img_obstacle_map = skimage.restoration.denoise_tv_chambolle(
        img_obstacle_map)
    otsu_threshold = threshold_otsu(denoised_img_obstacle_map)
    object_binary = denoised_img_obstacle_map >= otsu_threshold
    object_binary = 1.0*object_binary
    # Todo: K connected
    object_k_connected = skimage.measure.label(object_binary)

    # io.imshow(object_k_connected)
    # io.show()
    # cv2.imshow("img", object_k_connected)

    # object_binary = 1.0*object_binary
    cv2.imshow("obs map1", denoised_img_obstacle_map)
    cv2.imshow("obs map2", object_binary)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

self.cap.release()
cv2.destroyAllWindows()
