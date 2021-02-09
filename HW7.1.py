# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from copy import deepcopy


class Matrix:

    def __init__(self, data: list):
        self.__data = deepcopy(data)
        self.__row_numbers = len(self.__data)  # высота матрицы (n)
        self.__column_numbers = len(self.__data[0])  # длина матрицы (m)
        if not isinstance(self.__data, list):
            raise TypeError("Ошибка. Требуется тип данных list")
        for ind, column in enumerate(self.__data, 1):
            if not len(column) == self.__column_numbers:
                raise ValueError(f"Ошибка ввода данных в строке {ind}")
            if not isinstance(column, list):
                raise TypeError(f"Ошибка. Неверный тип данных в строке {ind}. Необходим тип данных list")

    def __iter__(self):
        return self.__data.__iter__()

    def __getitem__(self, item):
        return tuple(self.__data[item])

    def __str__(self):
        """Возвращает строку, в которой каждый элемент вложенного списка разделен пробелом.
        Каждый элемент выводится с новой строки
        """
        result = ""
        for line in self.__data:
            result += " ".join([f'{itm}' for itm in line]) + '\n'
        return result

    def __add__(self, other):
        """
        Возвращает новую матрицу при суммировании двух матриц
        """
        if not isinstance(other.__data, list):
            raise TypeError("Неверный тип данных. Необходим тип данных list")
        if self.__row_numbers == other.__row_numbers and self.__column_numbers == other.__column_numbers:
            # 1: объединение элементов матриц по индексам в кортежи (каждый состоит из 2 списков)
            temp_1 = list(zip(self, other))
            # 2: в каждом из сформированных кортежей объединяем элементы 2 списков по индексам в новые кортежи
            temp_2 = map(lambda x: list(zip(*x)), temp_1)
            # 3: и, наконец, складываем элементы новых кортежей
            temp_3 = []
            for elm in temp_2:
                elm = list(map(sum, elm))
                temp_3.append(elm)
            return Matrix(temp_3)
        else:
            raise ValueError("Матрицы имеют разный размер!")


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
matrix3 = matrix1 + matrix2
matrix4 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix5 = Matrix([[1, 2], [3, 4], [5, 6]])
# закоменнтированные строки - проверка на ошибки при вводе данных
# print(matrix4+matrix1)
# matrix2 = Matrix([[11, 12, 13], (14, 15, 16), [17, 18, 19]])
# matrix5 = Matrix([[1, 2], [3], [5, 6]])
# matrix4 = Matrix(([1, 2], [3, 4], [5, 6]))
print(f"Первая матрица: \n{matrix1}")
print(f"Вторая матрица: \n{matrix2}")
print(f"Результат: \n{matrix3}")