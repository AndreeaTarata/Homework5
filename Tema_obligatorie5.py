# 1.Funcție care să calculeze și să returneze suma a două numere

# def suma(a, b):
#     x = a + b
#     print(x)
#
# suma(5, 7)
# suma(70, 10)

# def suma(a, b):
#     x =  a + b
#     return x
# rezultat = suma(5,7)
# print(rezultat)
# rezultat = suma(25,17)
# print(rezultat)


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

# def numar(x):
#     if x % 2 == 1:
#         return 'numar impar'
#     else:
#         return 'numar par'
# raspuns = numar(5)
# print(raspuns)

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

# def caractere():
#     nume = 'Tarata'
#     prenume = 'Andreea'
#     mijlociu = 'Brindusa'
#
#
#     print(len(nume) + len(prenume) + len(mijlociu))
# caractere()

# 4. Funcție care returnează aria dreptunghiului

# def aria_dreptunghi(l, L):
#     print(l * L)
# aria_dreptunghi(5, 10)

# 5. Funcție care returnează aria cercului

# def aria_cerc(r):
#     print(r*r)
# aria_cerc(5)

# def aria_cerc(r):
#     return r*r
#
# rezultatul = aria_cerc(5)
# print(rezultatul)

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

# def caracter(x):
#     if x in 'amazonx':
#         return 'True'
#     else:
#         return 'false'
#
# returneaza = caracter('x')
# print(returneaza)

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
#
# def numara(numele):

#     count = 0
#     for litera in numele:
#         if litera.isupper():
#             count += 1
#
#     print(f'Nr de caractere lower case este {count}')
#
#     count_mic = 0
#     for x in numele:
#         if x.islower():
#             count_mic += 1
#     print(f'Nr de caractere lower case este {count_mic}')
#
# numara('AnDgj')

#8 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

# def positive_numbers(*numere):
#     positive_nr = []
#     for n in numere:
#         if n > 0:
#             positive_nr.append(n)
#     return positive_nr
#
# print(positive_numbers(1, -5, 7))

# 9 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

# def numere(x, y):
#     if x > y:
#         print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
#     elif y > x:
#         print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
#     else:
#         print('numerele sunt egale')
#
# numere(17, 7)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False



def adauga_numar(n, set_nr):
  if n in set_nr:
    print('nu am adaugat numărul în set. Acesta există deja')
    return False
  else:
    set_nr.add(n)
    print('am adaugat numărul nou în set')
    return True
set_nr = {1, 2, 3}
print(adauga_numar(3, set_nr)) # False
# print(adauga_numar(7, set_nr)) # True
print(set_nr)