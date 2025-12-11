# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.
word = input("What is the word?")
vowels = "aeiouAeiou"
count = 0
for letter in word:
    print(letter)
    
for  letter in word:
    if letter in vowels:
       count+=1  
# Challenge:
print("number of vowels is, ", [count])


# Count how many vowels are in the word.