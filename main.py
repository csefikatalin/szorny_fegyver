import csoport1, csoport2, csoport3

def jatek(nev, pont):
    print("\033c")
    csoport1.tul_lap(nev, pont)
    sz=csoport3.szorny()
    f=csoport3.fegyver()
    e=csoport1.harc_eredmeny(f, sz)
    fegyver=csoport2.fegyvernev(f)
    csoport2.harc_eredmeny_kiir(fegyver, e, sz)
    if e== "nyertél":
        pont+=1
    else:
        pont-=2
    csoport1.tul_lap(nev, pont)
print("\033c")
nev=input("A neved🐒:    ")
pont= 5
jatek(nev, pont)
jatek(nev, pont)
jatek(nev, pont)