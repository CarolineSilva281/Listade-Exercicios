#Exercício 10: Promoção infantil
# Pede a idade da criança
idade = int(input("Digite a idade da criança: "))

# Verifica se tem direito à entrada gratuita (até 12 anos)
if idade <= 12:
    #Mostrar mensagem informando se o ingresso é gratuito ou não
    print(" Ingresso gratuito. Promoção infantil aplicada.")
else:
    print(" Ingresso normal. Promoção não aplicável.")