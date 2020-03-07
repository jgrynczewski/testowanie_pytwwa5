
# a = [3, 4, -2, 0]
#
# print(a.sort())
# b = sorted(a)
# print(a)
# print(b)

# Kopiowanie przez wartość
# a = 4
#
# def increment(a):
#     a = a+1
#     return a
#
# increment(a)
#
# print(a)

# Kopiowanie przez referencje
# a = [3]
#
# def increment(a):
#     a[0] = a[0]+1
#     return a
#
# increment(a)
#
# print(a)

# a = 5
# b = a
#
# a = a+1
# print(b)
#
# c = [4]
# d = c
#
# c.append(5)
# print(d)


a_list = [1, 2, 3]

class A:
    def powieksz(self, a):
        a.append(4)

a = A()
a.powieksz(a_list)
a.powieksz(a_list)
a.powieksz(a_list)
print(a_list)

