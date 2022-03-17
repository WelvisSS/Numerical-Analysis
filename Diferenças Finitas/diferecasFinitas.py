from lu import lu
def diferencasFinitas(h, P, DeltX, x0, xl, Ta):
  B = []
  m = []
  it = 0
  for i in range(P-1):
    m.append([])
    for j in range(P-1):
      it += 1
      if i == 0 and j == 0: 
        m[i].append(2+h*DeltX**2)
        continue
      if i == 0 and j == 1:
        m[i].append(-1)
        continue
      
      if i == P-2 and j == P-2:
        m[i].append(2+h*DeltX**2)
        m[i][j-1] = -1
        continue
      m[i].append(0)

  for i in range(P-2):
    for j in range(P-2):
      it += 1
      if i != 0 and j != 0 and i == j:
        m[i][j-1] = -1
        m[i][j] = 2+h*DeltX**2
        m[i][j+1] = -1

  B.append(h*(DeltX**2)*Ta+x0)
  for j in range(P-3): B.append(h*(DeltX**2)*Ta)
  B.append(h*(DeltX**2)*Ta+xl)

  R = lu(len(m), m, B)
  T = [x0]
  for r in R: T.append(r)
  T.append(xl)
  file_out.write("Resultado = {}\nIterações = {}\n\n" .format(T, it))

file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')

while(True):
  h = float(file_in.readline()) 
  L = float(file_in.readline()) # Último ponto de x
  P = int(file_in.readline()) # Número de pontos
  x0 = float(file_in.readline()) 
  xl = float(file_in.readline())
  Ta = float(file_in.readline())
  diferencasFinitas(h, P, L/P, x0, xl, Ta)
  if(file_in.readline() == ""): break