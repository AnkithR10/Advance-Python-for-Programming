#Nested loop - Matrix
m=[[10,20,30],[44,45,46],[17,28,59]]

for row in m:
    for value in row:
        print(value,end=" ")
    print()
print(type(m))