import allTheFuctions
#budcalc = allTheFuctions.avgTHC(thcBud=0.22,thcWeight=0.5,cbdWeight=0.5, cbdBud=0.1)
#test = allTheFuctions.f(2)
def f(n, delta):
    n += delta - 1
    n += ((1-n)/9)*9
    print(n % 9 + 1)
    pass
for i in range(1,127):
    for x in range(1,10):
        print(i,x)
        test = f(i,x)
        
