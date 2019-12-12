import re
f = open("nirav.txt", "r+")
data = f.read()
numofword = len(data.split())
print(data)
print(numofword)


def four_letters():
    f = open("nirav.txt", "r+")
    data = f.read()
    test = data.split()
    ee = [i for i in test if len(i) == 4]
    eee = ee.__len__()
    return eee


import re


# print(four_letters())
def the():
    count = 0
    f = open('nirav.txt', 'r+')
    data = f.read()
    tu = re.findall('the', data)
    ee = tu.__len__()
    return ee


print(the())


def replace():
    count = 0
    f = open('nirav.txt', 'r+')
    data = f.read()
    kkk = re.sub('Scrooge', 'the Grinch', data)
    return kkk


print(replace())
