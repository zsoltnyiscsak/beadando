import numpy as np

db = 0
ls = []
s = input()                               #1 standard bemenetről olvas be
lst = s.split(',')                        #2 vesszők szerint elválasztjuk a számokat + a split miatt egy listába tesszük őket, mert a split mindig listát hoz létre.
for sz in lst:                            #3 végigmegyünk a listában levő "sztringeken"
    x = int(sz, 2)                        #4 az "sz" stringet x-ként alakítjuk át 10-es számrendszerbeli alakká.

    if x %3 == 0:                         #5 megnézzük, hogy az x számok közül van e, ami 3-mal osztható.
        ls.append([x,int(sz)])            #6 (ls létrehozva) amennyiben osztható 3-mal, hozzáadjuk a listához. (vektorhoz nem tudunk hozzáadni)
        db += 1                           #7 megszámoljuk a hozzáadott számokat.

m = np.random.randint(1,2,(2,db))         #8 létrehozunk egy kétdimenziós vektort.
for i in range(db):
    m[i,0] = ls[i][0]                     #10 felülírjuk a vektor elemeit (step1)
    m[i,1] = ls[i][1]                     #10 felülírjuk a vektor elemeit (step2)
print(m)
