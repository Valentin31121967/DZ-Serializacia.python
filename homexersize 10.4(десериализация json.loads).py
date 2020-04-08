# деcериализация данных в файл c использованием json.loads
import json
fil = str(input("Введите с клавиатуры имя файла:  "))
d = {}
with open(fil, "r") as f:
    json_loads_d = f.read()
d = json.loads(json_loads_d)
print(type(json_loads_d))
print(type(d))
print(d)
