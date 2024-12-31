username = "Harshal"

def func():
    username = "Prajakta"
    print(username)
    
func()
print(username)


x = 99
def func2(y):
    z = x + y
    return z

print(func2(4))


def f1(num):
    def actual(x):
        return x ** num
    return actual

f = f1(3)

print(f(2))