#DAY 32 - Set methods
set1 = set()
set2 = set()
while True:
    elementsfor1 = input("Add an element to set1: ")
    set1.add(elementsfor1)
    cont = input("Do you want to continue (yes/no): ").lower()
    if cont == 'no':
        break
while True:
    elementsfor2 = input("Add an element to set 2: ")
    set2.add(elementsfor2)
    cont = input("Do you want to continue (yes/no): ").lower()
    if cont == 'no':
        break
print("Set1", set1)
print("Set2", set2)
print(f'''Set operations -
Union - {set1.union(set2)}
Intersection - {set1.intersection(set2)}
Symmetric Difference - {set1.symmetric_difference(set2)}
Set1 - Set2 = {set1.difference(set2)}
Set2 - Set1 = {set2.difference(set1)}
Are Set1 and Set2 disjoint? - {set1.isdisjoint(set2)}
Is Set1 a subset of Set2, or, Set2 is a superset of Set1? - {set1.issubset(set2)}
Is Set2 a subset of Set1, or, Set1 is a superset of Set2? - {set2.issubset(set1)}
''')
# Also got to learn about set1.clear(), set1.update(), set1.difference_update()
# set1.pop(), set1.discard(), set1.remove() but didn't include them here.