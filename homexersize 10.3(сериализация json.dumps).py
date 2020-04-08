# cериализация данных в файл c использованием json.dumps
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
json_dumps_d = json.dumps(dict_student)
with open(fil, 'w') as f:
    f.write(json_dumps_d)
print(json_dumps_d)