import os
import csv
from datetime import datetime

#Конструктор класса Visitor.
class Visitor:
    def __init__(self, number, datetime, inout, gender):
        self.number = number
        self.datetime = datetime
        self.inout = inout
        self.gender = gender
#Возвращает строковое представление объекта класса Visitor.
    def __repr__(self):
        return f"{self.number} {self.datetime} {self.inout} {self.gender}\n"

class Data:
    # Конструктор класса Data
    def __init__(self):
        self.visitors = []
# Получает элемент из списка посетителей по индексу
    def __getitem__(self, index):
        return self.visitors[index]
# Устанавливает значение атрибута объекта класса.
    def __setattr__(self, name, value):
        if name == "visitors":
            object.__setattr__(self, name, value)
        else:
            raise AttributeError("You can't set attribute directly")
#Читает данные из файла CSV и добавляет их в список словарей
    def read_data(self, filename='data.csv'):
        if not os.path.exists(filename):
            print("Файл не найден.")
            return
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                number = int(row[0])
                datetime = row[1]
                inout = bool(row[2])
                gender = row[3]
                visitor = Visitor(number, datetime, inout, gender)
                self.visitors.append(visitor)

    # Сортировка таблицы по столбцу "gender"
    def sort_by_str(self):
        sorted_list = sorted(self.visitors, key=lambda x: x.gender)
        return sorted_list

    # Сортировка таблицы по столбцу "datetime"
    def sort_by_num(self):
        sorted_list = sorted(self.visitors, key=lambda x: datetime.strptime(x.datetime, "%d.%m.%Y %H:%M"))
        return sorted_list

    # Ввод новой записи в таблицу
    def write_date(self):
        if self.visitors:
            number = self.visitors[-1].number + 1
        else:
            number = 1
        datetime_now = datetime.now().strftime("%d.%m.%Y %H:%M")
        inout = input("Вошел/Вышел (Введите 1/0): ") == '1'
        gender = "Man" if input("Пол Мужской/Женский (1/0): ") == '1' else "Woman"

        with open('data.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow((number, datetime_now, inout, gender))
            self.visitors.append(Visitor(number, datetime_now, inout, gender))

    # Генерация и внесение новой записи в таблицу
    def generate_data(self):
        import random
        if self.visitors:
            number = self.visitors[-1].number + 1
        else:
            number = 1
        genders = ["Man", "Woman"]
        with open('data.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            date_time = datetime.now().strftime("%d.%m.%Y %H:%M")
            inout = random.choice([True, False])
            gender = random.choice(genders)
            writer.writerow((number, date_time, inout, gender))

    # Поиск директории вывод количество файлов и сами файлы
    @staticmethod
    def directory_files():
        directory = input("Введите путь к директории: ")
        if not os.path.exists(directory):
            print("Директория не существует.")
            return
        files = os.listdir(directory)
        print("Количество файлов: " + str(len(files)))
        for file in files:
            print(file)


# Основная функция
def main():
    Data.directory_files()
    data = Data()
    data.read_data()
    print("Исходная таблица: ")
    print(data.visitors)
    print("Сортировка по строковому полю(gender): ")
    print(data.sort_by_str())
    print("Сортировка по числовому полю(datetime): ")
    print(data.sort_by_num())

    choice = input("Внести/Сгенерировать запись (Введите 1/0, иначе завершить программу): ")
    if choice == '1':
        data.write_date()
    elif choice == '0':
        data.generate_data()



if __name__ == "__main__":
    main()
