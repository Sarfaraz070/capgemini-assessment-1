
Total_bill = int(input("ENTER THE TOTAL BILL: "))
number_people = int(input("ENTER TOTAL NUMBER OF PEOPLE: "))
any_tip = int(input("ENTER THE TIP AMOUNT YOU WANT TO GIVE: "))

# Correct the calculation of the total amount to pay
Amount_to_pay = Total_bill + any_tip

# Calculate how much each person should pay
amount_per_person = Amount_to_pay / number_people
print(f"Each person has to pay: {int(amount_per_person)}")