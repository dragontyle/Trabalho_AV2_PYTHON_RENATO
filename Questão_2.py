def soma_imposto(taxa_imposto, custo):
    taxa = (custo*taxa_imposto)/100
    return custo + taxa


imposto = int(input("Digite a taxa de imposto sobre o produto: "))
valor = float(input("Digite o valor do produto: "))
print(f"O custo do meu produto é de R${soma_imposto(imposto, valor)}")
