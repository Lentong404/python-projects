print("Welcome to the tip calculator!")
# A floating integer because money can be any kind of __.__
bill = float(input("What was the total bill? $"))
# Changing the string input to a whole number to be manipulated in math
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
#Changing the string input to a whole number to be manipulated
people = int(input("How many people to split the bill? "))

total = round((bill/people) * (tip/100 + 1),2)
print (f"Each person will pay {total}!")