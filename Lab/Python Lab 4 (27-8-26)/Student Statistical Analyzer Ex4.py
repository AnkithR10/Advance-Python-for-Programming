import statistics as s
marks=list(map(int,input("Enter marks seperated by spaces:").split()))
print("\n----Statistical Analysis---")
print("Marks:",marks)
print(f"Mean:{s.mean(marks)}")
print(f"Median:{s.median(marks)}")
print(f"Mode:{s.mode(marks)}")
print(f"Standard Deviation:{s.stdev(marks)}")