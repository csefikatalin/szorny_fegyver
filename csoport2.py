hossz:int=30

def harc_eredmeny_kiir(fegyver:str, szorny:str, eredmeny:str):
    print(f"{'='*{hossz}}")
    print(f"{'A HARC EREDMÉNYE' :^{hossz}}")
    print(f"{'-'*{hossz}}")
    print(f"{'A '+ szorny + ' ellen harcoltál' :^{hossz}}")
    print(f"{'-'*{hossz}}")
    print(f"{'A fegyvered '+ fegyver :^{hossz}}")
    print(f"{'-'*{hossz}}")
    print(f"{eredmeny.upper():^{hossz}}")
    print(f"{'='*{hossz}}")

def fegyvernev(f):
    if f == 1:
        fegyver="íj"
    elif f == 2:
        fegyver ="kard"
    else:
        fegyver ="varázspálca"
    return fegyver