#addition
def add(x, y):
    return x + y
#substraction
def subtract(x, y):
    return x - y
#multiplication
def multiply(x, y):
    return x * y
#division
def divide(x, y):
    return x / y
# modulus
def mod(x,y):
    return x % y
# exponent
def exp(x,y):
    return x**y
# floor division
def floor(x,y):
    return x//y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.modulus")
print("6.exponent")
print("7.floor division")

while True:
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ('1','2','3','4','5','6','7'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))

        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1,num2))

        elif choice =='6':
            print(num1, "**",num2, "=", exp(num1,num2))

        elif choice =='7':
            print(num1, "//",num2, "=", floor(num1,num2))
        next_calculation = input("another calculation? yes/no")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
