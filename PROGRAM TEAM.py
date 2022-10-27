print("\nYou're on your lunch break, which restaurant do you want to go to?")
print("1. Potbelly")
print("2. Chick-fil-A")
print("3. Beggar's Pizza")
print("4. McDonald's")
print("5. Dunkin'")
print("0. None (Exit the program)")

number = int(input("\nNumber: "))

if number == 1:
    print("You went to eat at Potbelly!")
if number == 2:
    print("You went to eat at Chick-fil-A!")
if number == 3:
    print("You went to eat at Beggar's Pizza!")
if number == 4:
    print("You went to eat at McDonald's!")
if number == 5:
    print("You went to eat at Dunkin'!")
if number == 0:
    print("You did not eat at any of the places listed")
    exit()
