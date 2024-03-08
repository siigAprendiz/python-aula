# Exemplo de comentário de 1
# Exemplo de outro comentário

"""
exemplo
de comentário
com múltiplas linhas
"""

a = 15              # a variável a recebe o valor 15
b = 30              # a variável b recebe o valor 30
c = a + b           # a variável c recebe o resultado da soma de a + b
print(c)            # exibe o valor da variável c

# GERAÇÃO DE ENTRADA DE DADOS (input)
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

# OPERAÇÃO DE SAÍDA DE DADOS (print)
print(nome)
print(idade + 1)

print(nome, idade, altura)
print("O seu nome é", nome, "e sua idade é de", idade, "anos.")
print(f"o seu nome é {nome} e sua idade é de {idade} anos")             #f string (string formatada)
print("o seu nome é {} e sua idade é de {} anos".format(nome, idade))

print(f"o seu nome é {nome}")
print("sua idade é de {idade} anos.")

# caracter \n imprime um quebra de linha
print(f"O seu nome é {nome}\n Sua idade é de {idade} anos\n Sua altura é de {altura} metros")


