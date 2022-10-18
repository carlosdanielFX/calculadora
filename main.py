calculo = None

while calculo != 's':
    calculo = input(" use S para sair: \n use C para somar: \n use m para multiplicar: \n ")
    if calculo == 'c':
        s1 = int(input('Digite numero para soma: \n'))
        op = input('digite um operador: \n')
        s2 = int(input('digite segundo numero: \n'))
        if op == '+':
            resultado = s1 + s2
            print(f"resultado e {resultado}")
        else:
            print('OPERACAO INVALIDA')    
    if calculo == 'm':
        s3 = int(input('Digite numero para multiplicar: \n'))
        op = input('digite um operador: \n')
        s4 = int(input('digite segundo numero: \n'))
        if op == '*':
            resultado = s3 * s4
            print(f"resultado e {resultado}")
        else:
            print('OPERACAO INVALIDA')    

   
       
