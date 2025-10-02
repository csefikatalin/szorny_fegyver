import random
hossz=30

def szorny():
    szorny=random.randint(1,3)
    if szorny==1:
        sz="boszorkany"
    elif szorny==2:
        sz="troll"
    else:
        sz="sarkany"
    return sz

def fegyver():
    print(f"{'='*hossz}")
    print(f"{'- valassz fegyvert! -':^{hossz}}")
    print(f"{'-'*hossz}")
    print(f"{'1 - íj'}")
    print(f"{'2 - kard'}")
    print(f"{'3 - varazspalca'}")
    print(f"{'='*(hossz)}")
    f=int(input("Írj be egy számot!: "))
    return f


    