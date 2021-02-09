# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class MyAbstractClassClothes(ABC):

    @property
    @abstractmethod
    def amount_material(self) -> float:
        pass

    @property
    @abstractmethod
    def parameter(self) -> float:
        pass


class Coat(MyAbstractClassClothes):

    def __init__(self, name: str, size: float):
        self.name = name
        self.__size = size

    @property
    def amount_material(self) -> float:
        return (self.__size / 6.5) + 0.5

    @property
    def parameter(self) -> float:
        return self.__size


class Suit(MyAbstractClassClothes):

    def __init__(self, name: str, height: float):
        self.name = name
        self.__height = height

    @property
    def amount_material(self) -> float:
        return 2 * self.__height + 0.3

    @property
    def parameter(self) -> float:
        return self.__height

#Проверяем
if __name__ == "__main__":
    my_coat = Coat("coat", 46)
    print(f"Размер пальто: {my_coat.parameter}")
    print(f"Необходимо материалов для пальто: {my_coat.amount_material}")
    print("\n")
    my_suit = Suit("suit", 1.95)
    print(f"Костюм для роста:{my_suit.parameter}")
    print(f"Необходимо материалов для костюма:{my_suit.amount_material}")

    print(f"Всего материала необходимо:{my_coat.amount_material + my_suit.amount_material}")