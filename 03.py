#Exercício 3: Divisão inteira e resto
# Pedir dois números ao usuário
numero1 = float(input('Digite um número para a divisão: '))
divisor = float(input('Digite o número para dividir: '))

# Divisão inteira e resto
divisaoInteira = numero1 // divisor
restoDivisao = numero1 % divisor

# Mostrar o resultado da divisão inteira (sem casas decimais)
print(f"A divisão inteira de {numero1} // {divisor} = {divisaoInteira}")

# Mostrar o resto da divisão entre os dois números
print(f"O resto da divisão de {numero1} por {divisor} é {restoDivisao}")