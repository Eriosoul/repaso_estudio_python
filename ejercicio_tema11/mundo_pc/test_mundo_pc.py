from ejercicio_tema11.mundo_pc.computadora import Computadora
from ejercicio_tema11.mundo_pc.monitor import Monitor
from ejercicio_tema11.mundo_pc.raton import Raton
from ejercicio_tema11.mundo_pc.teclado import Teclado
from ejercicio_tema11.mundo_pc.orden import Orden

teclado1 = Teclado('Hp', 'USB')
raton1 = Raton('Gaming', 'USB')
monitor1 = Monitor('AOC', 27)
computadora1 = Computadora('Intel', monitor1, teclado1, raton1)

teclado2 = Teclado('Hp', 'USB')
raton2 = Raton('Gaming', 'USB')
monitor2 = Monitor('AOC', 27)
computadora2 = Computadora('Intel', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado3 = Teclado('Hp', 'USB')
raton3 = Raton('Gaming', 'USB')
monitor3 = Monitor('AOC', 27)
computadora3 = Computadora('Intel', monitor3, teclado3, raton3)

teclado4 = Teclado('Hp', 'USB')
raton4 = Raton('Gaming', 'USB')
monitor4 = Monitor('AOC', 27)
computadora4 = Computadora('Intel', monitor4, teclado4, raton4)

computadoras2 = [computadora3, computadora4]
orden2 = Orden(computadoras2)
print(orden2)
