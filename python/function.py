def input_number():
    return int(input("enter a number"))



# def print_sum(num1,num2):
#     sum = num1 + num2
#     print("The sum is: ",str(sum))

# print_sum(2,3)


def multiply_values(list):
    multiply_values = []

    for item in list:
        multiply_values.append(item*2)

    return multiply_values

print(multiply_values([1,2,3]))