l = [52633, 8137, 1024, 999]
for j in range(0,len(l)):
    print(f'The factors of {l[j]} are\n1')
    for i in range(2, l[j]):
        if l[j] % i == 0:
            print(i)
    print(l[j])

