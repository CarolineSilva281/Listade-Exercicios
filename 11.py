# Exercicio 5: Pedir ao usuário a temperatura em graus Celsius
celsius= float(input("Digite a temperatura em graus celsius:"))
#Usar a fórmula de conversão: Celsius × 9 ÷ 5 + 32
fahrenheit = (celsius * 9 / 5) + 32
 #Mostrar a temperatura convertida para Fahrenheit
print(f"A temperatura de {celsius}°C em Fahrenheit é {fahrenheit:.2f}°F")