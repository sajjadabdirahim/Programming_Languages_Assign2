# Sajjad Abdirahim Gedow    Reg No: SCT211-0065/2022

# Assignment 2 PART A Data Type Recap - Tip Calculator

total_bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

tip_amount = total_bill * (tip_percentage / 100)

total_per_person = (total_bill + tip_amount) / num_people

total = round(total_per_person, 2)

print(f"Each person should pay: Ksh. {total}")
