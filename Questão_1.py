def area(bmaior, bmenor, altura):
    return ((bmaior+bmenor)*altura)/2


base_maior = int(input("Informe a base maior: "))
base_menor = int(input("Informe a base menor: "))
altura = int(input("informe a altura: "))


print(f"a area do trapézio é {area(base_maior, base_menor, altura)}")
