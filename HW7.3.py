# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:

    def __init__(self, cells_amount: int):
        self.__cells_amount = cells_amount

    @property
    def get_cells(self) -> int:
        return self.__cells_amount

    def __add__(self, other):
        """
        Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
         равняться сумме ячеек исходных двух клеток.
        """
        return Cell(self.__cells_amount + other.__cells_amount)

    def __sub__(self, other):
        """
        Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
        количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
        """
        cell_new = self.__cells_amount - other.__cells_amount
        if cell_new > 0:
            return Cell(cell_new)
        else:
            raise ValueError("разность количества ячеек двух клеток меньше нуля")

    def __mul__(self, other):
        """
        Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
        как произведение количества ячеек этих двух клеток.
        """
        return Cell(self.__cells_amount * other.__cells_amount)

    def __floordiv__(self, other):
        """Возвращает общая клетка из двух, где количество ячеек клетки
        результат от целочисленного деления"""
        return Cell(self.__cells_amount // other.__cells_amount)

    def __truediv__(self, other):
        """Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется
        как целочисленное деление количества ячеек этих двух клеток. Осуществляется
        округление значения до целого числа.
        """
        return self.__floordiv__(other)

    def make_order(self, cell_in_row: int):
        """
        Организация ячеек по рядам. Возвращает строку вида *****\n*****\n*****...,
        где количество ячеек между \n равно переданному аргументу. Если ячеек на
        формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
        Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
        Тогда вернется строка: *****\n*****\n**. Если равняется 15, количество ячеек в ряду — 5.
        Тогда вернется строка: *****\n*****\n*****.
        """
        if not isinstance(cell_in_row, int):
            raise TypeError('Неверный тип данных. Необходимо ввести целое число (int)')
        str_amount = self.get_cells // cell_in_row
        cell_in_last_row = self.get_cells % cell_in_row
        cells_str = '\n'.join(("*" * cell_in_row for _ in range(str_amount))) + "\n" + cell_in_last_row * "*"
        return cells_str


if __name__ == '__main__':
    cell1 = Cell(5)
    cell2 = Cell(17)
    cell3 = Cell(4)
    cell4 = Cell(12)
    cell5 = Cell(22)
    sum_cells = cell1 + cell3
    sub_cells1 = cell2 - cell1
    mul_cells = cell1 * cell3
    div_cells = cell4 / cell3
    my_str1 = sum_cells.make_order(5)
    my_str2 = cell5.make_order(4)
    print(my_str1)
    print("\n")
    print(my_str2)












