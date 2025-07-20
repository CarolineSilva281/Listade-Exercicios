#imc
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros (ex: 1.75) "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC
if imc < 18.5:
    print("Está abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Peso ideal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")