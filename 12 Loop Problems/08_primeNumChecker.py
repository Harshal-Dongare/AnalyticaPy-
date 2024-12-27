# Prime number checker

num = 19
isPrime = True

for i in range(2, num):
    if (num%i) == 0:
        isPrime = False
        break
    
if isPrime:
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")