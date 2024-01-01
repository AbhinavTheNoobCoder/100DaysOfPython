#DAY 23 - Basic/common list manipulations
l = [9, 11, 1, 6, 2]
l.sort() #ascending order
print("Sorted List l =", l)
l.sort(reverse=True) #descending order
print("Reverse sorted List l =", l)
l.append(8) #add at end
print("List l with 8 appended =", l)
l.insert(0, 19) #index, value
print("List l with 19 inserted at index 0 =", l)
m = l.copy() #m = l would make m and l point at same memory address, copy prevents it
m[0] = 7
print("List m =", m)
print("List l =", l)
m = l
m[0] = 7
print("List m =", m)
print("List l =", l)
l.extend("Abhinav") #extend takes iterable object and adds each element at the end of the list
print("List l extended with 'Abhinav' =", l)
l.reverse()
print("Reversed List l =", l)
print("Count of element 6 in list l =", l.count(6))
print("Index of element 6 in list l =", l.index(6))