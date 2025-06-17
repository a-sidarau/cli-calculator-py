def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a or b == 0:
        print("Cannot divide by 0!")
    else:
        return a / b
    
def exponentiate(a, b):
    return a ** b 

def modulus(a, b):
    if a or b == 0:
        print("Cannot divide by 0!")
    return a % b

operations = {
    '+':add,
    '-':substract,
    '/':divide,
    '*':multiply,
    '**':exponentiate,
    '%':modulus
}

def controls():
    print("\n-------------------")
    print("Simple Terminal Calculator on Python")
    print("\n-------------------")
    print("Select operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Divide")
    print("4. Multiply")
    print("5. a²")
    print("6. Modulus %")
    print("9. Exit")
    print("\n-------------------")


def get_input():
    # Принимаем значение от пользователя и пытаемся привести к численному типу
    # Если введено не число, то приведение типа выдаст ValueError
    # Ловим исключение try-except блоком и начинаем цикл сначала
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
        except ValueError:
            print("This is not a number. Please enter a valid one\n")
            continue

        # Проверяем, что введённая операция (символ) есть в словаре
        operation = input("\nEnter operation (+, -, /, *, **): ")
        if operation not in operations:
            print("\nInvalid operation type! Enter one of the valid ones: +, -, /, *, **")
            continue

        try:
            num2 = float(input("\nEnter second number: "))
        except ValueError:
            print("This is not a number. Please enter a valid one\n")
            continue

def main():
    print("Starting simple Python calculator")

    while True:
        if operation in operations:
            print(f"{num1} {operation} {num2} = {operations[operation](num1, num2)}")


if __name__ == "__main__":
    main()