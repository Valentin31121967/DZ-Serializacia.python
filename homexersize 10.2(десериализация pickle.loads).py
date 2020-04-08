# десериализация данных из файла c использованием pickle.loads
import pickle
fil = input("Введите с клавиатуры имя файла:  ")
d = {}
with open(fil, "rb") as f:
    d_pickle_loads = f.read()
print(type(d_pickle_loads))
d = pickle.loads(d_pickle_loads)
print(type(d))
print(d)