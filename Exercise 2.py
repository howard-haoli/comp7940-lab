x = 52633
def print_factor(x):
    print(f'The factors of {x} are\n1')
    for i in range(2, x):
        if x % i == 0:
           print(i)
    print(x)
print_factor(x)