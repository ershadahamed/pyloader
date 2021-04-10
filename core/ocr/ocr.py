import time
import easyocr
import cv2
import numpy as np
import pytesseract
from core.ocr.PreprocessedImage import PreprocessedImage


def tesseract(image):
    start = time.time()
    img = PreprocessedImage(image).run_with_grayscale()
    ocr = pytesseract.image_to_data(img)
    end = time.time()

    cv2.imshow('sd', img)
    cv2.waitKey(0)

    print(f'Time taken: {end-start}')
    return ocr


def run(gpu, image):
    start = time.time()

    image = '../../assets/images/' + image

    reader = easyocr.Reader(['en'], gpu=gpu)
    result = reader.readtext(image)

    end = time.time()

    for r in result:
        accuracy = round(r[2] * 100, 2)
        the_str = r[1]
        if accuracy > 85:
            print(f'Text: {the_str} having accuracy at {accuracy} %')

    if gpu:
        print(f'Total time taken with GPU/CUDA: {end - start}')
    else:
        print(f'Total time taken with out GPU/CUDA: {end - start}')


# run(False)
# print('PAUSE')
# run(True, 'text1.jpg')
# run(True, 'text2.jpg')
# run(True, 'text3.png')
# run(True, 'text4.png')

print(tesseract('../../assets/images/text2.jpg'))
