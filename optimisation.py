def saisir():
    pas = float(input("pas = "))
    while not(0.0000001 <= pas <=0.1):
        pas = float(input("pas = "))
    return pas

def calculer(pas):
    X = 0
    Vmax = 0
    V =  0
    while not(Vmax>V or X >= 5):
        X += pas
        V = 4*X*X*X-40*X*X+100*X
        if(Vmax < V):
            Vmax = V
            Xmax = X
    return Xmax 




#pp
pas = saisir()
Xapp = calculer(pas)
print(Xapp)
