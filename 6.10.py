# Dog's age in dog's years
dog_age_human = int(input("Enter the dog's age in human years: "))
if dog_age_human <= 2:
    dog_age_dog = dog_age_human * 10.5
else:
    dog_age_dog = 21 + (dog_age_human - 2) * 4

print(f"The dog's age in dog's years is {dog_age_dog} years.")
