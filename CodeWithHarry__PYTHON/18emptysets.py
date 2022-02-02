# Important : This syntax will create a empty
# dictionary not a empty set
a={}
print(type(a))
# An empty set can be created by using
e=set()
print(type(e))
e.add(4)
e.add(8)
print(e)
# you can add tupple to set
# but can not add list/dic to set as list/dic can be changed 
e.add((4,8,9))
print(len(e))
print(e.pop())
d={'a','d','f'}
e=e.union(d)
print(e)


    