"""
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат(разделение полей рекомендуется делать через
                            точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.Например:
"""
import json
from datetime import datetime

"""модуль для получения текущей даты"""


def data():
    date_log = datetime.now()
    date = str(date_log.strftime("%d-%m-%Y %H:%M:%S"))
    return date

# Метод 'past' делает запись в файл


def past():
    flag = True
    with open('Note.json', 'r') as file:
        try:
            obj = json.load(file)
        except json.decoder.JSONDecodeError:
            temp = {'note': []}
            temp_dats = ({data(): [str(input("Введите заметку "))]})
            temp['note'].append(temp_dats)
            with open('Note.json', 'w+') as file:
                json.dump(temp, file, ensure_ascii=False, indent=4)
                print(f"Добавлена заметка : {temp_dats}")
            flag = False
    if (flag):
        with open('Note.json') as file:
            new_file = json.load(file)
            temp_dats = ({data(): [str(input("Введите заметку "))]})
            new_file['note'].append(temp_dats)
            with open('Note.json', 'w+') as fil:
                json.dump(new_file, fil, ensure_ascii=False, indent=4)
            print(f"Добавлена заметка : {temp_dats}")

# Метод 'print_note' сделан для вывода всех имеющихся записей в файле


def print_note():
    with open('Note.json', 'r+', encoding='utf8') as file:
        obj = json.load(file)
    for section, writ in obj.items():
        print(f"Раздел - {section}")
        for note in writ:
            for key, val in note.items():
                new_val = (val[0])
                print(f"Дата заметки: {key}. Ваша запись : {new_val}")


"""В блоке 'redactor_note' происходит вывод в консоль всех имеющихся записей.
Далее необходимо выбрать какую запись нужно редактировать и соответственно на какую 
запись меняем."""


def redactor_note(num_note):
    if (num_note == 0):
        with open('Note.json', 'r+', encoding='utf8') as file:  # Открываем файл
            obj = json.load(file)
            num = 0
            for section, writ in obj.items():  # Выводим все имеющиеся заметки в консоль
                # Делал так для более красивого вывода
                print(f"Раздел - {section}")
                for note in writ:
                    for key, val in note.items():
                        new_val = (val[0])
                        num += 1
                        print(
                            f"{num} Дата заметки: {key}. Ваша запись : {new_val}")
                num_note_redact = int(
                    input("Введите номер заметки для ее редактирования "))
            redactor_note(num_note_redact)
    else:
        txt_note_redact = str(input("Введите новый текст заметки "))
        with open('Note.json', 'r+', encoding='utf8') as file:
            # В данном блоке происходит замена выбранной заметки и вывод новой заметки в консоль
            obj = json.load(file)
            num = 0
        for section, write in obj.items():
            for note in write:
                for keys, value in note.items():
                    num += 1
                    if (num == num_note):
                        keys_note = keys
                        value[0] = txt_note_redact
        with open('Note.json', 'w+', encoding='utf8') as file:
            json.dump(obj, file, ensure_ascii=False, indent=4)
            print(f"Заметка - {keys_note} Изменена на - {txt_note_redact}")


# Метод который вызывает необходимые методы для работы.
def core_note():
    number = int(input(
        "Выберите действие : \n0 - выход из приложения \n1 - сделать запись \n2 - Просмотреть записи \n3 - Редактирование записи "))
    if (number == 0):
        print("Программа завершена")
        return 0
    if (number == 1):
        past()
    if (number == 2):
        print_note()
    if (number == 3):
        redactor_note(0)
    return core_note()

core_note()
