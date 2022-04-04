def saisir():
    pas = float(input("pas = "))
    while not(0.0000001 <= pas <=0.1):
        pas = float(input("pas = "))
    return pas

def calculer(pas):
    X = 0
    S = 0
    while not(S>=1):
        X += pas
        S = (-2/3) * X * X + 2 * X
        print(S)
    if(S>1):
        X = X - pas
    return X




#pp
pas = saisir()
Xapp = calculer(pas)
print(Xapp)