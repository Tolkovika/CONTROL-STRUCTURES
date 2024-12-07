# Prints the name of university where you are studying
# with an extra space between characters

university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(university)  # original university name
print(university_expanded.strip())  # expanded university name
