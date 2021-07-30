# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests
# и посчитать число строк в нём. Используйте функцию get для получения файла (имеет смысл вызвать метод strip
# к передаваемому параметру, чтобы убрать пробельные символы по краям).
# После получения файла вы можете проверить результат, обратившись к полю text.
# В поле ответа введите одно число или отправьте файл, содержащий одно число.

import requests

url = 'https://stepic.org/media/attachments/course67/3.6.2/296.txt'
req = requests.get(url)
txt = req.text
splitted = txt.splitlines()
print(len(splitted))
