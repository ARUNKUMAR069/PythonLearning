# Introduction to Dictionary
# Creating Dictonary
chai_types={
#"Key":"value",
"Masala": "Spicy",
"Ginger": "Zesty",
"Green": "Mild",
}
# Printing Dict
print(chai_types) 
# First Method to get values from dictionary
chai_types["Green"]="Fresh"
print(chai_types)
# Second method to get values from dictionary
a=chai_types.get("Green")
print(a)
# For Loop in Dictionary
for chai in chai_types:
    print(chai,chai_types[chai]) 
# Conditional Statements in Dictionary
if "Masala" in chai_types:
    print("I have masala chai")
    # Adding new key and value in Dict
chai_types["Earl grey"]="Citrus"
print(chai_types)
# Pop the Dictionary with key refrence
chai_types.pop("Ginger")
print(chai_types)
# Pop the Dictionary without key refrence
chai_types.popitem()
print(chai_types)
# Use of Delete Keyword to remove the key and it's value from the memory refrence
del chai_types["Green"]
print(chai_types)
# USe of Copy fn in Dict
chai_types_copy=chai_types.copy()
# Multi Dimmensional Dictionary
tea_shop={
    "chai":{"Masala":"Spicy","Ginger":"Zesty"},
    "tea":{"Green":"Mild","Black":"Strong"}
}
