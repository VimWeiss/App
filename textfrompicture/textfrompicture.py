#pip install pytesseract pillow
#sudo apt install tesseract-ocr

import pytesseract
from PIL import Image
#открываем файл
picture = Image.open('1.jpeg')
#считываем имя файла и берем название до точки
file_name = picture.filename
file_name = file_name.split(".")[0]
#распознаем текст на картинке
text = pytesseract.image_to_string(picture)
#записываем результат в текстовый файл
with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(text)


