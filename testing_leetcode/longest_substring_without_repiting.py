s = "supasupor"

liste = []
liste2 = []

for i in range(len(s)):
    if s[i] not in liste:
        liste.append(s[i])
    elif s[i] == s[i-1]:
        for j in liste:
            liste2.append(j)
        liste.clear()

if len(liste) > len(liste2):
    print(len(liste))
else:
    print(len(liste2))


