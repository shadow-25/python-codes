list=[1,2,3,4,5,6,7,8,9,"a","b","c"]
print(list[0])
print(list[:])
print(list[::-1])
if 2 in list:
    print("yes")
else:
    print("no")

lis=[i for i in range(51) if i%2==0]
print(lis)
li=[100,50,40,66,12,50]
li.append(154) #Append object to the end of the list.
li.sort() #Sort the list in ascending order and return None.
print(li)
li.sort(reverse=True) #Sort the list in descending order and return None.
print(li)
print(li.index(12)) #Return first index of value.
print(li.count(50)) #Return number of occurrences of value.
la=li #create reference of original list and any change in reference will result in change in original list
le=li.copy() #Return a shallow copy of the list.
le[0]=121
print(le)
li.insert(3,545)
print(li)
k=li+le #add both list
print(k)
li.extend(le) #Extend list by appending elements from the iterable.
print(li)

