branches = ["Branch A", "Branch B", "Branch C"]
categories = ["Salary", "Rent", "Transport"]

expenses = [
    [50000, 15000, 10000],
    [60000, 12000, 8000],
    [45000, 18000, 12000]
]

branch_totals = []

print("--- Branch Expense Analysis ---")

for i in range(len(branches)):
    total = sum(expenses[i])
    average = total / len(categories)
    branch_totals.append(total)

    print("\nBranch:", branches[i])
    print("Salary:", expenses[i][0])
    print("Rent:", expenses[i][1])
    print("Transport:", expenses[i][2])
    print("Total Expense:", total)
    print("Average Expense:", round(average, 2))

print("\n--- Category Totals ---")

category_totals = []

for j in range(len(categories)):
    total = 0

    for i in range(len(branches)):
        total += expenses[i][j]

    category_totals.append(total)
    print(categories[j], ":", total)

largest_branch = branch_totals.index(max(branch_totals))
largest_category = category_totals.index(max(category_totals))

print("\nBranch with Highest Expense:", branches[largest_branch])
print("Highest Branch Expense:", branch_totals[largest_branch])

print("Largest Expense Category:", categories[largest_category])
print("Category Total:", category_totals[largest_category])

grand_total = sum(branch_totals)
print("Grand Total Expense:", grand_total)
print("Average Branch Expense:", round(grand_total / len(branches), 2))