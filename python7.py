n = int(input("Enter number of students: "))
quota = int(input("Enter scholarship quota: "))
students = []

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    if marks >= 75 and attendance >= 75 and income <= 200000:
        students.append([name, marks, attendance])
    else:
        print("Not eligible")

students.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n--- Scholarship Selection ---")

for i in range(min(quota, len(students))):
    print("Rank:", i + 1)
    print("Name:", students[i][0])
    print("Marks:", students[i][1])
    print("Attendance:", students[i][2])
    print("Scholarship Awarded\n")

print("Total Selected:", min(quota, len(students)))s