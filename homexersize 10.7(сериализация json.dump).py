# cериализация данных в файл c использованием json.dump
import json
d = {}
def user_input():
            surname = str(input('Введите фамилию студента'))
            name = str(input('Введите имя студента'))
            patronymic = str(input('Введите отчество студента'))
            age = input('Введите возраст студента')
            d = {'first': surname, 'second': name, ' third': patronymic, 'age': age}
            return d
dict_student = user_input()
print(dict_student)
fil = str(input("Введите с клавиатуры имя файла:  "))
with open(fil, 'w') as f:
    json.dump(dict_student, f)
