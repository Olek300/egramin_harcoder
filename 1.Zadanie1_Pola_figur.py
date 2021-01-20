import math

jaka_figura = input("Wybierz figurę (wpisz: 1, 2 lub 3), której pole pragniesz obliczyć: \n\n 1. koło \n 2. trójkąt \n 3. prostokąt \n\n: ")
while jaka_figura not in ['1', '2', '3']:
    jaka_figura = input("Proszę wybrać z następujących opcji (wpisz: 1, 2 lub 3) : \n\n 1. koło \n 2. trójkąt \n 3. prostokąt \n\n:")

def chcek_input(x):
    if x.isalpha() or x.strip()=="":
        print(x + " to nie jest liczba\n")
        return True
    elif float(x)<=0:
        print("\n" + x + " podana wartość nie jest więkasza od 0\n")
        return True

def pole_kola():
    r=input("podaj promień koła r większy od 0 \n\n: ")
    if chcek_input(r):
        pole_kola()
    else:
        r=float(r)
        P=math.pi*r**2
        komunikat_koncowy= "Pole koła o podanych wartościach wynosi {}".format(str(P))
        print(komunikat_koncowy)
        return P

def pole_trojkata():
    a=input("podaj podstawę trójkąta a większą  od 0 \n\n: ")
    h=input("podaj wysokość trójkąta a większą  od 0 \n\n: ")
    
    if chcek_input(a) or chcek_input(h):
        pole_trojkata()
    else:
        a=float(a)
        h=float(h)
        P=0.5*a*h
        komunikat_koncowy= "Pole trójkąta o podanych wartościach wynosi {}".format(str(P))
        print(komunikat_koncowy)
        return P

def pole_prostokata():
    a=input("podaj bok prostokąta a większy od 0 \n\n: ")
    b=input("podaj bok prostokąta b większy od od 0 \n\n: ")
    if b.strip()=="":
        b=a
    if chcek_input(a) or chcek_input(b):
        pole_prostokata()
    else:
        a=float(a)
        b=float(b)
        P=a*b
        komunikat_koncowy= "Pole prostokąta o podanych wartościach wynosi {}".format(str(P))
        print(komunikat_koncowy)
        return P
           
if jaka_figura=='1':
    print("Dobry wybór. Będziemy obliczać pole koła.\n")
    pole_kola()
    

elif jaka_figura=='2':
    print("Dobry wybór. Będziemy obliczać pole trójkąta.\n")
    pole_trojkata()

elif jaka_figura=='3':
    print("Dobry wybór. Będziemy obliczać pole prostokąta.\n")
    pole_prostokata()
