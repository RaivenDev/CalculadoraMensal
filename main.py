#Primeiro Gasto
val = float(input('me fale o valor de seu saldo mensal '))
prod1 = float(input('Me fale o valor do primeiro gasto'))
resul = val - prod1
valor1 = val*(1/100)
relult = resul / valor1
resulta = val - resul
resultar = resulta / valor1
print(
    'de acordo com o seu saldo de {}, ao gastar em algo de valor {}, você estaria gastando  {:.2f}% de seu salário, assim sobrando {:.2f}%, equivalente a {}'.format(val, prod1, resultar, relult, resul))
Continua = int(input('Quer continuar a subtrair com o mesmo saldo restante(2) ou quer parar por aqui(0)?'))
if Continua < 1:
    print('obrigado por usar essa calculadora de contas :) . Criada por Gustavo Linhares')
else:
    #Segundo Gasto
    prod2 = float(input('Me fale o valor do segundo gasto'))
    resul1 = resul - prod2
    relult1 = resul1 / valor1
    resulta1 = val - resul1
    resultar1 = resulta1 / valor1
print(
    'de acordo com o seu saldo de {}, ao gastar em algo de valor {}, você estaria gastando(mais os produtos anteriormente contados) {:.2f}% de seu salário, assim sobrando {:.2f}%,equivalente a {}'.format(val, prod2, resultar1, relult1, resul1))
Continua1= int(input('Quer continuar a subtrair com o mesmo saldo restante(2) ou quer parar por aqui(0)?'))

if Continua < 1:
    print('obrigado por usar essa calculadora de contas :) . Criada por Gustavo Linhares')
else:
    #Terceiro Gasto
    prod3 = float(input('Me fale o valor do terceiro gasto'))
    resul2 = resul1 - prod3
    relult2 = resul2 / valor1
    resulta2 = val - resul2
    resultar2 = resulta2 / valor1
print(
    'de acordo com o seu saldo de {}, ao gastar em algo de valor {}, você estaria gastando(mais os produtos anteriormente contados) {:.2f}% de seu salário, assim sobrando {:.2f}%,equivalente a {}'.format(val, prod3, resultar2, relult2, resul2))
Continua1= int(input('Quer continuar a subtrair com o mesmo saldo restante(2) ou quer parar por aqui(0)?'))
if Continua < 1:
    print('obrigado por usar essa calculadora de contas :) . Criada por Gustavo Linhares')
else:
    #quarto Gasto
    prod4 = float(input('Me fale o valor do quarto gasto'))
    resul3 = resul2 - prod4
    relult3 = resul3 / valor1
    resulta3 = val - resul3
    resultar3 = resulta3 / valor1
print(
    'de acordo com o seu saldo de {}, ao gastar em algo de valor {}, você estaria gastando(mais os produtos anteriormente contados) {:.2f}% de seu salário, assim sobrando {:.2f}%,equivalente a {}'.format(val, prod4, resultar3, relult3, resul3))
Continua1= int(input('Quer continuar a subtrair com o mesmo saldo restante(2) ou quer parar por aqui(0)?'))
if Continua < 1:
    print('obrigado por usar essa calculadora de contas :) . Criada por Gustavo Linhares')
else:
    #quinto Gasto
    prod5 = float(input('Me fale o valor do quinto gasto'))
    resul4 = resul3 - prod5
    relult4 = resul4 / valor1
    resulta4 = val - resul4
    resultar4 = resulta3 / valor1
    print(
        'de acordo com o seu saldo de {}, ao gastar em algo de valor {}, você estaria gastando(mais os produtos anteriormente contados) {:.2f}% de seu salário, assim sobrando {:.2f}%,equivalente a {}'.format(val, prod5, resultar4, relult4, resul4))
    print('Esse foi o último gasto que o meu criador teve paciencia em fazer caso queira mais gastos disponiveis fale com meu criador :)')