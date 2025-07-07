import sys


# Сложение
def add(a: float, b: float) -> float:
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


# Вычитание
def subtract(a: float, b: float) -> float:
    result = a - b
    print(f"{a} - {b} = {result}")
    return result


# Умножение
def multiply(a: float, b: float) -> float:
    result = a * b
    print(f"{a} * {b} = {result}")
    return result


# Деление
def divide(a: float, b: float) -> float:
# zero-division check
    if b == 0:
        print("Нельзя делить на 0!")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result


# Возведение в степень
def power(a: float, b: float) -> float:
    result = a ** b
    print(f"{a} ** {b} = {result}")
    return result


# Остаток от деления
def modulus(a: float, b: float) -> float:
    if b == 0.0:
        print("Нельзя делить на 0!")
    else:
        result = a % b
        print(f"{a} % {b} = {result}")
        return result

# Список операций хранится в множестве для проверки валидности ввода номера операции
operations = {'1', '2', '3', '4', '5', '6', 'R', 'M', 'N', 'P', 'C', '0'}

# Обработка ввода
def get_operands(calc_memory: float) -> float:
    print("\nВВОД ОПЕРАНДОВ")
    print("-------------------")
    print(f"Число в памяти: ", calc_memory)
    print("-------------------")
    
    # Принимаем значение от пользователя и пытаемся привести к численному типу
    # Если введено M, то присваиваем операнду значение из памяти (calc_memory)
    # Если введено не M и не число, то приведение типа выдаст ValueError
    # Ловим исключение try-except блоком и начинаем цикл сначала
    while True:
        num1 = input("Введите первое число (M для вызова из памяти): ")
        if num1.upper() == 'M':
            num1 = calc_memory
        else:
            try:
                num1 = float(num1)
            except Exception:
                print("Ошибка! Введите число или ключ M.")
                continue

        num2 = input("Введите второе число (M для вызова из памяти): ")
        if num2.upper() == 'M':
            num2 = calc_memory
        else:
            try:
                num2 = float(num2)
            except Exception:
                print("Ошибка! Введите число или ключ M.")
                continue

        return num1, num2


def main():
    # память калькулятора: общая и последнее вычисление
    calc_memory = 0.0
    last_result = 0.0
    
    # Получаем ввод чисел
    num1, num2 = get_operands(calc_memory)
        
    while True:
        # Выводим список операций
        print("\nПАМЯТЬ:")
        print("-------------------")
        print(f"Введённые значения:")
        print(f"1) {num1}")
        print(f"2) {num2}")
        print("-------------------")
        print(f"Число в памяти: ", calc_memory)
        print(f"Последнее значение: ", last_result)
        print("-------------------")
        print("P. Добавить последнее значение в память")
        print("N. Вычесть последнее значение из памяти")
        print("C. Очистить память")
        print("\nОПЕРАЦИИ:")
        print("-------------------")
        print("1. +\t" + "2. -\t" + "3. /\t")
        print("4. *\t" + "5. a**b\t" + "6. %\t")
        print("-------------------")
        print("R. Ввести числа заново")
        print("0. Выход")

        operation_number = input("\nВведите ключ(номер) операции: ").upper()

        # Проверяем наличие операций в словаре
        if operation_number not in operations:
            print("Операция не найдена в списке!")
            continue

        match operation_number:
            case "1":
                last_result = add(num1, num2)
            case "2":
                last_result = subtract(num1, num2)
            case "3":
                last_result = divide(num1, num2)
            case "4":
                last_result = multiply(num1, num2)
            case "5":
                last_result = power(num1, num2)
            case "6":
                last_result = modulus(num1, num2)
            case "R":
                num1, num2 = get_operands(calc_memory)
                # Если ввели R, то возвращаемся повторно вводим операнды
            case "P":
                # добавляем последнее вычисление в память
                calc_memory += last_result
            case "N":
                # уменьшаем память на величину последнего вычисления
                calc_memory -= last_result
            case "C":
                # очищаем память
                calc_memory = 0.0
            case "0":
                print("Выход из программы. До свидания!")
                sys.exit()


if __name__ == "__main__":
    main()