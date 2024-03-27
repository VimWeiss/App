import pytesseract
from PIL import Image


#открываем файл
picture = Image.open('001-002.jpg')
#считываем имя файла и берем название до точки
file_name = picture.filename
file_name = file_name.split(".")[0]
#распознаем текст на картинке
text = pytesseract.image_to_string(picture)
#записываем результат в текстовый файл
with open(f'{file_name}.txt', 'a') as text_file:
    text_file.write(text)


