
bypieces = {}

phrase = input("\nIngresa una frase > ").lower()

words = phrase.split()
for word in words:
    if word in bypieces:
        bypieces[word] += 1
    else:
        bypieces[word] = 1
print("\nContador de palabras")
for word in bypieces:
    print(f"\n{word} -> {bypieces[word]}")