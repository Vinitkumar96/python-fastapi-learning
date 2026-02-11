try:
    x = int(input("enter a number"))
    y =  1/x
    print(y)
except ZeroDivisionError:
    print("no division by zero")
except ValueError:
    print("Please enter an integer")

print("All done")