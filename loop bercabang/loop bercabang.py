a = 1

while a < 5:
    b = 0
    while(b<a):
        print("*", end='')
        b += 1
    print()
    a += 1

for a in range(1,5):
    for b in range(1,5):
        c = a*b
        print(c,end=' ')
    print()