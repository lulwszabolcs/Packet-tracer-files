'''
#7
x = int(input("x: "))
y = int(input("y: "))
for i in range(x,y+1):
    if i%8==0:
        break
    else:
        print(i)

#8
szam1 = int(input("1: "))
szam2 = int(input("2: "))
if szam1%2==0 and szam2%2==0:
    print("Mindkét szám páros")
elif szam1%2==0 or szam2%2==0:
    print("Csak az egyik")
else:
    print("Egyiksem")

#9
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if b<a and b<c:
    print(b,"vagyis a B legkisebb")
elif a<b and a<c:
    print(a,"vagyis az A a legkisebb")
else:
    print(c,"vagyis a C a legkisebb")

#9 másik megoldás
print(min(a,b,c))

#10
d = int(input("d: "))
for i in range(0,d+1):
    if i%3==0:
        print(i,end=' ')
'''
#11
szo1= input("szó: ")
szo2= input("szó: ")
if szo1 > szo2:
    print(szo2,szo1)
elif szo1 == szo2:
    print(szo1,"=",szo2)
else:
    print(szo1,szo2)