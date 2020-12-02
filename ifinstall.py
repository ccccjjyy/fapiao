from paddleocr import PaddleOCR, draw_ocr


def init():
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
    img_path = './data/3.jpg'
    result = ocr.ocr(img_path, cls=True)
    for line in result:
        print(line)


if __name__ == "__main__":
    init()