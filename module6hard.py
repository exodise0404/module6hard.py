class Figure:
    sides_count = 0
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r or g or b in range(0, 255):
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not isinstance(side, int):
                return False
        return True

    def  get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        if self.sides_count == 1:
            perimetr = self.__sides[0]
        else:
            for side in self.__sides:
                perimetr += side
        return perimetr

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Triangle (Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        P = 0
        for i in self.get_sides():
            P += i
        p = P / 2
        return ((p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5


class Circle (Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        import math
        self.__radius = self.get_sides()[0] / (2 * math.pi)


    def get_square(self):
        import math
        return math.pi * self.__radius ** 2

class Cube (Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())