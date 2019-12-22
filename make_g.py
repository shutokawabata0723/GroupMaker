#coding:utf-8
GREEN = '\033[92m'
ENDC = '\033[0m'
import random

# create member list 
a = open("members.txt","r")
members = []
for i in a:
    members.append(i.rstrip())
a.close()
# shuffle order of members
random.shuffle(members)

# input split number of the group
while (True):
    try:
        splitNum = int(input("how many groups you want?: "))
    except ValueError:
        print ("the input contains characters not only number. try again...")
        continue

    if splitNum <= len(members):
        break
    else:
        print ("the split number is more than members. try again...")
        continue

# split members to each group
gnum = 0
gnum_member = {}
for psn in members:
    gnum += 1
    gnum_member.setdefault(gnum, []).append(psn)
    if gnum >= splitNum:
        gnum = 0

# show each group member
for psn in gnum_member:
    print(GREEN, psn, ENDC, gnum_member[psn])