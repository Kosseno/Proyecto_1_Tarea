from triangulo import triangulorectangulo

def main():
    try:
        altura = float(input("Ingrese el altura del triangulo :"))
        base = float(input("Ingrese la base del triangulo :"))

        triang = triangulorectangulo(base, altura)
        triang.resultados()

    except ValueError as e:
        print("Error de entrada :", e)
    except Exception:
        print("Errorr ocurrio algo inesperado")

# ------ Programa Principal -----
if __name__ == "__main__":
    main()