a = 'Nastya'
print(type(a), )

z = 10
print(type(z), z)

f = 5.1233
print(type(f), f)

e = bytes(9)
print(type(e), e)

g = [1, 'Nastya']
print(type(g), g)

i = tuple()
print(type(i), i)
k = tuple('create',)
print(type(k), k)

l = set()
print(type(l), l)
l = set('hello')
print(type(l), l)

m = frozenset('candy')
print(type(m), m)

n = dict
n = { }
n["country"] = "Belarus"
print(type(n), n)

b = "Good"
c = "day"
d = (b + c)
print(type(d), d)

print(a, z, sep=",")
print(a, z, sep="+")

