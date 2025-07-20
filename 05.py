#Exercício 5: Conversor de temperatura
# Pede ao usuário a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Aplica a fórmula de conversão para Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Mostra o resultado convertido
print(f"{celsius}°C equivale a {fahrenheit}°F")
