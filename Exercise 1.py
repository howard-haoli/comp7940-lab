x = 52633
print(f'The factors of {x} are\n1')
for i in range(2, x):
    if x % i == 0:
        print(i)
print(x)
