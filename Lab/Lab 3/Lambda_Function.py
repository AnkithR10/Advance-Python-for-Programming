#lambda Function For Positive or negative
n = int(input("Enter the Number"))
check = lambda x:"Posiitive" if x > 0 else "Negative"
print(check(n))