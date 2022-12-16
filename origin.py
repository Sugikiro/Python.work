# Необходимо ввести данные о студенте: ФИО, направление подготовки, дату 
# рождения в формате date, номер зачётной книжки. Предусмотрите 
# возможные ошибки при вводе данных с помощью инструментов обработки 
# исключений. 

import datetime

try:
    FiO, napr, day, month, year, num = map(str, input("Введите данные об студенте: ").split())

    date_obj = datetime.datetime(int(year),int(month),int(day))
    print(FiO, napr, date_obj , num)

except ValueError:
    print("тип переменной правильный, но передаваемое значение – нет")
except AttributeError:
    print("невозможности присвоить значение или создать ссылку на атрибут.!")
except IOError:
    print("ошибка ввода/вывода!")
except TypeError :
    print("– возникает, когда операция или функция применяется к объекту несоответствующего типа!")
except ZeroDivisionError:
    print("Oшибка деления на ноль.!")

