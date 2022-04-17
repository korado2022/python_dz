# Реализуйте базовый класс Car:
#     ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
#         также методы: go, stop, turn(direction), которые должны сообщать, что машина
#         поехала, остановилась, повернула (куда);
#     ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#     ● добавьте в базовый класс метод show_speed, который должен показывать текущую
#         скорость автомобиля;
#     ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
#         скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
#         превышении скорости.
#     Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
#     выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула на {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превышаете допустимую скорость 60 км/ч на {self.speed - 60} км/ч')
        else:
            print(f'Текущая скорость автомобиля: {self.speed} км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превышаете допустимую скорость 40 км/ч на {self.speed - 40} км/ч')
        else:
            print(f'Текущая скорость автомобиля: {self.speed} км/ч')

class PoliceCar(Car):
   pass


town_car = TownCar(90, 'белый', 'Веста', False)
print('Название автомобиля: ', town_car.name)
print('Цвет автомобиля: ', town_car.color)
print(f'Скорость автомобиля: {town_car.speed} км/ч', )
print('Является ли автомобиль полицейской машиной: ', town_car.is_polise)
town_car.go()
town_car.show_speed()
town_car.turn('лево')
town_car.stop()

sport_car = SportCar(200, 'красный', 'Веста-спорт', False)
print('Название автомобиля: ', sport_car.name)
print('Цвет автомобиля: ', sport_car.color)
print(f'Скорость автомобиля: {sport_car.speed} км/ч', )
print('Является ли автомобиль полицейской машиной: ', sport_car.is_polise)
sport_car.go()
sport_car.show_speed()
sport_car.turn('право')
sport_car.stop()


work_car = WorkCar(60, 'синий', 'КамАЗ', False)
print('Название автомобиля: ', work_car.name)
print('Цвет автомобиля: ', work_car.color)
print(f'Скорость автомобиля: {work_car.speed} км/ч', )
print('Является ли автомобиль полицейской машиной: ', work_car.is_polise)
work_car.go()
work_car.show_speed()
work_car.turn('лево')
work_car.stop()

work_car = PoliceCar(220, 'зеленый', 'УАЗ', True)
print('Название автомобиля: ', work_car.name)
print('Цвет автомобиля: ', work_car.color)
print(f'Скорость автомобиля: {work_car.speed} км/ч', )
print('Является ли автомобиль полицейской машиной: ', work_car.is_polise)
work_car.go()
work_car.show_speed()
work_car.turn('лево')
work_car.stop()

