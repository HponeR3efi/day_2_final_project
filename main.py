#Day 2 Project

print ("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip woruld you like to hive? 10, 12, or 15?  "))
people_who_will_split_bill = int(input("How many people to split the bill? "))

percentage_calculation = percentage / 100

percentage_on_bill = bill * percentage_calculation 

total_bill_with_percentage = bill + percentage_on_bill

total_bill_splited_by_people = total_bill_with_percentage / people_who_will_split_bill

# there are two ways to get decimal numbers in python , here are these two examples

final_bill = round(total_bill_splited_by_people,2)
final_bill = "{:.2f}".format(total_bill_splited_by_people)

print(f"Each person should pay: ${final_bill}")
