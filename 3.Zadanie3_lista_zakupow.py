
lista_zakupow = input("Proszę wpisać produkty do zapuku, oddzielając je przecinkiem: \n\n : ")

podzielona_lista_zak = lista_zakupow.split(",")

podzielona_lista_zak= list(map(lambda x: x.strip(), podzielona_lista_zak))

lista_zak_bez_powtorzen = list(set(podzielona_lista_zak))

produkt_cena_dict={}

for produkt in lista_zak_bez_powtorzen:
    komunikat="\n proszę podaj cenę dla produktu: {} : ".format(produkt)
    
    cena=input(komunikat)
    try:
        cena = float(cena)
    except ValueError:
        cena = 0
    if cena<0:
        cena = 0
    
    produkt_cena_dict[produkt.upper()] = cena

ceny_produktow = produkt_cena_dict.values()
do_zaplaty= sum(ceny_produktow)

if do_zaplaty>100:
    print("\n Niestey brakuje  Ci {} zł.".format(str(do_zaplaty-100)))
else:
    print("\n Wystarczy Ci na zakupy a nawet zostanie {} zł".format(str(abs(do_zaplaty-100))) )

