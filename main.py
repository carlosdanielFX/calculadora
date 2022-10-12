calculo = None

while calculo != 'e':
    calculo = input(" use E para sair: \n use S para soma: \n use M para multiplicar: \n")
    if calculo == 's':
        s1 = int(input('Digite numero para soma: \n'))
        s2 = int(input('digite segundo numero: \n'))
        soma = (s1+s2)
        print(f" seu resultador e {soma}")
    elif calculo == 'm':
        m1 = int(input('digite numero para multiplicao: \n'))
        m2 = int(input('digite segundo numero: \n'))
        soma = (m1*m2)
        print(f"seu resultado e {soma}")
       
