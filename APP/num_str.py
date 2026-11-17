import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

try:
    position = int(input("Enter insertion position: "))

    element = input("Enter numerical element to insert: ")

    # Check whether the input contains only digits
    if not element.isdigit():
        raise ValueError(
            "Only numerical elements can be inserted into the array."
        )

    # Convert valid input to integer
    element = int(element)

    # Check insertion position
    if position < 0 or position > len(arr):
        raise IndexError("Invalid insertion position.")

    # Insert the element
    arr = np.insert(arr, position, element)

    print("Updated Array:", arr)

except ValueError as error:
    print("Input Error:", error)

except IndexError as error:
    print("Position Error:", error)

finally:
    print("Insertion process completed.")