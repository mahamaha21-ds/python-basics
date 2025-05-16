#list
lst=[10,30,40]
lst.insert(1,20)
print(lst)

lt=[10,30]
lt.append([70])
lt.extend([70])
print(lt)

#tuple
tup=(1,)
print(tup)

a="troll"
print(a[:])

def name(username):
    if username=="maha":
        return 0
    return 1
if name("")==1:
    print("invalid name")
elif name("maha")==0:
    print("valid name")


def search(lst, value):
    for i in lst:
        if i == value:
            return 0  # found
    return 1  # not found

if search([1,2,3], 2) == 0:
    print("Value found")


#strip()
txt=("   hello,maha ")
clean=txt.strip()
print(clean)

x=8
print("the covert{:.2f}".format(x))

#bool
x=bool(0)
print(x)

y=bool(-1.0)
print(y)

c=bool("")
print(c)

#operator
a=5
b=8
print(a>b)

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

if 5==4 or 5==5:
    print("statement occured")

#Python Lists
mylist=["apple","cherry","banana"]
print(mylist[2])

mylist=["apple","cherry","banana"]
print(len(mylist))

mylist=["apple","cherry","banana"]
print(mylist[-1])

sli=["apple","banana","grape","orange"]
print(sli[1:3])

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

#Python Add List Items
crl=["apple","banana","orange"]
crl.insert(0,"grape")
print(crl)

mist = ['apple', 'banana', 'cherry']
mist.insert(0, 'orange')
print(mist[1])

gm=["hello","raja","ram"]
gm.append("raja")
print(gm)

market=["things","food","radio","jam"]
market.insert(1,"lemon")
print(market)

