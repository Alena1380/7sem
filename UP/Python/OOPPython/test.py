import datetime as DT


def str_to_date(self_date, other_date):
    dt1 = self_date.split(".")
    dt2 = other_date.split(".")
    self_bdate = DT.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
    other_bdate = DT.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_bdate, other_bdate


class Students:
    def __init__(self, number, fio, bdate, oklad, on_leave=False):
        self.number = number
        self.fio = fio
        self.bdate = bdate
        self.salary = oklad
        self.on_leave = on_leave

    # Изменяем оклад
    def increase_salary(self, summa):
        self.salary += summa

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"Студент {self.number} {self.fio}, {self.bdate}," \
               f" стипендия: {self.salary}, на больничном: {'да' if self.on_leave else 'нет'}"

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate

    def __eq__(self, other):  # ==
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False


class Department:
    def __init__(self, title, chief=None, employees=None):
        self.title = title
        if employees is None:
            employees = list()
        self.employees = employees
        self.chief = chief

    # Добавляем сотрудника в отдел
    def append(self, emp):
        self.employees.append(emp)

    # Перехват функции print, когда она преобразует свое значение в строку
    # Возврат информации об отделе
    def __str__(self):
        return f"Группа 195: {self.title}, Куратор: Гришакова Татьяна Николаевна, Количество студентов: {len(self.employees)} "

    # Вывод участников группы
    def print_employees(self):
        for emp in self.employees:
            print(emp)

    # Вывод сотрудников отдела в отпуске/не в отпуске
    def print_employees_on_leave(self, status=True):
        for emp in self.employees:
            if emp.on_leave == status:
                print(emp.number, emp.fio)


emp_1 = Students(1, 'Меринов Дмитрий Александрович', '27.11.2002', 1590)
emp_2 = Students(2, 'Комаров Данила Алексеевич', '16.02.2003', 530)
emp_3 = Students(3, 'Алибеков Мустафа Магомедэминович', '02.04.2003', 1440)
emp_4 = Students(4, 'Гашев Вячеслав Иванович', '01.01.2005', 1590)
emp_5 = Students(5, 'Лидовской Иван Николаевич', '21.11.2002', 530)
emp_6 = Students(6, 'Демченков Вадим Сергеевич', '11.08.2004', 1440)

# Сравним по датам рождения
print(emp_1 < emp_2)
print(emp_1 > emp_2)
print(emp_1 == emp_2)
print(emp_1 <= emp_2)
print(emp_1 >= emp_2)

depart_1 = Department('архив', emp_1)
depart_1.append(emp_1)
depart_1.append(emp_2)
print(depart_1)
depart_1.print_employees()
emp_1.increase_salary(267)

print(emp_3)
print(emp_4)
print(emp_5)
print(emp_6)

depart_1.print_employees_on_leave()
