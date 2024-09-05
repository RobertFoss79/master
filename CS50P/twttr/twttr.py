text = input("What's your text? ")

vowels = "aeiouAEIOU"

text_without_vowels = text
for vowel in vowels:
    text_without_vowels = text_without_vowels.replace(vowel, "")

print(text_without_vowels)
