# Test case

def is_even(number):
    return number % 2 == 0

test_numbers = [0, 4, 7, 2, 0.67, -24, -44]
for number in test_numbers:
    if number == 0:
        print("'0' is neither even nor odd number!")
        continue
    result = is_even(number)
    if result:
        print(f"{number} is an even number!")
    else:
        print(f"{number} is not an even number!")