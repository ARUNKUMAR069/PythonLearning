# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# Solution: Write a program that asks for the customer's age and the day of the week,
# then calculates the ticket price based on the customer's age and the day of the week.
age=int(input("Enter Your age:"))
day_of_week=str(input("Enter the day of the week:"))
ticket_price=0

if  18<= age:
    ticket_price=12
else:
    ticket_price=8

if day_of_week=="Wednesday":
    ticket_price-=2
    print("You get a Special Discount of 2$")
    
print("Ticket Price:",ticket_price,"$")
