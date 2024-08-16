# Lists
L1 = []
L2 = []

# Loop 
for i in range(1, 101):
    if i % 2 == 0:
        L1.append(i)
    else:
        L2.append(i)

# Print lists
print("L1 : ", L1 , sep="\n")
print("L2 : ", L2 , sep="\n")
