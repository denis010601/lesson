
# # start = int(input("Введите начальное значение: "))
# # end = int(input("введите конечное значение: "))
# for i in range(0, 29):
#     if i % 2 != 0:
#         print(i)

# for a in range(0,3):
#     print(a)

# x = int(input("Ведите число на проверку простого число"))
# for i in range(2,x+1):
#     print(f"делим число {x} на {i}")
#     print(f"Остаток {x % i}")
#     if x % i == 0 and x != i:
#         print("Число сложное")
#         break
#     elif i == x:
#         print("Число простое")


# for x in range(0,100):
#     if x % 2 == 0 and x % 7 == 0:
#         print(x)

# x = int(input("Введите число: "))
# for i in range(2,10):
#     print(f"{x} * {i} = {x * i}")
# sum = 0
# for i in range(5,8):
#     sum = sum + i
#     print(sum)

# i = 0
# b = 10
# print("первый цикл")
# while True:
#     print(i)
#     i = i + 1
#     if i > 10:
#         break
# print("второй цикл")

# x = True
# while x == True:
#     print(i)
#     i = i + 1
#     if i > 15:
#         x = False


# myName = "denis"
# print(len(myName))
# i = 0
# while i < len(myName):
#     print(i)
#     i+=1


# for i in range(10):
#     print(i)

# x = 5 
# while x > 0:
#     print(x)
#     x = x - 1

# import time
# for h in range(0,24): # h = 0
#     for m in range(0,60): # m = 1
#         for s in range(0,60): # s = 1
#             print(f"ч:{h} м:{m} с:{s}")
#             time.sleep(1/10)
# h = 0
# while h < 24:
#     m = 0
#     while m < 60:
#         s = 0
#         while s < 60:
#             print(f"ч:{h} м:{m} с:{s}")
#             s+=1
#         m+=1
#     h+=1

# dd = int(input("d"))
# mm = int(input("m"))
# yy = int(input("d"))
# if mm == 4 or mm == 6 or mm == 9 or mm == 11:
#     if dd >= 30:
#         mm+=1
#         dd=1

#     elif dd < 30:
#         dd+=1
# elif mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm== 10:
#     if dd >= 31:
#         mm+=1
#         dd=1
#     elif dd < 31:
#         dd+=1
# elif mm == 12:
#     if dd >= 31:
#         mm=1
#         dd=1
#         yy+=1
#     elif dd < 31:
#         dd+=1
# elif mm == 2:
#     if yy % 4 == 0:
#         if dd >= 29:
#             mm+=1
#             dd=1
#         elif dd < 29:
#             dd+=1
#     else:
#         if dd >= 28:
#             mm+=1
#             dd=1
#         elif dd < 28:
#             dd+=1
# print(dd,mm,yy)


# ----------------------------------------------------
# Использование циклов внутри циклов, возрат значений , + условия
print("Регистрация персонажа")
reg = 0
while reg == 0:
    reg_gender = 0
    while reg_gender == 0:
        gender = input("Выберете пол персонажа\n1-муж\n2-жен\n: ")
        if gender == "1":
            gender = "Мужской"
            reg_gender=1
        elif gender == "2":
            gender = "Женский"
            reg_gender=1
        else:
            print("Ошибка: Выберете из перечисленного")
        if reg_gender == 1:
            reg_race = 0
            while reg_race == 0:
                race = input("0<-назад Выберете рассу пресонажа\n1-Человек\n2-Эльф\n: ")
                if race == "1":
                    race = "Человек"
                    reg_race = 1
                elif race == "2":
                    race = "Эльф"
                    reg_race = 1
                elif race == "0":
                    reg_gender = 0
                    break
                else:
                    print("Ошибка: Выберете из перечисленного")
                if reg_race == 1:
                    reg_role = 0
                    if race == "Человек":
                        while reg_role == 0:
                            role = input("0<-назад Выберете рассу пресонажа\n1-Воин\n2-Лучник\n: ")
                            if role == "1":
                                reg_role == 1
                    elif race == "Эльф":
                        pass
                    
    reg+=1