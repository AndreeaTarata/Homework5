# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
#
# Exemplu:
# list1 = [1, 1, 2, 3]
#
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

def numerele(lista1, lista2):
    numerele = []
    for element in lista1:
        if element in lista2:
            numerele.append(element)
    return numerele
lista1 = [1, 2, 8]
lista2 = [1, 5, 7, 2, 8]
print(numerele(lista1, lista2))

# Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.

def reducere(cost, reducere):
    pret = cost - (cost*reducere)/100
    if pret > pret/2:
        return pret
    else:
        return 'Reducerea nu este valida'
print(reducere(100, 90))


# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

def datetime_Ro():
    import datetime
    datetime_Ro = datetime.datetime.now()
    return datetime_Ro
print(datetime_Ro().strftime("%m/%d/%Y %H:%M"))

def china_time():
    import datetime
    from pytz import timezone
    china_timezone = timezone('Asia/Shanghai')
    china_time = datetime.datetime.now(china_timezone)
    print("Data si ora din China sunt: ", china_time.strftime("%m/%d/%Y %H:%M"))

china_time()

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)

def zile_pana_la_ziua_mea(zi, luna, an):
    from datetime import date
    astazi = date.today()
    data_mea = date(an, luna, zi)
    diferenta = data_mea - astazi
    return diferenta.days
print(zile_pana_la_ziua_mea(28, 2, 2023))