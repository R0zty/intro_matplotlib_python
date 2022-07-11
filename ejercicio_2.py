# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico

def multi_line_1():
 x = list(np.linspace(-4, 4, 20))
 y1 = [] 
 for i in x:
    y1.append(i**2)
 fig = plt.figure()
 fig.suptitle('Grafico Multiples lineas')
 ax = fig.add_subplot()


 ax.plot(x, np.sin(x), color ='b', marker = '<', label = 'y1=sin(x)')
 ax.plot(x, 2*np.sin(x), color = 'r', marker = 'o', label = 'y1=2*sin(x)')
 ax.plot(x, 3*np.sin(x), color = 'm', marker = 'v', label = 'y1=3*sin(x)')
 ax.plot(x, 4*np.sin(x), color = 'c', marker = ',', label = 'y1=4*sin(x)')

 ax.legend()
 ax.grid()
 ax.set_facecolor('whitesmoke')
 plt.show(block=False)




def multi_line_2():
 x = list(np.linspace(-4, 4, 20))
 y2 = []
 for i in x:
  y2.append(i**3)

 fig = plt.figure()
 fig.suptitle('Grafico Multiples lineas')
 ax = fig.add_subplot()
 ax.plot(x, np.sin(x), color = 'blue', marker = '<', label = 'y2=sin(x)')
 ax.plot(x, 2*np.sin(x), color = 'green', marker = '>', label = 'y2=2*sin(x)')
 ax.plot(x, 3*np.sin(x), color = 'c', marker = 'o', label = 'y2=3*sin(x)')
 ax.plot(x, 4*np.sin(x), color = 'k', marker = ',', label = 'y2=4*sin(x)')
 ax.legend()
 ax.grid()
 ax.set_facecolor('whitesmoke')
 plt.show()

 plt.show(block=False)




if __name__ == '__main__':
    multi_line_1()
    multi_line_2()



print("terminamos")
