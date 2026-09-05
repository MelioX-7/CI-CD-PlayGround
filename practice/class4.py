def greet(name):
    return "Hello " + name


def add(a, b):
    return a + b


def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"


print(greet("Kathir"))
print(add(10, 5))
print(check_age(21))
print(check_age(15))
