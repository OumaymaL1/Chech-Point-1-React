wc = 0
wv = 0

sentence = input("Veuillez écrire une phrase : ")
for i in range(len(sentence)):
    if sentence[i] in "oiyeauOIYEAU":
        wv += 1
    if sentence[i] == ' ':
        wc += 1

wc += 1

print("The number of vowels is:", wv)
print("The number of words is:", wc)