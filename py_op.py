#remove duplicates elements from list

my_list1=[1,1,1,4,4,6,5,6,7]
unique_list=list(set(my_list1))

print(unique_list)
#output:[1, 4, 5, 6, 7]

#find transpose of matrix
my_list2=[[1,2,3],
          [4,5,6],
          [7,8,9]]

transpose=[list(i) for i in zip(*my_list2)]
print(transpose)
#o/p:[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#find most frequent element in list
my_list3=[23,44,77,44,44,93,23]

most_frequent=max(my_list3,key=my_list3.count)
print(most_frequent)#44

#Convert list into dictionary

list4=["ID","Name","Age"]
list5=["101","John","20"]
my_dict=dict(zip(list4,list5))
print(my_dict)

#{'ID': '101', 'Name': 'John', 'Age': '20'}