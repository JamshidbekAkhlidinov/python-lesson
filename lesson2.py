thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[1])

print(len(thislist))

list1 = list(("apple", "banana", "cherry"))
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

print(list1 + list2 + list3 + list4)

print(type(list4))

print(type(list1))

print(thislist[-2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])


if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# thislist[1] = "blackcurrant"
# print(thislist)
#
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist[1:3] = ["watermelon"]
# print(thislist)

print(thislist)
thislist.insert(2, "watermelon")
print(thislist)

thislist.append("test")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)

thislist.clear()
print(thislist)