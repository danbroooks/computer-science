
from string import ascii_lowercase

def chr(char):
    return ascii_lowercase.index(char.lower())

def trim_alphabetical(str):
    output = str[0]

    if (len(str) < 2):
        return output

    for char in str[1:]:
        last = output[-1];
        if (chr(char) >= chr(last)):
            output += char
        else:
            break

    return output


longest = ''

for i in range(len(s)):
    trim = trim_alphabetical(s[i:])

    if (len(trim) > len(longest)):
        longest = trim

print("Longest substring in alphabetical order is: " + longest)

