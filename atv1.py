numero = input ('digite um numero:')
numero = int(numero)
validaposotivo = numero>0
validanegativo = numero<0
if validaposotivo:
    print("O numero é positivo")
elif validanegativo:
    print("O numero é negativo")
else:
    print("O numero é zero")
