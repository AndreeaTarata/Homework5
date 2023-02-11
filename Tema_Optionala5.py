# 1. Funcție care primește o lună din an și returnează câte zile are acea luna

def numar_zile_luna(luna):
    if luna.lower() == "ianuarie":
        return 31
    elif luna.lower() == "februarie":
        return 28
    elif luna.lower() == "martie":
        return 31
    elif luna.lower() == "aprilie":
        return 30
    elif luna.lower() == "mai":
        return 31
    elif luna.lower() == "iunie":
        return 30
    elif luna.lower() == "iulie":
        return 31
    elif luna.lower() == "august":
        return 31
    elif luna.lower() == "septembrie":
        return 30
    elif luna.lower() == "octombrie":
        return 31
    elif luna.lower() == "noiembrie":
        return 30
    elif luna.lower() == "decembrie":
        return 31
    else:
        return "introduceti o luna"
print(numar_zile_luna('ianuarie'))

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
#
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)


def calculator(numar1, numar2):
    suma = numar1 + numar2
    diferenta = numar1 - numar2
    inmultirea = numar1 * numar2
    impartirea = numar1 / numar2

    return suma, diferenta, inmultirea, impartirea

a, b, c, d = calculator(10, 2)

print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def count_occurances(list):
    occurances = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
    }

    for num in list:
        occurances[num] += 1

    return occurances


list = [1, 3, 1, 5, 9, 7, 7, 5, 5]

print(count_occurances(list))

# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele

def val_max(a, b, c):
    val_max = max(a, b, c)
    return val_max
print(val_max(-25, 5 ,15))

# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def suma_numerelor(numar):
    suma = 0
    for i in range(numar+1):
        suma += i
    return suma
print(suma_numerelor(3))
