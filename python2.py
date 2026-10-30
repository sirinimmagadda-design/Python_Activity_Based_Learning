n = int(input("Enter number of months: "))

bills = []

for i in range(n):
    print("\nMonth", i + 1)
    month = input("Enter month name: ")
    units = int(input("Enter units consumed: "))

    # Progressive slab calculation
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05
    total = energy + fixed + surcharge

    # Rebate for low consumption
    if units <= 100:
        rebate = total * 0.10
    else:
        rebate = 0

    total = total - rebate

    bills.append([month, units, total])

    print("Energy Charge: Rs.", round(energy, 2))
    print("Fixed Charge: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))

print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print(bills[i][0], "- Rs.", round(bills[i][2], 2))

    if i > 0:
        increase = bills[i][2] - bills[i - 1][2]

        if increase > bills[i - 1][2] * 0.30:
            print("Warning: Unusual increase in bill!")
        elif increase > 0:
            print("Bill increased by Rs.", round(increase, 2))
        else:
            print("No increase in bill.")