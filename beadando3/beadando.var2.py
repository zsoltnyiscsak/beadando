
import itertools

muveletek = ('+','-','')
szamok = range(1,10)

for jel in itertools.product(muveletek,repeat=8):
    sor = "1"
    x = 0
    for i in range (8):
        sor+=jel[i]+str(i+2)

    try:
        if eval(sor) == 100:
            print(sor+"=100")

    except:
        continue
