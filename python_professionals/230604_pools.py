# Тимур планирует пойти в бассейн. Среди всех бассейнов ему подходят те, которые открыты в понедельник в
# период с 10:00 до 12:00. Также ему нравится плавать по длинным дорожкам, поэтому из всех работающих в это
# время бассейнов нужно выбрать бассейн с наибольшей длиной дорожки, при равных значениях — c наибольшей шириной.

# Вам доступен файл pools.json, содержащий список JSON-объектов, которые представляют данные о крытых плавательных бассейнах:

# [
#    {
#       "ObjectName": "Физкультурно-оздоровительный комплекс с бассейном «ГБУ «СШОР № 82» Москомспорта»",
#       "AdmArea": "Северо-Восточный административный округ",
#       "District": "Алтуфьевский район",
#       "Address": "Инженерная улица, дом 5, корпус 1",
#       "WorkingHoursSummer": {
#          "Понедельник": "10:00-11:00",
#          "Вторник": "10:00-11:00",
#          "Среда": "10:00-11:00",
#          "Четверг": "10:00-11:00",
#          "Пятница": "10:00-11:00",
#          "Суббота": "10:00-11:00",
#          "Воскресенье": "09:00-15:00",
#       },
#       "DimensionsSummer": {
#          "Square": 350,
#          "Length": 25,
#          "Width": 14,
#          "Depth": 1.8
#       }
#    },
#    ...
# ]

# Под «бассейном» будем подразумевать один JSON-объект из этого списка. У бассейна имеются следующие атрибуты:

# ObjectName — название, будь то фитнес клуб или спортивный комплекс
# AdmArea — административный округ
# District — название района
# Address — адрес
# WorkingHoursSummer — график работы, время начала и закрытия указываются в формате HH:MM
# DimensionsSummer — размеры бассейна, где Square — площадь, Length — длина, Width — ширина, Depth — глубина

# Напишите программу, которая определяет бассейн, подходящий Тимуру. Программа должна вывести его размеры и адрес в следующем формате:
# <длина>x<ширина>
# <адрес>


import json
import pandas as pd
import re


with open('pools.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

df = pd.json_normalize(data)

cols = ['DimensionsSummer.Length', 'DimensionsSummer.Width', 'Address']
df['mondays'] = df['WorkingHoursSummer.Понедельник'].apply(lambda x: bool(re.match(r'10:00-1[2-9]:\d\d', x)))

best = df[(df['mondays'] == True)][cols] \
    .sort_values(by=['DimensionsSummer.Length', 'DimensionsSummer.Width'], ascending=[False, False]).head(1).values[0]

print(f"{int(best[0])}x{int(best[1])}\n{best[2]}")