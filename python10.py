n = int(input("Enter number of participants: "))
participants = []
registration_fees = 0

for i in range(n):
    print("\nParticipant", i + 1)
    reg_id = input("Enter registration ID: ")
    name = input("Enter participant name: ")
    fee = float(input("Enter registration fee: "))

    duplicate = False

    for p in participants:
        if p[0] == reg_id:
            duplicate = True
            break

    if duplicate:
        print("Duplicate registration detected")
    else:
        participants.append([reg_id, name])
        registration_fees += fee
        print("Registration accepted")

sponsorship = float(input("\nEnter sponsorship contributions: "))
expenses = float(input("Enter total festival expenses: "))

total_income = registration_fees + sponsorship
balance = total_income - expenses

print("\n--- Festival Financial Audit ---")
print("Valid Participants:", len(participants))
print("Registration Fees: Rs.", registration_fees)
print("Sponsorship: Rs.", sponsorship)
print("Total Income: Rs.", total_income)
print("Total Expenses: Rs.", expenses)
print("Final Balance: Rs.", balance)

if balance > 0:
    print("Result: Profit")
elif balance < 0:
    print("Result: Loss")
else:
    print("Result: No Profit, No Loss")