n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    consultation = float(input("Enter consultation charge: "))
    diagnostic = float(input("Enter diagnostic charge: "))
    treatment = float(input("Enter treatment charge: "))
    age = int(input("Enter patient age: "))

    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid charges")
        continue

    total = consultation + diagnostic + treatment

    # Concession policy
    if age >= 60:
        discount = total * 0.20
    elif total >= 10000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    # Patient classification
    if final_bill >= 10000:
        category = "High Payment"
    elif final_bill >= 5000:
        category = "Medium Payment"
    else:
        category = "Low Payment"

    print("\n--- Patient Bill ---")
    print("Patient Name:", name)
    print("Total Charges: Rs.", round(total, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Bill: Rs.", round(final_bill, 2))
    print("Patient Category:", category)