#Exercicio 2:Pedir ao usuário o valor de um produto
valorProduto= float(input("Digite o valor do produto:"))
#Calcular 10% de desconto sobre o valor.
desconto= valorProduto *0.10
#Subtrair o desconto do valor original
valorFinal= valorProduto - desconto
# Mostrar o valor final com desconto
print(f"10% de {valorProduto} é {valorFinal}")