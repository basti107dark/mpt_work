
#Функция, позволяющая зациклить выполнение данной программы
def RepeatWork():
    re = int(input("Продолжить работу?\n"
    "1- Продолжить работу\n"
    "0- Завершить работу\n"
    ))
    if re == 1:
        main()
    elif re == 0:
        print("завершение работы...")
    else:
        print("Ошибка ввода!")
        RepeatWork()

#Операция сложения
def MathSumm(firstNumer, secondNumber):
    #Выполнение сложения и вывод результата на консоль
    print(firstNumer + secondNumber)
    RepeatWork()

#Операция вычитания
def Difference(firstNumeb, secondNumber):
    # Выполнение вычитания и вывод результата на консоль
    print(firstNumeb - secondNumber)
    RepeatWork()

#Операция умножения
def Multiply(firstNumber, secondNumber):
    # Выполнение умножения и вывод результата на консоль
    print(firstNumber * secondNumber)
    RepeatWork()

#Операция деления
def Divide(firstNumber, secondNumber):
    #Проверка, равен ли делитель нулю
    if secondNumber == 0:
        print("Ошибка! Невозможно разделить число на нуль!")
        RepeatWork()
    else:
    #Вывод результата на консоль
        print(firstNumber / secondNumber)
        RepeatWork()

#Операция возвдение в степень
def Exponentiation(number, indicator):
    print(number ** indicator)
    RepeatWork()

def main():
    selectedOperation = int(input("Добро пожаловать! Выберите необходимую операцию:\n"
    "1- Сложение\n"
    "2- Вычитание\n"
    "3- Умножение\n"
    "4- Деление\n"
    "5- Возведение в степень\n"
))

    #Проверка коректности выбраного числа пользователем
    if selectedOperation < 1 or selectedOperation > 5 :
        print("Ошибка! Вы выбрали не существующую операцию!")

    #Ввод пользователем первого числа
    firstNumber = int(input('Введите первое число: '))

    # Ввод пользователем второго числа
    secondNumber = int(input('Введите второе число: '))

    #Следующий блок кода выполняет математическую операцию,
    #зависищую от выбранного пользователем числа
    if selectedOperation == 1:
        MathSumm(firstNumber, secondNumber)
    elif selectedOperation == 2:
        Difference(firstNumber, secondNumber)
    elif selectedOperation == 3:
        Multiply(firstNumber, secondNumber)
    elif selectedOperation == 4:
        Divide(firstNumber, secondNumber)
    elif selectedOperation == 5:
        Exponentiation(firstNumber, secondNumber)

#Выполнение программы
if __name__ == '__main__':
    main()
