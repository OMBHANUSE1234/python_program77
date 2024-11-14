dict1={69:'Samiii',70:'Yash',71:'Radhey'}
print(dict1)

#update
dict2={72:'Om'}
dict1.update(dict2)
print(dict1)

#add
dict1[73]="Pruthvi"
print(dict1)


print(dict1.keys())
print(dict1.values())

#pop
element=dict1.pop(71)
print("Popped element:",element)

#popitem
ele=dict1.popitem()
print("Last itemm popped:",ele)


#copy
copied=dict1.copy()
print("Copy:",copied)

#clear
dict1.clear()
print(dict1)