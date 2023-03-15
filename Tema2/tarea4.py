edad = int(input("Proporciona tu edad: "))
# ejemplo 1
# if edad >= 0 and edad <= 10:
#     print("La infancia es increible ")
# elif edad >= 11 and edad <= 20:
#     print("Muchos cambios y mucho estudio")
# elif edad >= 21 and edad <= 30:
#     print("Amor y comienza el trabajo")
# else:
#     print("error")

# Ejemplo 2
mensaje = None
if 0 <= edad <10:
    mensaje = 'La infancia es increible'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio'
elif 20 <= edad <30:
    mensaje = 'Amor y comienza el trabajo'
else:
    mensaje = 'Etapa de vida no conocida'
print(f'Tu edad es: {edad}, {mensaje}')