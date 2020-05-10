#Task3(Hard). Write a Python program to remove duplicates from a list.
mylist=[10,11,11,12,10,9,10,9,8,9,64]
print(f"Numbers before {mylist}")
num = []

for n in mylist:
    if n not in num:
        num.append(n)
print(f"Removed duplicates {num}")