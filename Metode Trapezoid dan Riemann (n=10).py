# Trapezoid
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x**2)*np.exp(-x)

a = 1.0
b = 10.0
n = 10

dx = (b-a)/(n-a)
x = np.linspace(a,b,n)

sigma = 0
for i in range (n-1):
    sigma = dx*func(x[i])
hasil = 0

for i in range (0-1):
    hasil += df*func(x[i])

xp = np.linspace(a,b)
plt.plot(xp,func(xp))
for i in range (n-1):
    plt.bar(x[i], func(x[i]), align = 'edge', width = 0.000001, color = 'red', edgecolor = 'yellow')

plt.fill_between(x, func(x), color= 'green')
plt.show()

# Riemann
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return (x**2)*np.exp(-x)
a = 1.0
b = 10.0
n = 10
# Riemann
x = np.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0
for i in range(n-1):
    hasil += dx*func(x[i])

xp =np.linspace(a,b)
plt.plot(xp,func(xp))
for i in range (n-1):
    plt.bar(x[i],func(x[i]), align = 'edge',width=dx, color = 'blue', edgecolor='black')
plt.show()
print (hasil)
