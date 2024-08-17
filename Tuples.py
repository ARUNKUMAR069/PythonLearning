# Creating a tuple
tea_types=("Black","Green","Olong")
# Printing Tuple
print(tea_types)
# Indexing in Tuple
print(tea_types[0])  # Output: Black
print(tea_types[-1])  # Output: Olong
# Length count in Tuple
print(len(tea_types))  # Output: 3 
# Conatination in tuple
more_tea=("Herbal","Earl Grey")
all_tea= tea_types+more_tea
print(all_tea)
# Condition in Tuple
if "Green" in all_tea:
    print("I have Green Tea")
# Finding Duplicate values or Count
more_tea=("Herbal","Earl Grey","Herbal")
print(more_tea.count("Herbal"))
# Nested tuple
nest_tuple=("hEloo",(1,2,3,4,5,6),"yes")
print(nest_tuple)
