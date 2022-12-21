Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... def func(x):
...     return(x**2)*np.exp(-x)
... a = 1.0
... b = 10.0
... n = 10
... 
... #Trapezoid
... dx = (b-a)/(n-1)
... x = np.linspace(a,b,n)
... sigma = 0
... for i in range(1, n-1):
...  sigma += func(x[i])
... hasil = 0.5*dx*(func(x[0])+2*sigma+func(x[-1]))
... print (hasil)
... 
... xp = np.linspace(a,b)
... plt.plot(xp,func(xp))
... 
... for i in range (n):
...     plt.bar(x[i],func(x[i]),align = 'edge',width = 0.000001, color = 'gray', edgecolor = 'red')
... 
... plt.fill_between(x,func(x),color='yellow')
... 
... plt.show()
... 
... #Reiman
... x = np.linspace(a,b,n)
... dx = (x[-1]-x[0])/(n-1)
... 
... hasil = 0
... for i in range(n-1):
...     hasil += dx*func(x[i])
... 
... xp = np.linspace(a,b)
... plt.plot(xp,func(xp))
for i in range (n-1):
    plt.bar(x[i],func(x[i]), align = 'edge', width=dx, color = 'red', edgecolor='black')
plt.show()

print(hasil)
