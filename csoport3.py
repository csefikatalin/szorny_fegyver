import random
hossz=30
def szorny():
    szorny=random.randint(1,3)
    if szorny==1:
        sz="boszorkány"
    elif szorny==2:
        sz="troll"
    else:
        sz="sárkány"
    return sz

def fegyver():
    print(f"{'═'*(hossz)}")
    print(f"{'- Válassz fegyvert! -':^{hossz}}")
    print(f"{'-'*(hossz)}")
    print(f"{'1 - íj'}")
    print(f"{'2 - kard'}")
    print(f"{'3 - varázspálca'}")  
    print(f"{'═'*(hossz)}")
    f=int(input("Írj be egy számot: "))
    return f



    