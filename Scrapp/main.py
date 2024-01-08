#  Anexo:Tenista líder en la Clasificación de la ATP individual
#  https://es.wikipedia.org/wiki/Anexo:Tenista_l%C3%ADder_en_la_Clasificaci%C3%B3n_de_la_ATP_individual

#  Vamos a otener la informacion de los tenistas lideres en la calisicaion de la ATP según wikipedia

from templates.spider import TenistaLider

if __name__ == '__main__':
    t: TenistaLider = TenistaLider()
    try:
        t.check_url_status()
        t.get_data_from_first_table()
    except Exception as e:
        print("Error: ", e)
