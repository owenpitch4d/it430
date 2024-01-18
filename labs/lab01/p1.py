# p1.py

import sys

print("Filename: ", end="")

myDict = {}

try:
    f = open(input(), "r")
    line = f.readline()
    while line:
        newLine = line.split()
        myDict[newLine[0]] = newLine[1]
        line = f.readline()
    f.close()

except OSError:
    print("File not found!")
    exit(0)

tab = 0

c = input("command: ")

while c != "checkout":

    cList = c.split()

    if cList[0] == "price":
        if cList[1] in myDict.keys():
            print(cList[1], "are $", myDict[cList[1]], " per pound")
        else:
            print("Error! ", cList[1], " not found!")

    if cList[0] == "add":
        if cList[3] in myDict.keys():
            tab = tab + float(cList[1])*float(myDict[cList[3]])
        else:
            print("Error! ", cList[3], " not found!")

    c = input("command: ")

print("total is $", tab)