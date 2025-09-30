

import csoport1, csoport2, csoport3,csoport4 

def jatek(nev, pont):
    print("\033c")
    csoport1.tul_lap(nev,pont)
    sz=csoport4.szorny()
    f=csoport4.fegyver()
    e=csoport3.harc_eredmeny(f,sz)
    if f==1:
        fegyver="íj"
    elif f==2:
        fegyver="kard"
    else:
        fegyver="varázspálca"
    csoport2.harc_eredmeny_kiir(fegyver,sz,e)
    if e=="nyertél":
        pont+=1
    else:
        pont-=2
    csoport1.tul_lap(nev,pont)



print("\033c")
nev=input("A neved 🧝‍♀️:  ")
pont=5



jatek(nev, pont)
jatek(nev, pont)
jatek(nev, pont)




