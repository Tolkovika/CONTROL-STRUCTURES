# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month in [1, 2, 3]:
    quarter = 1
elif month in [4, 5, 6]:
    quarter = 2
elif month in [7, 8, 9]:
    quarter = 3
elif month in [10, 11, 12]:
    quarter = 4

print(f'Month {month} is in quarter {quarter}')
