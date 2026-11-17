# Student Result File Processing
valid_marks = []
try:
    with open("marks.txt", "r") as file:
        for line in file:
            try:
                marks = int(line.strip())
                if marks < 0 or marks > 100:
                    raise ValueError("Marks must be between 0 and 100.")
                valid_marks.append(marks)
            except ValueError as error:
                print("Invalid entry:",line.strip(),"-",error)
    print("\nValid Marks:", valid_marks)

except FileNotFoundError:
    print("marks.txt file does not exist.")

finally:
    print("File operation completed.")