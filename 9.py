# get start and end
start = int(input("Enter the start : "))
end = int(input("Enter the end: "))

for i in range(start, end +1):
    if i % 15 == 0 :
      print(i, end=" ")
