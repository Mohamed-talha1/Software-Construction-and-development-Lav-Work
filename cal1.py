# main_calculator.py
import cal_mod as calc

def main():
    print("Simple Calculator using Modules")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", calc.add(num1, num2))
    elif choice == '2':
        print("Result:", calc.subtract(num1, num2))
    elif choice == '3':
        print("Result:", calc.multiply(num1, num2))
    elif choice == '4':
        print("Result:", calc.divide(num1, num2))
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
