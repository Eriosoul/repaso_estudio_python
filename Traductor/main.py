from translate import Translator

translator = Translator(from_lang='spanish', to_lang='english')

text = input("¿Qué deseas traucir?")
print(text)

res = translator.translate(text)
print(res)