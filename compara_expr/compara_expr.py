# Este programa determina si hay algún error en el proceso de simplificación de una expresión. 
# Pero no verifica si efectivamente se está simplificando la expresión.

import sympy as sp

simbolos_permitidos='0123456789+*-/xyz()'

def compara_ecuaciones():
    mensaje_inicial='''
    Para escribir las expresiones utilice la sintaxis de Python.
    Recuerde que la mul/ción es con el asterisco *,
    que la pot/ción es con doble asterisco **.
    Además, sólo está permitido usar: ''' \
    + ','.join(simbolos_permitidos) \
    + '\n Escriba la expresión inicial '

    x,y,z=sp.symbols('x y z')

    cadena1 = yield mensaje_inicial

    # verifica que TODOS los símbolos de la cadena estén en `símbolos_permitidos`
    if not min( i in simbolos_permitidos for i in set(cadena1)): 
        raise ValueError('La ecuación tiene símbolos inválidos para este programa. ')

    exp1 = sp.S(cadena1) # convierte la cadena a una expresión de sympy
    print(cadena1)

    while True:

        cadena2 = yield 'Escriba la expresión simplificada. "fin" para terminar '
        if cadena2=='fin':
            print('Chao')
            break

        # verifica que TODOS los símbolos de la cadena estén en `símbolos_permitidos`
        if not min( i in simbolos_permitidos for i in set(cadena2)):
            raise ValueError('La ecuación tiene símbolos inválidos para este programa')

        exp2 = sp.S(cadena2) # convierte la cadena a una expresión de sympy
        print(cadena2)

        if exp2-exp1==0: # Compara la expresión anterior con la actual
            print('iguales')
            exp1=exp2
            pass
        else:
            print('diferentes')
            pass

if __name__=='__main__': # No se ejecuta cuando se usa como librería
    ce = compara_ecuaciones()
    texto=next(ce)
    repetir=True
    while repetir:
        try:
            texto=ce.send(input(texto))
        except:
            repetir = False


'''
Para escribir las expresiones utilice la sintaxis de Python.
    Recuerde que la mul/ción es con el asterisco *,
    que la pot/ción es con doble asterisco **.
    Además, sólo está permitido usar: 0,1,2,3,4,5,6,7,8,9,+,*,-,/,x,y,z,(,)
 Escriba la expresión inicial 4*x+2*(3+x)
4*x+2*(3+x)
Escriba la expresión simplificada. "fin" para terminar 4*x+6+2*x
4*x+6+2*x
iguales
Escriba la expresión simplificada. "fin" para terminar 4*x+2*(3)
4*x+2*(3)
diferentes
Escriba la expresión simplificada. "fin" para terminar 6*x+6
6*x+6
iguales
Escriba la expresión simplificada. "fin" para terminar fin
Chao
'''