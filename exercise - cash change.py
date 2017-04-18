#the less coins we give back the better
monety = [5,2,1,0.5,0.2,0.1]
wydac = [0,0,0,0,0,0]
banknot = 20
zakupy = 8.30
reszta = banknot - zakupy

for indeks,moneta in enumerate(monety):
    if reszta >= moneta:
        ilosc = reszta // moneta
        wartosc = ilosc * moneta
        reszta = reszta - wartosc

        wydac[indeks] = ilosc

print(wydac)

print("Wydac: ")
for (moneta,ilosc) in zip(monety,wydac):
    print(moneta,'-',ilosc)