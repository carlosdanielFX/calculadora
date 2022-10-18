calculo = None

while calculo != 's':
    calculo = input(" use S para sair: \n use C para continuar: \n ")
    if calculo == 'c':
        s1 = int(input('Digite numero para soma: \n'))
        op = str(input('digite um operador: \n'))
        s2 = int(input('digite segundo numero: \n'))
        if op == '+':
            resultado = s1 + s2
            print(f"resultado e {resultado}")
        else:
            print("operedor ivalido")
    elif op == '-':
        resultado = s1 - s2
        print(f"resultado e {resultado}")
    else:
          print("operedor ivalido")
       
