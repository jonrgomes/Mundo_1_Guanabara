"""
Tipos primitivos
int = 7, -4, 0, 0875
float = 2.4, 0.076, -15.223, 7.0
bool = True ou false
str = '7'
Class type nos da o tipo primitivo da variável

"""
# int
n_1 = int(input('Digite um número: '))
print(type(n_1))
n_2 = int(input('Digite outro número: '))
s = n_1 + n_2
print(f'A soma entre {n_1} e {n_2} é {s}!') 

# float
n = float(input('Digite um valor: '))
print(n)

# bool
b = bool(input('Digite um valor: '))
print(b)

# Desafio_003
a = int(input('Um número: '))
b = int(input('Outro número: '))
c = a + b
print(f'A soma de {a} e {b} é {c}!')

# Desafio_004
d = input('Digite algo: ')
print(d.isalnum())
print('É numérico?', d.isnumeric())
print('É Alfanumerico?', d.isalpha())
print('Está em minúsculas?', d.islower())
print('Está em maiúsculas?', d.isupper())