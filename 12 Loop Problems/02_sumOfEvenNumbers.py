# Calculate sum of even numbers

n = 12
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += i
    
print("Sum of Even numbers:", sum_even)
