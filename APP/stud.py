class InvalidMarksError(Exception):
    pass

while True:
    try:
        name = input("\nEnter student name: ")

        # Assertion to ensure name is not empty
        assert name.strip() != "", "Student name cannot be empty."

        marks = int(input("Enter marks: "))

        if marks < 0 or marks > 100:        # Custom exception
            raise InvalidMarksError(
                "Marks must be between 0 and 100."
            )

        # Save valid record to file
        with open("student_records.txt", "a") as file:
            file.write(f"{name}, {marks}\n")
        print("Student record saved successfully.")

    except ValueError:
        print("Invalid marks. Please enter a numeric value.")

    except AssertionError as error:
        print("Error:", error)

    except InvalidMarksError as error:
        print("Error:", error)

    finally:
        print("Student record processing completed.")

    choice = input("\nDo you want to add another student? (yes/no): ").lower()

    if choice != "yes":
        print("Program ended.")
        break