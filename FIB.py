from timeit import timeit
from matplotlib import pyplot as plt

#fibonacci recursivo
def fibRec(n):
    if n < 2:
        return n
 
    else:
        return fibRec(n - 1) + fibRec (n - 2)

#fibonacci iterativo 
def fibIte(n):
    j = 1
    i = 0

    for _ in range(1, n + 1, 1):
        t = i + j
        i = j
        j = t

    return i



#criando uma lista de 1 a 41    
n = [ i for i in range(1,42,1)]
#calcula o tempo de fibonacci recursivo do número 1 a 41 e add a lista y1
y1 = [timeit(lambda: fibRec(i), number = 1)for i in range(1, 42, 1)]
#calcula o tempo de fibonacci iterativo do número 1 a 41 e add a lista y2
y2 = [timeit(lambda: fibIte(i), number = 1)for i in range(1, 42, 1)]

#imprime o gráfico
plt.xlabel('n')
plt.ylabel('segundos')
plt.plot(n, y1,  'go-')
plt.plot(n, y2, 'ro-')
plt.show()





