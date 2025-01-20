
# Program Name: Lab1.py
# Course: IT1114/Section W03
# Student Name: Ronnie Vincenty
# Assignment Number: Lab1
# Due Date: 01/19/2025
# Purpose: This program calculates the total cost of flooring for a room.
#          It takes the room's dimensions and cost per square foot as input,
#          then calculates the flooring cost, tax (7%), and total amount due.


# Gather user input and convert to floats for
# room dimensions and cost to be used later.

length = float(input("What is the Room Length? : "))
width = float(input("what is the Room Width? : "))
cost_per_sqft = float(input("What is the cost per square foot? : "))

#calculate square footage
square_footage = length * width

#calculate flooring cost
flooring_cost = square_footage * cost_per_sqft

#calculate tax
tax = cost_per_sqft * 0.07

#calculate total cost
total_cost = tax + flooring_cost

#print receipt
print("-" * 47)
print("-" * 47)
print("*" * 19, "RECEIPT" , "*" * 19)
print("Square Feet : ", square_footage)
print("Flooring Cost : ", flooring_cost)
print("Tax : ", tax)
print("Total : ", total_cost)
