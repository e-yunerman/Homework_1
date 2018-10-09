#define an array
x = [0.0, 3.0, 5.0, 2.5, 3.7]		
print(type(x))

#remove the third element from the array
x.pop(2)
print(x)

#remove the element equal to 2.5
x.remove(2.5)
print(x)

#add an element at the end (note: there are other ways to add elements into an array)
x.append(1.2)
print(x)

#get a copy of the array
y = x.copy()
print(y)

#how many elements are 0.0
print(y.count(0.0))

#print the index with the value 3.7
print(y.index(3.7))

#sort the list (from smallest to largest)
y.sort()
print(y)

#reverse sort (sort from largest to smallest)
y.reverse()
print(y)

#remove all elements from the array
y.clear()
print(y)