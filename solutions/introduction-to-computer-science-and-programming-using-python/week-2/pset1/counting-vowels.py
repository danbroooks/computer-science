
def isVowel(char):
    return char.lower() in 'aeiou'

count = 0

for char in s:
    count += isVowel(char)

print("Number of vowels: " + str(count))
