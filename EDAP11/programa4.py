#Estrategia descendente o top-down
#guardar los resultados previamente calculados, haciendo
# que no se tengan que volver a hacer las operaciones

memoria = {1:1, 2:1, 3:2}

def fibo(numero):
    a = 1
    b = 1
    for i in range(1, numero-1)
        a, b=b, a+b
    return b

def fibo_top_down(numero):
    if numero in memoria:
        return memoria[numero]
    f = fibo(numero-1) + fibo(numero-2)
    memoria[numero] = f
    return memoria[numero]

print(fibo_top_down(5))
print(memoria)

print(fibo_top_down(4))
print(memoria)


