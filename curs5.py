# def sign_up(name, email, pasword, is_registered = False, *home_details, **work_details):
#     print(work_details['Street'])
#     print(work_details['House_nr'])
#     print(work_details['City'])
#     if is_registered:
#         print('You already have an account')
#
#     else:
#         print('please enter name, email etc')
#         for h in home_details:
#             print(h)
#
#
#     print(name, email)
#     print(pasword, is_registered)
#
#
# def get_user(*address):
#     print(address[0])
#     for a in address:
#         print(a)
def get_max_score(students):
    max_g = 0
    students = [{ 'nume' : 'Ion', 'grade': 5}, { 'nume' : 'Maria', 'grade': 7}]
    for s in students:
        for n, g in s.items():
            if n == 'grade':
                print(n, g)
                if g > max_g:
                    max_g = g
    return(max_g)
print(get_max_score(''))

# TODO PRINTAM SI STUDENTUL CARE A LUAT MAX_GRADE
# TODO schimbam inca lista de dictionare sa fie transmisa din exterior - ca argument (sub main), (val reale ar fi argumente)

# ce trimiti din exterior este argument si ce def in campul functiei este parametru

# if __name__ == '__main__':
    # sign_up('Ion', 'ion@gmail.com', 'abcd', is_registered=True, Street='Rue de Paris', House_nr=20, City='Paris')
    # sign_up('Maria', 'maria@gmail.com', 'xyz', 'Calea Dorobanti', 70, 'Copsa mica', Street='Rue de Paris', House_nr=20, City='Paris')
    # get_user('Calea Constantei', 'g')
    # print('Hello', end = '***')
    # print('hello', 'World', 'Hello world John', sep = '@')
    # print('hello', 'World', 'Hello world John')


