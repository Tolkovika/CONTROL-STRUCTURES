# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus_percentage = 0.15  

is_bonus = input('Does the employee receive a bonus? (Y/N): ').strip().upper() == 'Y'

if is_bonus:
    bonus = basic_salary * bonus_percentage
    total_salary = basic_salary + bonus
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included? {"Yes" if is_bonus else "No"}')
print(f'Total salary: {total_salary} PLN')
