import random
'''#1
lista = []
for i in range(50):
    x = random.randint(0,100)
    lista.append(x)
print(lista)
#2
lista[4] = lista[46]
print(lista)
#3
print(lista[-25:])
#4
db = lista.count(0)
print(db)
#5
gyumolcs = input("Írj be 5 gyümölcsöt: ")
print("alma" in gyumolcs)
'''
#6
tantargyak = ["angol","tesi","matek","töri","biosz"]
for i in tantargyak:
    print(i)

for index in range(len(tantargyak)):
    print(index, tantargyak[index])

print()

for index, tantargy in enumerate(tantargyak):
    print(index,tantargy)

print()

tantargyak.sort() #tantargyak.sort(reverse=True)
print(tantargyak)
tantargyak.reverse()
print(tantargyak)

y = tantargyak.count("matek")
print(y)
z = tantargyak.index("biosz")
print("Biosz indexe: ",z)

print()
tantargyak.append("magyar")
print(tantargyak)
tantargyak.insert(0,"eor")
print(tantargyak)


hobbi = ["krunker","kódolás","hálózat","App Inventor"]
tantargyak.extend(hobbi)
print(tantargyak)
uj = hobbi.copy()
uj.pop(3)
print(uj)
uj.remove("kódolás")
print(uj)







