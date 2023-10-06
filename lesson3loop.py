thislist = ["apple", "banana", "cherry"]
print(thislist)

for x in thislist:
    print(x)

print(5 * "--" + "range" + 5 * "--")
for i in range(len(thislist)):
    print(thislist[i])

print(5 * "--" + "while" + 5 * "--")
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

print(5 * "--" + "one function" + 5 * "--")

[print(x) for x in thislist]
[print(x) for x in ["salom", "qale", "yaxshimi"]]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist22 = [x.upper() for x in fruits]
print(newlist22)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)


def myfunc(n):
    return n


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
