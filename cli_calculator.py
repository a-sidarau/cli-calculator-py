import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a or b == 0:
        print("Cannot divide by 0!")
    else:
        return a / b
    
def power(a, b):
    return a ** b 

def modulus(a, b):
    if a or b == 0:
        print("Cannot divide by 0!")
    return a % b

# Управляющая функция калькулятор. Принимает номер операции и вызывает её из словаря operations
def controls(num1, num2):
    print("-------------------")
    print("Список операций:")
    print("-------------------")
    print("1 +\t" + "2 -\t" + "3 /")
    print("4 *\t" + "5 a^b\t" + "6 %")
    # print("7 M+\t" + "8 MR\t" + "9 MC")
    print("-------------------")
    print("0. Выход")
    while True:
        user_input = input("\nВведите номер операции: ")
        if user_input == '0':
            sys.exit()
        elif user_input in operations:
            return operations[user_input](num1, num2)
        else:
            print("\nОшибка ввода!")


def get_input():
    # Принимаем значение от пользователя и пытаемся привести к численному типу
    # Если введено не число, то приведение типа выдаст ValueError
    # Ловим исключение try-except блоком и начинаем цикл сначала
    while True:
        try:
            num1 = float(input("Введите первое число: "))
        except ValueError:
            print("Ошибка! Это не число.")
            continue

        try:
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка! Это не число.")
            continue

        return num1, num2

operations = {
    '1':add,
    '2':subtract,
    '3':divide,
    '4':multiply,
    '5':power,
    '6':modulus
}


def main():
    while True:
        # вначале получаем ввод чисел
        num1, num2 = get_input()

        # затем предоставляем выбор операции
        print(controls(num1, num2))
    


if __name__ == "__main__":
    main()