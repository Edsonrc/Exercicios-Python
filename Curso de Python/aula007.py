n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
re = n1 % n2
print('Você digitou os seguintes valores: {} e {}'.format(n1,n2))
print('A soma vale {},\n a multiplicação vale {}\n e a divisão vale {:.3f}'.format(s, m, d), end="")
print(' A divisão inteira vale {} e o resto da divisão vale {}'.format(di, re))



