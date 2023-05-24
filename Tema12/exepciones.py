from Tema12.numerosidentitcosexeption import NumerosIdenticosExeption
resultado = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosExeption('Numeros identicos')
    resultado = a/b
except ZeroDivisionError as e:
    print('Ocurrio un error: ', e)

except TypeError as a:
    print('Ocurrio un error', a)

except Exception:
    print('Final error')

print(f'Resultado: {resultado}')
print('Continuamos...')
