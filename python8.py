n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter student name: ")
    fee_due = float(input("Enter pending fee amount: "))
    attendance = float(input("Enter attendance percentage: "))
    marks = float(input("Enter internal marks: "))

    reasons = []

    if fee_due > 0:
        reasons.append("Fee Pending")

    if attendance < 75:
        reasons.append("Low Attendance")

    if marks < 40:
        reasons.append("Low Internal Marks")

    print("\n--- Eligibility Audit ---")
    print("Student:", name)

    if len(reasons) == 0:
        print("Status: Eligible for Examination")
    else:
        print("Status: Not Eligible")
        print("Reasons:")
        for reason in reasons:
            print("-", reason)