# Minnebruk O(n)
# Kjøretid O(n)
def fakultet(heltall):
    if heltall < 0:
        raise ValueError("Fakultet av negative tall finnes ikke")
    if heltall == 0:
        return 1
    return heltall*fakultet(heltall-1)

# Kjøretid Theta(n)
# Minnebruk Theta(1)
def fakultet_iterativ(heltall):
    if heltall < 0:
        raise ValueError("Fakultet av negative tall finnes ikke")
    if heltall == 0:
        return 1
    forelopig_fakultet = 1
    for i in range(1, heltall + 1):
        forelopig_fakultet *= i
    return forelopig_fakultet

if __name__ == "__main__":
    print(fakultet(5))
    print(fakultet(7))
    print(fakultet(3))
    print()
    print(fakultet_iterativ(5))
    print(fakultet_iterativ(7))
    print(fakultet_iterativ(3))