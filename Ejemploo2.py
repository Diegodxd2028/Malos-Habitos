def multiplicacion(multiplicando, multiplicador):
    producto = multiplicando * multiplicador
    return producto

def suma(producto, c):
    sumatoria = producto + sumando
    return sumatoria

if __name__=="__main__":
    multiplicando = float(input("Ingresar multiplicando: "))
    multiplicador = float(input("Ingresar multiplicador: "))
    sumando = float(input("Ingresar sumando: "))
    multiplica = multiplicacion(multiplicando, multiplicador)
    sumatotal = suma(multiplica, sumando)
    print(f"{multiplicando} * {multiplicador} + {sumando} = {sumatotal}")