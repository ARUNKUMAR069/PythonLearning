# Problem 1
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# Solution
# 1 Step Taking user age as input
age=int(input("Enter your Age:"))
print(age)
# 2 Step Using if-elif-else statement to classify the age group
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
elif 60<=age:
    print("Senior")
else:
    print("Invalid age")


