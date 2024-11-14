
group1={"cricket","reading","trekking","travelling","cricket"}
group2={"reading","gaming","painting","reading"}

#1.Removing all duplicate hobbies

print("Unique set1:",group1)

print("Unique set2:",group2)


#2.Display unique hobbies in alphabetical order
unique=[]
for i in group1:
    unique.append(i)


alpaha1=sorted(unique)
print("Alphabetical Order 1:",alpaha1)

unique2=[]
for i in group2:
    unique2.append(i)

alpaha2=sorted(unique2)
print("Alphabetical Order 2:",alpaha2)



#3.Find commnon hobbies between two separate groups of survey participants
common=[]
for hobbie in group1:
    if hobbie in group2:
        common.append(hobbie)

print("Common hobbies:",common)


#4.Hobbies unique to one group but not other
print("Difference:",group1.difference(group2))





