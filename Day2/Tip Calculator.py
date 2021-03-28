print("Welcome to The Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage would you like to give? 10, 12, or 15? "))
nr_people = int(input("How many people to split the bill? "))
tip_percent = tip/100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_div = total_bill / nr_people 
result = "{:.2f}".format(bill_div)
print(f"Each person should pay: ${result}")