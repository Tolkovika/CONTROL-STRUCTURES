# Electronic thermometer
temperature = int(input("Enter temperature in Celsius: "))
if temperature > 35:
    print("It is extremely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold")
else:
    print("Warning, frost")
