"""
Operações aritiméticas

+ adição
- subtração
* multiplicação
/ divisão
** potencia
// divisão inteira
% resto

Ordem de procedencia

1º ()
2º **
3º * // / %
4º + -

"""
# Exemplos:

print(5 + 3 * 2) 
print(3 * 5 + 4 ** 2)
print(3 * (5 + 4) ** 2)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma vale {n1+n2}, a divisão é {n1/n2:.2f}, o produto é {n1*n2}!')
print(f'A divisão inteira é {n1//n2} e o resto é {n1%n2}!')

# # Desafio 005
num = int(input('Digite um número: '))
print(f'o seu antecessor é {num-1} e o seu sucessor é {num+1}!')

# Desafio 006
alg = int(input('Um valor: '))
print(f'Seu dobro é {alg*2} e sua raiz quadrada é {alg**2}!')

# Desafio 007
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
print(f'A média é {(nota_1 + nota_2)/2:.2f}!')

# Desafio 008
metros = float(input('Qual a meidade em metros: '))
print(f'Em centimetros fica {metros * 100:.2f}cm e me milimetos {metros * 1000:.2f}mm!')

