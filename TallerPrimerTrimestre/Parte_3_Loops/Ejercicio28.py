
vowels = "aeiou"
vowel = 0
word = input("Ingrese una palabra > ").lower()

for i in range(len(word)):
    if word[i] in vowels:
        vowel += 1

print("La palabra ", word.capitalize(), "tiene ", vowel, "vocales")
