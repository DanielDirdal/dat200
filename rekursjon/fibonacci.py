import numpy as np

# Kjøretid O(2**n)
def naiv_fibonacci(heltall):
    if heltall < 0:
        raise ValueError("Fibonacci-tall for negative tall finnes ikke!")
    if heltall == 0:
        return 0
    if heltall == 1:
        return 1
    return naiv_fibonacci(heltall-1) + naiv_fibonacci(heltall-2)

# Kjøretid O(n)
# Minnebruk O(n)
def rekursiv_fibonacci_dynamisk_programmering(heltall):
    if heltall < 0:
        raise ValueError("Fibonacci-tall for negative tall finnes ikke!")
    array = np.zeros(heltall + 1)
    return fibonacci_rekursiv_hjelper(heltall, array)


def fibonacci_rekursiv_hjelper(heltall, array):
    if heltall == 0:
        return 0
    if heltall == 1:
        return 1
    if array[heltall] != 0:
        return array[heltall]
    else:
        resultat = fibonacci_rekursiv_hjelper(heltall-1, array) + fibonacci_rekursiv_hjelper(heltall-2, array)
        array[heltall] = resultat
        return resultat

# Kjøretid O(n)
# Minnebruk O(1)
def iterativ_fibonacci(heltall):
    if heltall < 0:
        raise ValueError("Fibonacci-tall for negative tall finnes ikke!")
    if heltall == 0:
        return 0
    if heltall == 1:
        return 1
    n2 = 0
    n1 = 1
    resultat = 0
    for a in range(2, heltall+1):
        resultat = n1 + n2
        n2 = n1
        n1 = resultat
    return resultat


if __name__ == "__main__":
    print(naiv_fibonacci(2))
    print(naiv_fibonacci(3))
    print(naiv_fibonacci(4))
    print(naiv_fibonacci(5))
    print(naiv_fibonacci(6))
    print(naiv_fibonacci(7))
    print(naiv_fibonacci(8))
    print(naiv_fibonacci(30))
    print()
    print(rekursiv_fibonacci_dynamisk_programmering(2))
    print(rekursiv_fibonacci_dynamisk_programmering(3))
    print(rekursiv_fibonacci_dynamisk_programmering(4))
    print(rekursiv_fibonacci_dynamisk_programmering(5))
    print(rekursiv_fibonacci_dynamisk_programmering(6))
    print(rekursiv_fibonacci_dynamisk_programmering(7))
    print(rekursiv_fibonacci_dynamisk_programmering(8))
    print(rekursiv_fibonacci_dynamisk_programmering(30))
    print(rekursiv_fibonacci_dynamisk_programmering(40))
    print(rekursiv_fibonacci_dynamisk_programmering(60))
    print()
    print(iterativ_fibonacci(2))
    print(iterativ_fibonacci(3))
    print(iterativ_fibonacci(4))
    print(iterativ_fibonacci(5))
    print(iterativ_fibonacci(6))
    print(iterativ_fibonacci(8))
    print(iterativ_fibonacci(30))
    print(iterativ_fibonacci(40))
    print(iterativ_fibonacci(60))