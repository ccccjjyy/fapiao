from PIL import Image
import pytesseract

image=Image.open('img/dizhi.png')
content=pytesseract.image_to_string(image,lang='chi_sim')
print(content)