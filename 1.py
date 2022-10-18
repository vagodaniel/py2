"""
szam=int(input("kerek egy szamot:):"))
from operator import truediv
import random
veltipp=random.randint(1,100)
lepes=0
talalt=False
while talalt==False:
    if szam==veltipp:
        lepes+=1
        print(f"{lepes}-bol talaltad ki")
        talalt=True
    elif szam>veltipp:
        lepes+=1
        veltipp=random.randint(1,szam)
    elif szam<veltipp:
        lepes+=1
        veltipp=random.randint(szam,100)
    else:
        print("nrm nyert")
"""
"""
a=int(input("egyszam:"))
b=int(input("masikszam:"))

#a+(b*2)

print(f"{a+(b*2)}")

"""

"""
a=int(input("szam:"))
db=0
while a!=0:
    if a>5:
        db+=1
    a=int(input("add meg a szamot"))
print(f"no: {db}")
"""
"""
a=int(input("egy szam:"))
db=0
while a!=0 and a>=0:
    if a>0:
        db+=1
    a=int(input("egy szam:"))
print(f"atlag:{}")
"""
"""
a=int(input("egy szam:"))
db=0
while a!=-5 and a>=-5:
    if a>10:
        db+=1
    a=int(input("egy szam:"))
    if a!=-5 and a<=10:
        db+=0
    a=int(input("egy szam:"))
print(f"10 fok felett=:{db}")
"""
"""
a=int(input("egy szam:"))
paros=0
paratlan=0
while a!=0 and a>=0:
    if a%2:
        paros+=1
    a=int(input("egy szam:"))
    if a%2==1:
        paratlan+=1
    a=int(input("egy szam:"))
print(f"paratlan: {paratlan}, paros: {paros}")
"""


"""

n=int(input("adj egy szamot"))
m=int(input("masik szam:"))
i=1
while i<n:
    j=1
    while j<=m:
        print(f"{i*j}", end="\t")
        j+=1
    print()
    i+=1
"""