choice=int(input("Введите номер задачи: "))
if choice==1:
    a=int(input("Введите первое число: "))
    b=int(input("Введите второе число: "))
    if a>b:
        print(a,"больше")
    elif a<b:
        print(b,"больше")
    else:
        print("Числа равны")
elif choice==2:
    paswrd=input("Введите пароль: ")
    if paswrd=="1234":
         print("Вход выполнен")
    else:
        print("Доступ запрещен")
elif choice==3:
    age=int(input("Введите ваш возраст: "))
    if age<7:
        print("Дошкольник")
    elif age<18:
        print("Несоврешеннолетний")
    elif age<65:
        print("Взрослый")
    else:
        print("Пожилой человек")


