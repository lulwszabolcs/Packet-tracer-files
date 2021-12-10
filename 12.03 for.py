
#1
for i in range(10,22):
    print(i,end=' ')

#2
szam = int(input("Írj be egy számot!:"))
osszeg = 0
while szam != 0:
    osszeg += szam
    szam = int(input("Mégegyszer: "))
if szam == 0:
    print(osszeg)


#3
szo = input("Írj be egy szót: ")
for i in szo:
    print(i)

#4
irj = input("Írj be egy szót vagy mondatot!: ")
print(irj.replace(" ",""))

#5
ot = int(input("Írj be egy 5-tel osztható számot: "))
while ot%5!=0:
    ot = int(input("Írj be egy 5-tel osztható számot: "))
    if ot%5==0:
        print("Vége")

#6
txt = input("Írj be egy szót: ")
for i2 in txt:
    print(i2)
    if i2=="t":
        break

