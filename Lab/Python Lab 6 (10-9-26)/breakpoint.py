import random
heads=0
for i in range(1,1001):
    if random.randint(0,1)==1:
        heads+=1
        breakpoint()

    if i==500:
        print("Halfway done!")
        breakpoint()
print('Heads came up '+str(heads) + ' times.')

#OUTPUT:
# PS C:\Python Lab> & "C:\Program Files\Python314\python.exe" "c:/Python Lab/Python Lab 6 (10-9-26)/breakpoint.py"
# > c:\python lab\python lab 6 (10-9-26)\breakpoint.py(6)<module>()
# -> breakpoint()
# (Pdb) n
# > c:\python lab\python lab 6 (10-9-26)\breakpoint.py(8)<module>()
# -> if i==500:
# (Pdb) c
# > c:\python lab\python lab 6 (10-9-26)\breakpoint.py(6)<module>()
# -> breakpoint()
# (Pdb) w
# > c:\python lab\python lab 6 (10-9-26)\breakpoint.py(6)<module>()
# -> breakpoint()
# (Pdb) s
# > c:\python lab\python lab 6 (10-9-26)\breakpoint.py(8)<module>()
# -> if i==500:
# (Pdb) l
#   3     for i in range(1,1001):
#   4         if random.randint(0,1)==1:
#   5             heads+=1
#   6             breakpoint()
#   7  
#   8  ->     if i==500:
#   9             print("Halfway done!")
#  10             breakpoint()
#  11     print('Heads came up '+str(heads) + ' times.')
# [EOF]
# (Pdb) q
# Quitting pdb will kill the process. Quit anyway? [y/n] y