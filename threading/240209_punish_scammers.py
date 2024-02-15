# Вы якобы выиграли бесплатную PlayStation 5, вас просят лишь ввести данные своей кредитной карты и заплатить 1 дол. за доставку.
# Само собой сайт фейковый, который ворует данные карты владельца и, видимо, 1 дол. Если заполнить поля ввода для кредитной карты,
# сайт для проверки валидности карты отправляет запросы на реальный сервис проверки, который обходится мошеннику в 5 центов за запрос.
# А сам запрос длится ~2 секунды.

# Но вот беда, мошенник поумнел и построил защиту, которая блокирует проверочные запросы для не уникальных или не валидных кредитных карт,
# поэтому заспамить проверку только одной картой теперь уже не получится. Напишите решение с учетом этого нового условия, чтобы в течении 4 секунд
# мошенник потерял 3 доллара (не менее 3 долларов).

# Валидные кредитные карты - это карты с номерами в диапазоне 4007000000028 - 4007000000099 включительно.

# В тестирующей системе проверяется, что:
# - Ваше решение за 4 секунды (или менее) приводит к уменьшению баланса мошенника на 3 доллара (или больше).
# - Ваше решение "не зависает" и выполняется не более 5 секунд.


import threading
from time import sleep

def do_request(card_number):
    sleep(2)

tasks = [threading.Thread(target=do_request, args=(card,), daemon=True) for card in range(4007000000028, 4007000000099)]
for task in tasks:
    task.start()

sleep(3.5)