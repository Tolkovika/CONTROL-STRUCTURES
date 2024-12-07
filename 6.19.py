print("Welcome to the survey! Please answer the questions below with 'y' for Yes or 'n' for No.\n")

answer1 = input("Are you interested in computer science? (y/n): ")
answer2 = input("Do you like playing computer games? (y/n): ")
answer3 = input("Do you have an Instagram account? (y/n): ")

print("\nSURVEY RESULTS:")

if answer1 == 'y':
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")

if answer2 == 'y':
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if answer3 == 'y':
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")
