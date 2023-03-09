n = input()
numbers = list(map(int, input().split()))
count = 0
for number in numbers:
    if number == 1:
        continue
    elif number == 2 or number == 3:
        count += 1
    else:
        is_it_prime = True
        for i in range(2, number-1):
            if number % i == 0:
                is_it_prime = False
                break
        if is_it_prime:
            count += 1

print(count)
