# Problem: Regn ut tverrsummen av et heltall.
#
# Tverrsum er summen av sifrene tallet består av, så summen av tallet 46342 er
# 4 + 6 + 3 + 4 + 2 = 19

# Algoritme:
# lag en variabel naaverande_tall, og sett den lik tallet
# lag en variabel tverrsum, og sett den lik 0
# Fortsett inntil naaverande_tall er 0
#   Finn det siste sifferet gjennom naaverande_tall mod 10
#   Legg det siste sifferet til tverrsummen
#   sett naaverande_tall lik naaverande_tall // 10
# returner tverrsum

# Kjøretid blir:
# Hvis problemstørrelsen n er antall siffer: Theta(n)
# Hvis problemstørrelsen m er størrelsen til tallet: Antall siffer er Theta(log10(n))
#   Dermed blir kjøretida Theta(log10(n))
def tverrsum(heltall):
    naaverande_tall = heltall                           # Kjører 1 gang
    tverrsum = 0                                        # Kjører 1 gang
    while naaverande_tall > 0:                          # Kjører i Theta(antall siffer)
        siste_siffer = naaverande_tall % 10             # Kjører i Theta(antall siffer)
        tverrsum += siste_siffer                        # Kjører i Theta(antall siffer)
        naaverande_tall = naaverande_tall // 10         # Kjører i Theta(antall siffer)
    return tverrsum                                     # Kjører 1 gang

if __name__ == "__main__":
    jeff = tverrsum(46342)
    print(tverrsum(46342))