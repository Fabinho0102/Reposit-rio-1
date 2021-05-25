a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))

operacao = input("+: Soma\n-: Subtração\n*: Multiplicação\n/: Divisão")
if operacao == '+':
    resultado == a + b
elif operacao =='-':
    resultado == a - b
elif operacao == '*':
    resultado == a * b
else:
    resultado == a // b 

print(resultado)