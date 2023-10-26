# SET METHODS IN PYTHON
#  values does not repeat in sets , and the values are unordered in a set.
# sets are unchangeable,and the items in a set cannot duplicate.
s={2,3,4,2,5,1}
print(s)
# different data type values are included in a set.
info = {"pihu",20,False}
print(info)
a={}
print(type(a))
# O/P: <class 'dict'>
a=set()
print(type(a))
# O/P: <class 'set'>

s1={2,4,6,8}
s2={3,6,9}

print(s1.union(s2))
# O/P: {2, 3, 4, 6, 8, 9}

s1.update(s2)
print(s1,s2)
# O/P: {2, 3, 4, 6, 8, 9} {9, 3, 6}

print(s1)
# O/P: {2, 3, 4, 6, 8, 9} -- as s1 is updated above

print(s1.intersection(s2))
# O/P: {9, 3, 6} -- these values are common in both s1 and s2, thus intersection shows the items that are common in both sets.

print(s1.symmetric_difference(s2))
# O/P: {2, 4, 8}

print(s1.difference(s2))
# o/p: {8, 2, 4}

x= {'a','b','c','d'}
y={'p','q','r','s'}
print(x.isdisjoint(y))
#   o/p:  True

z= x.union(y)
print(z)

z.update(x,y)
print(z)
# o/p: {'r', 'd', 's', 'a', 'p', 'c', 'q', 'b'}

print(z.issuperset(x))
# 

