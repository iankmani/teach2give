# Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for char in sentence:
        if char.lower() in vowels:
            vowel_count += 1
    
    return vowel_count
sentence = "Hello World"
print("Number of vowels:", count_vowels(sentence))  # Output: 2