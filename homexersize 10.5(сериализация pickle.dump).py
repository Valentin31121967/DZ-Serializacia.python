# cериализация данных в файл c использованием pickle.dump
import pickle
d = {}
def user_input():
            surname = str(input('Введите фамилию студента'))
            name = str(input('Введите имя студента'))
            patronymic = str(input('Введите отчество студента'))
            age = input('Введите возраст студента')
            d = {'first': surname, 'second': name, ' third': patronymic, 'age': age}
            return d
p = user_input()
print(p)
fil = input("Введите с клавиатуры имя файла:  ")
with open(fil, 'wb') as f:
    pickle.dump(p, f)
