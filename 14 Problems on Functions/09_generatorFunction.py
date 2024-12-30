# Generator function

# Write a generator function that yields even numbers up to a specified unit

def even_generator(limit):
    for i in range(2, limit +1, 2):
        yield i
        
for num in even_generator(10):
    print(num)