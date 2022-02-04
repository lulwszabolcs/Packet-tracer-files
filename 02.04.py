'''torpe = ["Tudor","Vidor","Morgó","Szundi","Szende","Hapci","Kuka"]
torpe.sort()
print(torpe)

torpe.sort(reverse=True)
print(torpe[2:])

nev = input("Írj be egy törpe nevet: ")
if nev in torpe:
    print("Benne van")
else:
    print("Nincs benne")

torpe.remove("Szende")
print(torpe)

szereplok = ["Hófehérke","Banya","Herceg"]

mese = szereplok.copy()
print(mese)

mese.extend(torpe)
print(mese)

#1
szinek = ["piros","kék","sárga","zöld","kék","fekete"]

#2
szin = input("Írj be egy színt: ")
if szin in szinek:
    print("Benne van")
else:
    print("Nincs benne")

#3
print("Ennyi van belőle: ",szinek.count(szin))
print("Indexe: ",szinek.index(szin))

#4
szinek.append(szin)
print(szinek)

#5
def sorba():
    szinek.sort()
sorba()
print(szinek)

def hossz_szerint(a):
    return len(a)

#szavak hossza szerint
szinek.sort(key=hossz_szerint)
print(szinek)

szavak = ["Takács","alma","körte","Ananász"]
szavak.sort()
print(szavak)
szavak.sort(key=str.lower)
print(szavak)
'''
#1
import random
lista = []
for i in range(15):
    x = random.randint(0, 100)
    lista.append(x)

print(lista[0:])

if szam%3==0 in lista:
    print("Benne van")
else:
    print("Nincs benne")