from random import randint

tentativa = int(input('Digite um número: '))

while True:
    numero_certo = randint(1,5)
    if numero_certo == tentativa:
        print('Parabéns, você acertou!')
        break
    else:
        print('Você erou, tente novamente')
        tentativa = int(input('Digite um número: '))
