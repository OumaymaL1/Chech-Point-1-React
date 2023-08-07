ue = []

s1 = list(input("Veuillez entrer la première liste: ").split())
s2 = list(input("Veuillez entrer la deuxième liste: ").split())

for i in range(len(s1)):
    found_in_s2 = True
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            found_in_s2 = False
            break
    if not found_in_s2:
        ue.append(s1[i])

for i in range(len(s2)):
    found_in_s1 = True
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            found_in_s1 = False
            break
    if not found_in_s1:
        ue.append(s2[i])

print("La liste d'éléments uniques est la suivante :", ue)