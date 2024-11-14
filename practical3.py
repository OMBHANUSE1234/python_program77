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

lst1=["abc","xyz"]
reverse_str=[i[::-1] for i in lst1]
reverse_str.sort()
rev= reverse_str[::-1]
print(rev)

# Creating a tuple
my_tuple = (1, 2, 3, "Hello", 5.5)
print(my_tuple)

# Accessing elements
print(my_tuple[0])    # Output: 1
print(my_tuple[3])    # Output: "Hello"


# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, "Hello")


# Tuple unpacking
a, b, c, d, e = my_tuple
print(a)    # Output: 1
print(d)    # Output: "Hello"






    







