#Nosso desafio é criar um código que solicite ao usuário que insira um número positivo. No entanto, como não podemos confiar no usuário para fornecer um valor válido na primeira tentativa, precisamos criar uma lógica que permita solicitar novamente até que o usuário finalmente insira um número válido.

numero = -1
for i in range(3):
    numero = int(input('Insira um número positivo: '))
    if numero > 0:
        break
print(f'Voce inseriu {numero}') 
#Perceba que, para criar esse loop, precisamos definir um número arbitrário de tentativas para que o usuário inserisse esse valor. Isso acontece porque o loop for é utilizado quando se conhece previamente o número de iterações que devem ser realizadas.

numero2 = -1
while numero2 <= 0:
    numero2 = int(input('Insira um número positivo: '))
print(f'Voce inseriu {numero2}')
