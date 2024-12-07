speed_limit_min = 40  
speed_limit_max = 140  

car_speed = float(input("Enter car speed: "))

if car_speed < speed_limit_min:
    print(f"Warning: invalid car speed!!")
elif speed_limit_min <= car_speed <= speed_limit_max:
    print(f"Your speed is okay!")
else:
    print(f"You need to reduce your speed!!")
