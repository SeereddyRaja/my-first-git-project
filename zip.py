str1 = "ABC"
str2 = "123"
combined = zip(str1, str2)
#print(list(combined))
for item in combined:
    print(item)
number = 1
for row in range(2):
    for col in range(5):
        print(number, end = " ")
        number+=1
    print()
for i in range(6):
    for j in range(i):
        print("*", end = " ")
    print()
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()