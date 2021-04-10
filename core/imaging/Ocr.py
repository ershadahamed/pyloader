import time
import easyocr
import pytesseract
from core.imaging.PreprocessedImage import PreprocessedImage


class Ocr:
    pass


def tesseract(image):

    try:
        start = time.time()
        img = PreprocessedImage(image).run_with_grayscale()
        ocr = pytesseract.image_to_data(img)
        end = time.time()
    except Exception as e:
        print(f'Some problem: {e}')
    else:
        # cv2.imshow('Sample Image', img)
        # cv2.waitKey(0)

        print(f'Time taken: {end-start}')
        # main data needed here is OCR variable, below just the logics for this data
        out = ocr.splitlines()
        output = []
        for o in out[1:]:
            if int(o.split('\t')[10]) > 50:
                output += o.split('\t')[-1:]

        return output


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


print(tesseract('../../assets/images/text2.jpg'))
