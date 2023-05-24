try:
    archivo = open('prueba.txt', 'w', encoding='utf-8')
    archivo.write('Agregamos texto al archivo\n')
    archivo.write('Esto es genial')
except Exception as e:
    print(e)
finally:
    archivo.close()
