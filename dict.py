from csv import Dialect
from typing import Dict


dict = {"aryan":200,"nidhi":100,"gaurav":150,"srb":50,"ronak":[500,600,400,40],"vaibhav":500}

print(dict)

print(type(dict))

print(len(dict))

x= dict.keys()
print(x)

y = dict.values()
print(y)


if "vaibhav" in dict:
    print("yes")


dict.update({"aryan":700})

print(dict)


dict.update({"loki":800})
print(dict)

dict.pop("srb")
print(dict)


#loop
for items  in dict:
    print(items )



for a,b in dict.items():
    print(a,b)

    # making copy of dictionary using dict()function

mydict= dict(dict)
print(mydict)



#formskey()----to join the value of keys in dict