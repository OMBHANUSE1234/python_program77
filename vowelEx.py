vowels=['a','e','i','o','u']
word=input("Enter string:")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)

#Enter string:Om Bhanuse
#['a', 'u', 'e']