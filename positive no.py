# Write a Python program to print all positive numbers in a range.
list_1 = [12,-7,5,64,-14]
list_2 = [12,14,-95,3]

a = [num for num  in list_1 if num >= 0]
b = [num for num in list_2 if num >= 0]

print ("Positive numbers in the list:",a)
print("Positive numbers in the list",b)