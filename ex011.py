print('Programa que lê a largura e a altura de uma parede em metros e calcula a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinha pinta 2 metros quadrados.')
print('-'*176)
largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
área = largura * altura
print('Sua parede tem dimensão {} x {} e sua área é de {} m²'.format(largura,altura,área))
tinta = área/2
print('Para pintar essa parede, você vai precisar de {} litros de tinta'.format(tinta))