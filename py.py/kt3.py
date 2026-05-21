# //1

def print_hello(name):

    print(f"Пивееееееет, {name} ♥ ~")

string = "Чебурашечка"

print_hello(string)

# //2

def gcd(a,b):
    if b ==0:
        return a
    return gcd(b, a % b)
result = gcd(13,7)
print(result)