
# Kjøretid: Best case O(1)
#           Worst case O(n)
def palindrom(streng, string):
    if len(streng) <= 1:
        return f"{string} er et palindrom"
    if streng[0] == streng[-1]:
        return palindrom(streng[1:-1], string)
    return f"{string} er ikke et palindrom som vi kan se {string[::-1]}"

# Kjøretid: Best case O(1)
#           Worst case O(n)
def palindrom_iterasjon(streng, string):
    if len(streng) <= 1:
        return f"{string} er et palindrom"
    for i in range(len(streng)):
        if len(streng) <= 1:
            return f"{string} er et palindrom"
        if streng[0] == streng[-1]:
            streng = streng[1:-1]
        else:
            return f"{string} er ikke et palindrom som vi kan se {string[::-1]}"

if __name__ == "__main__":
    streng = "regninger"
    print(palindrom(streng, streng))
    print(palindrom("jeff", "jeff"))
    print(palindrom("", ""))
    print()
    print(palindrom_iterasjon(streng, streng))
    print(palindrom_iterasjon("jeff", "jeff"))
    print(palindrom_iterasjon("i", "i"))
