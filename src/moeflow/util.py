# -*- coding: utf-8 -*-
import cv2
import logging
import math
import numpy as np

WIDTH_HEIGHT_LIMIT = 800  # in pixel


def resize_large_image(image_data):
    img_array = np.fromstring(image_data, dtype=np.uint8)
    image = cv2.imdecode(img_array, 0)
    height, width = image.shape[:2]
    logging.info("Height: {}, Width: {}".format(height, width))
    if height > width and height > WIDTH_HEIGHT_LIMIT:
        ratio = float(WIDTH_HEIGHT_LIMIT) / float(height)
        new_width = int((width * ratio) + 0.5)
        return cv2.resize(
            image,
            (new_width, WIDTH_HEIGHT_LIMIT),
            interpolation=cv2.INTER_AREA
        )
    else:
        ratio = float(WIDTH_HEIGHT_LIMIT) / float(width)
        new_height = int((height * ratio) + 0.5)
        return cv2.resize(
            image,
            (WIDTH_HEIGHT_LIMIT, new_height),
            interpolation=cv2.INTER_AREA
        )
