# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

print("Well the Program will help you to find appropriate mode of transport")
Destination_Distance=float(input("What is the distance to reach your destination="))
if Destination_Distance < 3:
    print("You should walk to your destination")
elif Destination_Distance >= 3 and Destination_Distance <= 15:
    print("You should bike to your destination")
elif Destination_Distance>15:
    print("You should use car to reach your destination")
else:
    print("Invalid input")  # This will print if the input is not a number or is
     