n = int(input("Enter number of days: "))

for i in range(n):
    print("\nDay", i + 1)

    day = input("Enter day name: ")
    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))
    leftover = int(input("Enter leftover meals: "))

    if prepared < 0 or served < 0 or leftover < 0:
        print("Invalid input")
        continue

    if served + leftover != prepared:
        print("Invalid data: meals do not match")
        continue

    if prepared == 0:
        waste = 0
    else:
        waste = (leftover / prepared) * 100

    print("Day:", day)
    print("Meals Prepared:", prepared)
    print("Meals Served:", served)
    print("Leftover Meals:", leftover)
    print("Wastage Percentage:", round(waste, 2), "%")

    if waste > 10:
        print("Warning: Food wastage exceeds limit!")
    else:
        print("Food wastage is within the limit.")