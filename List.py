# Learning about List\


# Creating a list
tea_varities=["Black", "Green", "Oolong", "white","Blue"]
# Priniting the list
print(tea_varities)
# Indexing the List
print(tea_varities[0]) 
# Slicing the List
print(tea_varities[0:3])
# Updating the List with slicing
tea_varities[1:2]=["Yellow "]
# Output
print(tea_varities)
# Refreshing
tea_varities=["Black", "Green", "Oolong", "white","Blue"]
# Print
print(tea_varities)
# Adding an element to the list
tea_varities[1:3]=["Masala","Black"]
# Print
print(tea_varities)

# LOOP using in list
for i in tea_varities:
    print(i,end="\t")
# Conditions use in List
if "Black" in tea_varities:
    print( "\n Black is present in the list")

# Push
tea_varities.append("Yellow")
# Pop
tea_varities.pop()
# Remove
# tea_varities.remove("Yellow")
# insert
tea_varities.insert(1,"Purple")
# List compreensiom
squared_nums=[x**2 for x in range(10)]
print(squared_nums)