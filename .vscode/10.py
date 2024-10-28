first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("choose operation (+, -, /, *) ")

if operation == '+':
    result = (first_number + second_number)
elif operation ==  '-':
    result = (first_number - second_number)
elif operation == '/':
    result = (first_number / second_number)
elif operation == '*':
    result = (first_number * second_number)

print(result)
