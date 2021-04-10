import cv2
import numpy as np


# We are going to use:
# 1. resize
# 2. Median blurring


class PreprocessedImage:

    def __init__(self, image):
        self.image = cv2.imread(image)

    def run(self):
        return self.median_blurring(self.resize(self.image))

    def run_with_grayscale(self):
        return self.gray_scalling(self.median_blurring(self.resize(self.image)))

    def run_with_binary(self):
        return self.adaptive_threshold(self.gray_scalling(self.median_blurring(self.resize(self.image))))

    # Use INTER_CUBIC - Better
    # OR
    # Use INTER_LINEAR - Faster
    def resize(self, img):
        return cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    def averaging(self, img):
        return cv2.blur(img, (5, 5))

    # Faster, doesn't preserve edges
    def gaussian_blurring(self, img):
        return cv2.GaussianBlur(img, (5, 5), 0)

    # Slower, preserve edges
    def median_blurring(self, img):
        return cv2.medianBlur(img, 3)

    # Slowest, preserve edges, more better
    def bilateral_filter(self, img):
        return cv2.bilateralFilter(img, 9, 75, 75)

    def normal_threshold(self, img):
        return cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Use ADAPTIVE_THRESH_GAUSSIAN_C
    # OR
    # Use ADAPTIVE_THRESH_MEAN_C - Better result
    def adaptive_threshold(self, img):
        return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    def gray_scalling(self, img):
        kernel = np.ones((1, 1), np.uint8)
        return cv2.erode(cv2.dilate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), kernel, iterations=1), kernel, iterations=1)

    # Convert to gray
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply dilation and erosion to remove some noise:
    # kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
