def main():
    text_without_vowels = input("What's your text? ")
    result = shorten(text_without_vowels)
    print(result)

def shorten(word):
    vowels = "aeiouAEIOU"
    text_without_vowels = word
    for vowel in vowels:
        text_without_vowels = text_without_vowels.replace(vowel, "")
    return text_without_vowels

if __name__ == "__main__":
    main()
