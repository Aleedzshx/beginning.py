

count = {}

word = input("\nIngresa una palabra > ")
for letter in word:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print("\nContador de letras")
for letter in count:
    print(f"\n{letter} -> {count[letter]}")

