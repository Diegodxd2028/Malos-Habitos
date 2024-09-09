# Función para calcular el área de un rectángulo
def area_rectangulo(largo, ancho):
    result = largo * ancho
    return result

# Función para calcular el área de un triángulo
def area_triangulo(base, altura):
    r = 0.5 * base * altura
    return r

# Función principal
if __name__ == "__main__":
    largo = float(input("Ingresar largo del rectángulo: "))
    ancho = float(input("Ingresar ancho del rectángulo: "))
    base = float(input("Ingresar base del triángulo: "))
    altura = float(input("Ingresar altura del triángulo: "))
    rect_area = area_rectangulo(largo, ancho)
    tri_area = area_triangulo(base, altura)
    print("Área del rectángulo:", rect_area)
    print("Área del triángulo:", tri_area)