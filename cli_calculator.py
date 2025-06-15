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
    
def times(a, b):
    return a ** b 

operations = {
    '+':add,
    '-':substract,
    '/':divide,
    '*':multiply,
    '**':times
}
\
print("Starting simple Python calculator")

while True:
    # Принимаем значение от пользователя и пытаемся привести к численному типу
    # Если введено не число, то приведение типа выдаст ValueError
    # Ловим исключение try-except блоком и начинаем цикл сначала
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

    if operation in operations:
        print(operations[operation](num1, num2))
    
    choice = input("\nDo you wish to continue? [y/n]\n")
    if choice.lower() in ['y', 'yes']:
        continue
    else:
        break