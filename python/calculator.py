import acelib

# Aliases for operations
adds = ['1', '+', "add", "addition"]
subs = ['2', '-', "sub", "subtract", "subtraction"]
muls = ['3', 'x', '*', "mul", "multiplication", "multiply"]
divs = ['4', '/', "div", "division", "divide"]

# Functions for the Calculator
def get_operator():
    while True:
        op = input("Enter your choice: ").lower().strip()
        if op in adds:
            return '+'
        elif op in subs:
            return '-'
        elif op in muls:
            return 'x'
        elif op in divs:
            return '/'
        else:
            print("Invalid operator! Please try again.")
            continue

def calculate(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == 'x':
        return n1 * n2
    elif op == '/':
        try:
            return n1 / n2
        except ZeroDivisionError:
            print("You are trying to divide by zero!")
            return None


# Main program   
def main():
    print("------------------------------------------------------------")
    print("                 Welcome to Ze Kalkulator!                  ")
    print("------------------------------------------------------------")
    while True:
        print('''\n------------------------------------------------------------
Choose the operation you wish to perform:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division''')

        operator = get_operator()

        print()

        number1 = acelib.get_float("Enter number 1: ")
        number2 = acelib.get_float("Enter number 2: ")

        print()

        result = calculate(operator, number1, number2)

        if result is None:
            print("Let's restart!")
            continue

        print(f"{number1} {operator} {number2} = {result}\n")


        again = input("Do you want to do another calculation(y/n): ").lower()
        print("------------------------------------------------------------")
        if again not in ['y', "yes"]:
            break

if __name__ == "__main__":
    main()
