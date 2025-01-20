length = float(input("What is the Room Length? : "))
width = float(input("what is the Room Width? : "))
cost_per_sqft = float(input("What is the cost per square foot? : "))

square_footage = length * width

flooring_cost = square_footage * cost_per_sqft

tax = cost_per_sqft * 0.07

total_cost = tax + flooring_cost

print("----RECEIPT-----")
print("Square Feet : ", square_footage)
print("Flooring Cost : ", flooring_cost)
print("Tax : ", tax)
print("Total : ", total_cost)
