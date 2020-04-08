# деcериализация данных в файл c использованием json.load
import json
fil = str(input("Введите с клавиатуры имя файла:  "))
d = {}
with open(fil, "r") as f:
    d = json.load(f)
print(type(d))
print(d)