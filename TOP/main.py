

#  Двигатель и его функции
# def start():
#     print("Запуск") 

# def stop():
#     print("Стоп")

# Engine = {
#     "start" : start,
#     "stop" : stop,
# }

# # Engine["start"]()
# # Engine["stop"]()
# def open():
#     print("Капот открыт")

# def close():
#     print("Капот закрыт")

# Bonnet = {
#     "open" : open,
#     "close" : close,
# }
# # Основа авто
# Car = {
#     "color" : "",
#     "marka" : "",
#     "Engine" : "",
#     "Bonnet" : ""
# }

# auto = Car
# auto["marka"] = "audi"
# auto["color"] = "green"
# auto["Engine"] = Engine
# print(auto)
# auto["Engine"]["start"]()

# # Основная функция
# def Car(marka,color):
#     thisMarka = marka
#     thisColor = color

#     activeList = {
#         "showMarka" : showMarka
#     }

# def showMarka(param):
#     print(param)
     
# Двигатель


# auto = Car("audi","green")

# import copy
# Mash = {
#     "color" : "",
#     "marka" : ""
# }

# # Car = copy.deepcopy(Mash)
# Car["Engine"] = Engine
# Car["Doors"] = "двери"

# myAuto = copy.deepcopy(Car)
# myAuto["color"] = "Синий"

# Ster = copy.deepcopy(Mash)

# Ster["Engine"] = Engine
# Ster["Baraban"] = "Барабан"
# mySter = copy.deepcopy(Ster)
# mySter["color"] = "Белый"

# print("Основа техники",Mash)
# print("----------")
# print("Основа техники --> В шаблон авто",Car)
# print("----------")
# print("Шаблон авто --> мой авто",myAuto)
# print("----------")
# print("Основа техники --> В шаблон стиральная машина",Ster)
# print("----------")
# print("шаблон стиральная машина --> в мою стиральную маину",mySter)

# # ------------------------------------
# import copy
# # Создание персонажа
# def attack(param):
#     return param


# Person = {
#     "name" : "Варвар",
#     "gender" : "Мужской",
#     "actions" : {
#         "attack" : attack
#     }
# }

# # Создание расы на основе объекта Person
# Human = copy.deepcopy(Person)
# Human["race"] = "Человек"
# Human["skills"] = ["Быстрый бег", "Красноречие"]

# Orc = copy.deepcopy(Person)
# Orc["race"] = "Орк"
# Orc["skills"] = ["Сила", "Быстрый бег"]

# # Создание ролей на основе race


# Warrior = copy.deepcopy(Orc) or copy.deepcopy(Human)
# Warrior["role"] = "Воин"
# Warrior["desc"] = "Воин отличается своим сочетанием мобильности, живучести, способности наносить урон и прерывать противника."
# Warrior["actions"]["attack"]("Удар")

# Archer = copy.deepcopy(Human) 
# Archer["role"] = "Лучник"
# Archer["desc"] = "Лучники способны избегать все эффекты контроля (кроме Эриолы) и получать меньше входящего урона, что позволяет им дольше жить и беспрепятственно вносить ДПС"
# Archer["actions"]["attack"]("стрельба")

# Shaman = copy.deepcopy(Orc)
# Shaman["role"] = "Шаман"
# Shaman["desc"] = "Шаманы — наставники в духовных практиках, идущих не от богов, а от самих природных стихий. "
# Shaman["attaka"] = "Закленание"
# Shaman["actions"]["attack"] = attack(Shaman["attaka"])

# # print("----------")
# # print(Person)
# # print("----------")
# # print(Human)
# # print("----------")
# # print(Orc)
# # print("----------")
# # print(Archer)
# # print("----------")
# # print(Warrior)
# # print("----------")
# # print(Shaman)
# # print("----------")

# myPerson = copy.deepcopy(Shaman)
# print(myPerson)
# print(myPerson["actions"]["attack"])

# # Frog = {
# #     "gender": "Мужской",
# #     "name" : "СуперЛяг",
# #     "color" : "Синий"
# # }


# Archer = copy.deepcopy(Frog) 
# Archer["role"] = "Лучник"
# Archer["desc"] = "Лучники способны избегать все эффекты контроля (кроме Эриолы) и получать меньше входящего урона, что позволяет им дольше жить и беспрепятственно вносить ДПС"
# Archer["skills"] = "Двойное сальто"


class Car:
    def __init__(self, color, marka, engine): # создание переменных дня класса (объекта)
        self.color = color
        self.marka = marka
        self.engine = engine
    # методы - действия с определенным классом
    def showColor(self):
        print(self.color)

    def showMarka(self):
        print(self.marka)

    def showHP(self):
        print("Наследуется")

class Engine:
    def __init__(self, HP, volume):
        self.HP = HP
        self.volume = volume

    def start(self):
        print("Запуск")

    def stop(self):
        print("Стоп")

    


myEngine = Engine(120, 2)
twoEngine = Engine(280, 2.2) 
myAuto = Car("green","audi",myEngine)

print(myAuto.engine.volume)


# Наследование

class SportCar(Car):
    def __init__(self, color, marka, engine, abs):
        # self.color = color
        # self.marka = marka
        # self.engine = engine
        self.abs = abs
        super().__init__(color, marka, engine)


lambarginiEngine = Engine(900, 6)
twoAuto = SportCar("blue","lamborgini", lambarginiEngine, True)

twoAuto.showHP()


class Animal:
    def __init__(self, name , sound):
        self.name = name
        self.sound = sound
    
    def activeSound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Мяу")

    def purr(self):
        print("Мурлыкает")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Гав")

    def digHole(self):
        print("Копает яму")

myCat = Cat("Вася")
myCat.activeSound()