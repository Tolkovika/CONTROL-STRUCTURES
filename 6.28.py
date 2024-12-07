first_term = 0
second_term = 1

print(first_term, second_term, end=" ")

for _ in range(18):  
    next_term = first_term + second_term
    print(next_term, end=" ")

    first_term = second_term
    second_term = next_term
