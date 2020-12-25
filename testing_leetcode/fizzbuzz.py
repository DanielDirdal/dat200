
for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 != 0:
        print(f"{i}: fizz")
    if i % 5 == 0 and i % 3 != 0:
        print(f"{i}: buzz")
    if i % 5 == 0 and i % 3 == 0:
        print(f"{i}: fizzbuzz")


