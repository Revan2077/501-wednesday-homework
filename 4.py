# lists
folder1 = []
folder2 = []
folder3 = []
# Get numbers
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
number4 = int(input("Enter fourth number: "))
number5 = int(input("Enter fifth number: "))

# add to folder
folder1.append(number1)
folder2.append(number2)
folder3.extend([number3, number4, number5])
folder4 = tuple(folder3)

# Print
print(folder1)
print(folder2)
print(folder4)
