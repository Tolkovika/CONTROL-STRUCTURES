# Female name checker
name = input("Enter name: ")
if name[-1].lower() == 'a':
    print(f"{name} -- Polish female name")
else:
    print(f"{name} -- Not a typical Polish female name")
