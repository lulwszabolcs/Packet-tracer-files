'''class Diak():
    def __init__(self,vnev, knev, pont):
        self.pont = pont
        self.knev = knev
        self.vnev = vnev
    def __repr__(self):
        return f"Diák adatai: {self.knev} {self.vnev} {self.pont}"
    def vizsgal(self):
        if self.pont > 20:
            return "átment"
        else:
            return "megbukott"
diak1=Diak("Kurva","Anyá",34)
diak2=Diak("Nagy","Anna",11)
print(diak1.vnev,diak1.knev)
print(diak1,diak1.vizsgal())
print(diak2,diak2.vizsgal())


class Auto():
    def __init__(self,auto, evjarat):
        self.auto = auto
        self.evjarat = evjarat
    def veteran(self):
        if self.evjarat < 2000:
            return "veterán"
        else:
            return "nem veterán"
auto1=Auto("Fiat",2020)
auto2=Auto("Mercedes",2010)
print(auto1.veteran())
print(auto2.veteran())
print(auto2.evjarat)

nevek = ["Szabolcs","Lajos","Ágnes","József","Ferenc","DX"]
rovidnev = []
for i in nevek:
    if len(i)<5:
        rovidnev.append(i)
print(rovidnev)

f= open("diakosztalyzat.txt","r",encoding="UTF-8")
class Diak():
    def __init__(self,keresztnev,osztalyzat):
        self.osztalyzat = osztalyzat
        self.keresztnev = keresztnev
    def __repr__(self):
        return f"{self.keresztnev} {self.osztalyzat}"
    def atment(self):
        if self.osztalyzat==1:
            return "megbukott"
        else:
            return "átment"
jegyek = []
for sor in f:
    s = sor.strip().split()
    diak = Diak(s[0],int(s[1]))
    jegyek.append(diak)
for i in jegyek:
    print(i,i.atment())
'''
class Ajandek():
    def __init__(self,mit, ar):
        self.mit = mit
        self.ar = ar
    def __repr__(self):
        return f"{self.mit} {self.ar}"

f = open("ajandek.txt",encoding="UTF-8")
lista = []
for sor in f:
    sor = sor.strip().split(";")
    aj = Ajandek(sor[0],int(sor[1]))
    lista.append(aj)
print(lista)
for i in lista:
    print(i)


