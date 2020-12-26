# Problemstørrelse: Størrelsen på tallet n
# Kjøretid: O(n)
def sum_heltall_lokke(n):
    if n <= 0:                      # Kjører 1 gang uansett n
        return 0                    # Kjører 1 gang hvis n <= 0
    forelopig_sum = 1               # Kjørere 1 gang uansett n
    for tall in range(2, n+1):      # Kjører n ganger
        forelopig_sum += tall       # Kjører n ganger
    return forelopig_sum            # Kjører 1 gang uansett n


# Kjøretid: O(1)
def sum_heltall_formel(n):
    if n <= 0:                      # Kjører 1 gang uansett n
        return 0                    # Kjører 1 gang hvis n <= 0
    return (n*(n+1))//2             # Kjører 1 gang uansett n

for n in range(1, 10):
    print(sum_heltall_lokke(n))
    print(sum_heltall_formel(n))