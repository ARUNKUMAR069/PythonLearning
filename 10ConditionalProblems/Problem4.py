# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit_name="Banana"
print("Fruit name is "+fruit_name)
fruit_colour=str(input("Enter the colour of Fruit ="))
if "Green"== fruit_colour:
    print(fruit_name + " is Unripe")
elif "Yellow"== fruit_colour:
    print(fruit_name + " is Ripe")
elif "Brown" == fruit_colour:
    print(fruit_name + " is Overripe")
else:
    print(fruit_name + " is Unknown")