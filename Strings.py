# String Syntax
str1 = "Hello1"
str2 = "Hello2"
str3 = """Hello3"""
# Printing String 1
print(str1)
# Indexing String 1
print(str1[2])
# Slicing in String 1
print(str1[0:3])
# Creating a list
list1 = "0123456789"
print(list1[0:10:2])  # Starting of index =0 Ending of indexing=10  Gap in Indexing=2
# Methods in Strings

# 1. len() function
print(len(str1))
# 2. lower() function
print(str1.lower())
# 3. upper() function
print(str1.upper())
# 4. count() function
print(str1.count("l"))
# strip() function
print(str1.strip())
# replace() function
print(str1.replace("Hello", "Kida tu"))
# Order String format
food_item = "Burger"
quantity = 10
order = "Hello Your order of {} {} is ready."
print(order.format(quantity, food_item))
