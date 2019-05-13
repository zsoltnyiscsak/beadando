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
