#Exercício 6: Verificador de maioridade
#Pedir a idade da pessoa
while True:
    idade = int(input('Digite sua idade: '))

    # Verificar se a idade é maior ou igual a 18
    if idade >= 18:
        print(f'Com {idade} anos pode dirigir')
    else:
        print(f'{idade} anos - Não pode dirigir')

    continuar = input("Quer testar outra idade? (s/n): ")
    if continuar.lower() != "s":
        break