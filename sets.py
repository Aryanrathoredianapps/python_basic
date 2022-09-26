fruits = {"apple","orange","bannana"}
print(fruits)
print(type(fruits))

fruits2 ={"kiwi","watermelon","cherry","mango"}
fruits.update(fruits2)

print(fruits)

fruits.pop()
print(fruits)


fruits.remove("cherry")
print(fruits)

for items in fruits:
    print(items)