def solve(n):
    array=[]
    for i in range(n*n):
        array.append(input().split())
    isMatch = "false"
    for dd in array:
        for hh in dd:
            if 0<int(hh)<10:
                continue
            else:
                isMatch = "true"
    for f in range(n*n):
        hbox = []
        vbox = []
        array2d = []
        for h in range(n*n):
            hbox.append(array[f][h])
            vbox.append(array[h][f])
        for g in range(n*n):
            ctl=vbox.count(vbox[g])
            ctl2 = hbox.count(hbox[g])
            if ctl!=1 or ctl2!=1:
                isMatch="true"
                break
        vbox.clear()
        hbox.clear()
        if ctl!=1 or ctl2!=1:
            break
    for v in range(n):
        for k in range(n):

            for m in range(n):

                for t in range(n):
                    array2d.append(array[m+(k*n)][t+(k*n)])
            for kk in range(n*n):
                ctl3 = array2d.count(array2d[kk])
                if ctl3!=1:
                    isMatch="true"
                    break
            array2d.clear()

    if isMatch=="false":
        return "Yes"
    else:
        return "No"

t = int(input())
c=0
while(t>0):
    c+=1
    n = int(input())
    print(f"Case # {c} : {solve(int(n))}")
    t-=1
