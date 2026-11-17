# An MCA department wants to store student information such as:
# Roll Number, Name, Course,  Marks

# Writing stude
# nt records to a file
with open("student_records.txt", "w") as file:
    n = int(input("Enter number of students: "))
    for i in range(n):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")

        file.write(f"{roll},{name},{course},{marks}\n")
print("Student records saved.")

# Reading the student records from the file
print("\nStudent Records:")
with open("student_records.txt", "r") as file:
    for line in file:
        roll, name, course, marks = line.strip().split(",")
        print("\nRoll Number:", roll)
        print("Name:", name)
        print("Course:", course)
        print("Marks:", marks)

# Search a Student in a File
roll_search = input("Enter Roll Number to search: ")
with open("student_records.txt", "r") as file:
    for line in file:
        roll, name, course, marks = line.strip().split(",")
        if roll == roll_search:
            print("\nStudent Found")
            print("Roll Number:", roll)
            print("Name:", name)
            print("Course:", course)
            print("Marks:", marks)
            break
    else:
        print("Student not found.")

# Copy One File to Another
with open("student_records.txt", "r") as source:
    content = source.read()

with open("student_backup.txt", "w") as destination:
    destination.write(content)

print("Backup created successfully.")

# Delete a File
# import os
# os.remove("student_records.txt")
# print("File deleted successfully.")

# Delete a File
# import os
# if os.path.exists("student_records.txt"):
#   os.remove("student_records.txt")
# else:
#   print("The file does not exist")

# Delete a Folder
# import os
# os.rmdir("myfolder")
# print("Folder deleted successfully.")