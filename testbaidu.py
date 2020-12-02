from aip import AipOcr

if __name__ == "__main__":
    # 此处填入在百度云控制台处获得的appId, apiKey, secretKey的实际值
    appId, apiKey, secretKey = ['23077616', '6FlEkzTZhREpWzPiWWtGGdjt', 'wqoMOGQEMGOlc8DVCyLfgjnKhinsSYH6']
    # 创建ocr对象
    ocr = AipOcr(appId, apiKey, secretKey)
    with open('img/dizhi.png', 'rb') as fin:
        img = fin.read()
        res = ocr.basicGeneral(img)
        print(res)