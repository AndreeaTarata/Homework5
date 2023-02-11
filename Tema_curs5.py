def get_max_score(students):
    max_g = 0
    students = [{ 'nume' : 'Ion', 'grade': 5}, { 'nume' : 'Maria', 'grade': 7}]
    for s in students:

        for n, g in s.items():
            if n == 'grade':
 #               print(n, g)
                if g > max_g:
                    max_g = g
        # for a, b in s.items():
        #     if a == 'nume':
        #         print(a, b)
        print(s)

    return(max_g)
print(get_max_score(''))

# TODO PRINTAM SI STUDENTUL CARE A LUAT MAX_GRADE
# TODO schimbam inca lista de dictionare sa fie transmisa din exterior - ca argument (sub main), (val reale ar fi argumente)

def nota_maxima(elevi):
  nota_max = 0
  student_max = ""
  for student, nota in elevi.items():
    if nota > nota_max:
      nota_max = nota
      student_max = student
  return student_max, nota

elevi = {
  'John': 8.5,
  'Eric': 7.1,
  'Adam': 9.0
}

print(nota_maxima(elevi))