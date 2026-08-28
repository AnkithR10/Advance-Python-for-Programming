from datetime import datetime as d
current=d.now()
print("----Attendance Date Tracker----")
print("Current Date and Time:",current)
print("Day:",current.day)
print("Month:",current.month)
print("Year:",current.year)
print("Date:",current.date())
print("Time:",current.time())

#Formatted version
print("Date:",current.strftime("%d-%m-%Y"))
print("Time:",current.strftime("%H:%M:%S"))