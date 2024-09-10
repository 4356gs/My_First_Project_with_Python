# Write your code here
print("Earned amount:")

Bubblegum = 202
Toffee = 118
Ice_cream = 2250
Milk_chocolate = 1680
Doughnut = 1075
Pancake = 80

print("Bubblegum: $", Bubblegum)
print("Toffee: $", Toffee)
print("Ice cream: $", Ice_cream)
print("Milk chocolate: $", Milk_chocolate)
print("Doughnut: $", Doughnut)
print("Pancake: $", Pancake)
suma = Bubblegum + Toffee + Ice_cream + Milk_chocolate + Doughnut + Pancake
print()
print("Income: $", suma)

expense = int(input("Staff expenses:"))
other = int(input("Other expenses:"))

total_expense = expense + other

print("Net income: ",  suma - total_expense)
