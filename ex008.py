print('Programa que lê um valor em metros e exibe convertidos em centímetros e milímetros')
print('----------------------------------------------------------------------------------')
medida = float(input('Digite um valor em metros: '))
cm = medida *100
mm = medida *1000
print("O valor em centímetros é {:.0f}".format(cm))
print("O valor em milímetros é {:.0f}".format(mm))