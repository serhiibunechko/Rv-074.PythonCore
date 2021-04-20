class Ntm:
    name = str(input("Hello, what is your name? "))
    age = int(input("How old are you? "))
    city = str(input("Where do you live? "))


ntm = Ntm()
print("Hello, ", getattr(ntm, "name"))                          # method 1
print("You are", ntm.age, "years old")                          # method 2
print('You are form', ntm.city)
