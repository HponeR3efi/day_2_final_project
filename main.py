#Day 2 Project

print ("Welcome to the tip calculator")

bill = input("What was the total bill? $")
percentage = input("What percentage tip woruld you like to hive? 10, 12, or 15?  ")
people_who_will_split_bill = input("How many people to split the bill? ")

percentage_upon_bill = int(percentage) / 100

add_percentage_to_bill = float(bill) * percentage_upon_bill

total_bill = float(bill) + float(add_percentage_to_bill)

spliting_the_total_bill_to_respective_number_of_people = round(float(total_bill) / int(people_who_will_split_bill),2)

print(f"Each person should pay: ${spliting_the_total_bill_to_respective_number_of_people}")
