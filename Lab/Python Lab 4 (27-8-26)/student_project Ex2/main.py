from student_result import calculate_total
from student_result import calculate_grade
from student_result import calculate_percent

n=int(input("Enter number of subjects:"))
marks=[]
for i in range(n):
    mark=float(input(f"Enter marks for Subject{i+1}:"))
    marks.append(mark)

total=calculate_total(marks)
percent=calculate_percent(marks)
grade=calculate_grade(percent)
print("\n----Student Result----")
print("Marks:",marks)
print("Total:",total)
print("Percentage:",round(percent,2))
print("Grade:",grade)