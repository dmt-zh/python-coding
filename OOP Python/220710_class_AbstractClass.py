# Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:
# obj = AbstractClass()
# переменная obj должна ссылаться на строку с содержимым: "Ошибка: нельзя создавать объекты абстрактного класса"


class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return f"Ошибка: нельзя создавать объекты абстрактного класса"

obj = AbstractClass()
print(obj)