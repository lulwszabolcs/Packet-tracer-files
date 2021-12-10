'''#12
nev = input("Írd be a neved: ")
kor = int(input("Írd be az életkorod: "))
while kor !=0:
    if kor > 18:
        print("Jó napot kívánok", nev + '!')
        kor = int(input("Írd be az életkorod: "))
    else:
        print("Hello", nev + '!')
        kor = int(input("Írd be az életkorod: "))

#13
osszeg = 0
for i in range(6):
    jegy = int(input("Jegy: "))
    if jegy < 1:
        print("Hibás szám")
        break
    elif jegy > 5:
        print("Hibás szám")
        break
    else:
        osszeg = jegy+osszeg
print("A 6 szám átlaga:",osszeg/6)
'''
#14
szam = int(input("Szám: "))
db = 0
for x in range(1,szam+1):
    if szam%x==0:
        db += 1
if db==2:
    print("prím")
else:
    print("Nem prím")



