months=["january","february","march","april","may"]
expenses=[2200,2350,2600,2130,2190]
# how many dollar you spent extra campare to jan
expen=expenses[1]-expenses[0]
print(expen)

# total expense in first three month
total_expen=expenses[0]+expenses[1]+expenses[2]
print(total_expen)

# spent exactly 2000 in any month
print("exactly 20000 in expenses",2000 in expenses)

# june month finished and epenses is 980 dollar
# add june expense to expense list
expenses.append(1980)
print(expenses)

# returned an item that you bought in april
expenses[3]=expenses[3]-200

print(expenses[3])
print(expenses)