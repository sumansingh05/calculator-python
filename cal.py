def switch(operator,a,b):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a//b
    elif operator == '%':
        return a%b
    else:
        return "Invalid operator"
    
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
operator = input("enter operator:")[0]

result = switch(operator,a,b)
print("Result is",result)




