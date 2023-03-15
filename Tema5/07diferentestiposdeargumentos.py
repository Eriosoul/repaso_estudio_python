def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Lola', 'Karla']
desplegarNombres(nombres)
desplegarNombres('Carlos')  # error ya que nos intera letra por letra
# desplegarNombres(10, 11)  # error ya que son int
desplegarNombres((10, 11))  # si funcionaria porque se transforma en una tuple
desplegarNombres([10, 11])  # en vez de tupla ahora es una lista
