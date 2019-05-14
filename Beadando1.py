#Írj egy programot, ami nulla végjelig szavakat kér a standard bemenetből. A szavakat
#gyűjtse össze egy listába. Ha egy szót másodjára is megkap, akkor kérjen egy másik
#szót helyette. Majd rendezd a szavakat betűrendbe az első karakterük alapján. Az azonos
#első karakterrel rendelkező szavak sorrendjéről a szavak hossza (hány karakterből áll)
#döntsön úgy, hogy először a hosszabb majd a rövidebb szavak következzenek. Ha
#vannak azonos karakterrel kezdődő és azonos hosszúságú szavak, akkor az álljon
#előrébb, amit később kapott meg bemenetként. Végül a program írja ki az eredeti és a
#rendezett listáját is a szavaknak.
#16

def rendez(lst):
    l = lst.copy()
    for i in range(0,len(lst)-1):       # 2 ciklus egymásban, azért
        minimum = i
        for j in range(i,len(lst)):
            if lst[j][0] < lst[minimum][0]:
                minimum = j
            elif lst[j][0] == lst[minimum][0]:
                if len(lst[j]) > len(lst[minimum]):
                    minimum = j
                elif len(lst[j]) == len(lst[minimum]):
                    if l.index(lst[j]) > l.index(lst[minimum]):
                        minimum = j
        lst[i],lst[minimum] = lst[minimum],lst[i]
    return lst

ls = []

while True:
    sz = input()
    if sz == "0":
        break
    ls.append(sz)

print(rendez(ls))
