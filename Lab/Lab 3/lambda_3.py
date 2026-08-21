'''Lambda with Bilt in Function
map
filter
sorted

#A student has a marks store as  a list.
#The system needs to increase evry mark by 5 bonus marks,subject to maximum of 100
marks =list(map(int,input("Enter the marks:").split()))
updated_marks = list(map(lambda x:min(x+5,100),marks))

print("original Marks:",marks)
print("Updated Marks:",updated_marks)
'''
#Second method
marks =list(map(int,input("Enter the marks:").split()))
updated_marks = list(filter(lambda x:x>=80,marks))

print("original Marks:",marks)
print("Updated Marks:",updated_marks)