# десериализация данных из файла c использованием pickle.load
import pickle
fil = input("Введите с клавиатуры имя файла:  ")
d = {}
with open(fil, "rb") as f:
    d = pickle.load(f)
print(type(d))
print(d)