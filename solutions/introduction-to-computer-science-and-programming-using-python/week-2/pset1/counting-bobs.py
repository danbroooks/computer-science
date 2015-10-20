
count = 0

for i in range(len(s)):
    count += (s[i:i+3] == 'bob')

print("Number of times bob occurs is: " + str(count))
