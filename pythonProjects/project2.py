#Projeto2

print("Welcome to the tip calculator!")
bill = float(input("How much was the total cost of the bill?"))
bill = round(bill, 2)

tip = float(input("How much tip would you like to give? 10, 12 or 15%"))
tip = bill*(tip/100)
totalBill = round(bill + tip, 2)

numPeople = int(input("How many people to split the bill?"))
totalBill = round(totalBill/numPeople, 2)

print(f"Each person must pay {totalBill}€.")