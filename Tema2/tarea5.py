nota = int(input("Introduce tu nota: "))
mesaje = None

if 0 <= nota < 6:
    mesaje = 'F'
elif 6 <= nota < 7:
    mesaje = 'D'
elif 7 <= nota < 8:
    mesaje = 'C'
elif 8 <= nota < 9:
    mesaje = 'B'
elif 9 <= nota <= 10:
    mesaje = 'A'
else:
    mesaje = 'Nota fuera de rango'
print(f'Su calificacion es una: {nota} , {mesaje}')