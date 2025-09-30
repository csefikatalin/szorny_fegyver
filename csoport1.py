hossz = 30

def tul_lap(nev:str,pont:int):
    
    print(f"{'═'*(hossz)}")
    print(f"{'- JÁTÉKOS ADATLAP -':^{hossz}}")
    print(f"{'-'*(hossz)}")
    print(f" név: {nev} ")
    print(f" életerő: {pont} ")
    print(f"{'═'*(hossz)}")
    input("tovább....")

def harc_eredmeny(fegyver:int,szorny:int):
    if fegyver==szorny:
        eredmeny="nyertél"
    else:
        eredmeny="vesztettél"
    return eredmeny