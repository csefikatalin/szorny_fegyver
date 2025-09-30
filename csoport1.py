hossz = 30

def tul_lap(nev:str,pont:int):
    
    print(f"╔{'═'*(hossz)}╗")
    print(f"║{'★ JÁTÉKOS ADATLAP ★':^{hossz}}║")
    print(f"║{'-'*(hossz)}║")
    print(f"║     név: {nev:<{hossz-11}} ║")
    print(f"║ életerő: {pont:<{hossz-11}} ║")
    print(f"╚{'═'*(hossz)}╝")
    input("tovább....")