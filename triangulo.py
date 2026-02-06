import math

class triangulorectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base o altura deben ser mayor a cero.")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_hipotenusa(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))
    
    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()
    
    def resultados(self):
        print("\nResultados :")
        print("Area :", self.calcular_area())
        print("Hipotenusa :", self.calcular_hipotenusa())
        print("Perimetro :", self.calcular_perimetro())