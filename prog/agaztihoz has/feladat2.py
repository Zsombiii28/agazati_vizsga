import datetime

def number_input(szoveg,maximum):
    szam=0
    while szam<=0 or szam>maximum:
        try:
            szam=int(input(szoveg))
        except:
            print('Nem megfeleő szám!')
    return szam

def eltelt_napok_szama(ev,honap,nap,ev2,honap2,nap2):
    date1=datetime.date(ev,honap,nap)
    date2=datetime.date(ev2,honap2,nap2)
    diff=date2-date1
    return diff

ev=number_input('Kérem az első dátum évét: ',2024)
honap=number_input('Kérem az első dátum hónapját: ',12)
nap=number_input('Kérem az első dátum napját: ',31)

ev2=number_input('Kérem az második dátum évét: ',2024)
honap2=number_input('Kérem az második dátum hónapját: ',12)
nap2=number_input('Kérem az második dátum napját: ',31)

print(f'{ev}.{honap}.{nap} és {ev2}.{honap2}.{nap2} között {eltelt_napok_szama(ev,honap,nap,ev2,honap2,nap2).days} nap volt.')