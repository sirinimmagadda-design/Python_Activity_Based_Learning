v = int(input("Enter number of vehicles: "))
vehicles = []

for i in range(v):
    name = input("Enter vehicle name: ")
    capacity = float(input("Enter vehicle capacity in kg: "))
    vehicles.append([name, capacity, capacity])

n = int(input("\nEnter number of packages: "))
packages = []

for i in range(n):
    print("\nPackage", i + 1)
    name = input("Enter package ID: ")
    zone = input("Enter destination zone: ")
    weight = float(input("Enter package weight: "))
    priority = int(input("Enter priority (1-3): "))

    packages.append([name, zone, weight, priority])

# Higher priority packages are handled first
packages.sort(key=lambda x: x[3], reverse=True)

print("\n--- Dispatch Report ---")

for package in packages:
    assigned = False

    for vehicle in vehicles:
        if vehicle[1] == package[1] and vehicle[2] >= package[2]:
            print(package[0], "assigned to", vehicle[0])
            vehicle[2] -= package[2]
            assigned = True
            break

    if not assigned:
        print(package[0], "cannot be dispatched")

print("\n--- Remaining Vehicle Capacity ---")

for vehicle in vehicles:
    print(vehicle[0], ":", vehicle[2], "kg remaining")