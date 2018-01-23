'''
Construir um algoritmo que pergunte os km percorridos por um carro
alugado e a quantidade de dias que ele foi alugado. O aluguel p/ dia é
de R$ 60 e o km é de R$ 0.15 km/rodado
Nome: Edson Ricardo Czarneski
Disciplina: Programação II - Python
Data: 13/01/2018

'''
dias = float(input('Para quantos dias o carro foi alugado?'))
km = float(input('Quantos quilômetros foram rodados?'))
valor = (dias*60) + (km * 0.15)
print('O preço das diárias é de R$ {:.2f};\n O valor da quilometragem é de R${:.2f}; \n O valor total é de R${:.2f}.'.format(dias * 60, km * 0.15, valor ))