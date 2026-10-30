n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    subject = float(input("Enter minimum subject marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
        students.append([name, marks, attendance, income])
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")

# Sort by aggregate marks, then attendance
students.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students")
else:
    rank = 1
    for student in students:
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print()
        rank += 1
3