number = int(input("enter a number:"))
factorial = 1
if number < 0:
    print("number should not be -ve")
elif number == 0:
    print("factorial = 1")
else:
    for i in range(1,number+1):
        factorial = factorial * i
print(factorial)