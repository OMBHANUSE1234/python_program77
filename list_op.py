list1= ["apple", "banana", "cherry", "mango"]
print(list1)
print(list1[::-1])
list1.remove("apple")
print(list1)
list1.sort()
print(list1)
list1.insert(2,"orange")
print(list1)


for x in list1 :
    print(x)



# vowels=['a','e','i','o','u']
# word=input("Enter string:")
# found=[]
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
#
# print(found)

#print even numbers from list

def even(list2):

    list3=[]
    for i in list2:
        if i%2==0:
            list3.append(i)

    print(list3)
list2=[1,2,3,4,5,6,7,8]
even(list2)


    







