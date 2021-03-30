from timeit import timeit
from matplotlib import pyplot as plt


def fibRec(n):
    if n < 2:
        return n
 
    else:
        return fibRec(n - 1) + fibRec (n - 2)

def fibIte(n):
    j = 1
    i = 0

    for _ in range(1, n + 1, 1):
        t = i + j
        i = j
        j = t

    return i



    
n = [ i for i in range(1,42,1)]
y1 = [timeit(lambda: fibRec(i), number = 1)for i in range(1, 42, 1)]
y2 = [timeit(lambda: fibIte(i), number = 1)for i in range(1, 42, 1)]


plt.plot(n, y1, n, y2)
plt.show()





