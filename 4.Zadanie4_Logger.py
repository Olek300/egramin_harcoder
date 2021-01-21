import time
import random
podana_liczba_sekund = input("Podaj proszę przez ile sekund ma działać program: \n\n: ")

def chcek_input(x):
    if x.isalpha() or x.strip()=="":
        print(x + " to nie jest liczba\n")
        return True
    elif float(x)<=0:
        print("\n" + x + " podana wartość nie jest więkasza od 0\n")
        return True
    
while chcek_input(podana_liczba_sekund):
    podana_liczba_sekund = input("Podaj proszę przez ile sekund ma działać program: \n\n: ")

podana_liczba_sekund=int(podana_liczba_sekund)

for i in range(podana_liczba_sekund):
    now = time.localtime()
    N = i
    N = "0" * (len(str(podana_liczba_sekund))- len(str(i))) +str(N)       #dodaj zera przed kolejne N tak by log był wyrównany przy większych liczbach
    R = random.random()
    DD = time.strftime('%d', now)
    DD = "{:02d}".format(int(DD))
    Mon = time.strftime("%b", now)
    YYYY = time.strftime('%Y', now)
    hhmmss= time.strftime('%H:%M:%S ', now)
    timestamp= int(time.time())
    

    with open("logs.txt", "a") as file:
        value= "{} | {} {} {} | {} | {} | {}".format(N, DD, Mon, YYYY, hhmmss, timestamp, R)
        file.write(value  + "\n")
    print(i)
    time.sleep(1)
