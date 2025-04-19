print('-'*20)

print('Escolha um número : ')
valor1 = float(input('Número = '))

print('Outro número : ')
valor2 = float(input('Número = '))

print('''Que tipo de operação deseja fazer?
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Divisão
[ 4 ] Multiplicação
''')
opcao = int(input('Escolha : '))

def calcular (opcao , valor1 , valor2):
	match opcao:
		case 1 :
			return valor1 + valor2
		case 2 :
			return valor1 - valor2
		case 3 :
			return valor1 / valor2
		case 4:
			return valor1 * valor2
		case _:
			return 'Opção inválida'
		
resultado = calcular(opcao , valor1 ,valor2)
print(f'Resultado: {resultado}')
