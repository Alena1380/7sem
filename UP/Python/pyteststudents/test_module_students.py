from module_employee import Student, Department
import pytest


# Проверка на отрицательную стипендию
def test_wrong_stip():
    with pytest.raises(ValueError):
        employee_1 = Student(1, "Меринов Д.А.", "27.11.2002", -100)




# Номер студента должен быть числовой
def test_wrong_type_student_num():
    with pytest.raises(TypeError):
        employee_1 = Student("1", "Меринов Д.А.", "27.11.2002", 10000)


# Проверяем увеличение стипендии
def test_increase_stip():
    employee_1 = Student(1, "Меринов Д.А.", "11.11.2002", 10000)
    employee_1.increase_salary(5000)
    assert employee_1.salary == 15000


# Сравниваем двух студентов по Дню Рождения
def test_employees_lt():
    employee_1 = Student(1, "Меринов Д.А.", "11.11.2002", 10000)
    employee_2 = Student(2, "Меринов Д.А.", "11.11.2002", 10000)
    assert (employee_1 < employee_2) == False



# Проверка при добавлении сотрудника в отдел. (неверный тип)
def test_wrong_type_Department():
    with pytest.raises(TypeError):
        # employee_1 = Employee("1", "Семенов М.А.", "12.12.2000", 10000)
        dep_1 = Department("Закупок", "Смирнов И.В.")
        dep_1.append("Петров А.Н.")


# Проверка при добавлении сотрудника в отдел (добавтли правильно)
def test_append_Department():
    with pytest.raises(TypeError):
        employee_1 = Student("1", "Семенов М.А.", "12.12.2000", 10000)
        dep_1 = Department("Закупок", "Смирнов И.В.")
        count_before = len(dep_1.employees)
        dep_1.append(employee_1)
        assert count_before == len(dep_1.employees) - 1