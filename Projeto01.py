from deep_translator import GoogleTranslator #biblioteca que usa o tradutor do google

#traducao = GoogleTranslator(source='pt', target='en').translate('Oi pessoal de boas ?')
#print(traducao)

#Anotações importantes a importação do GoogleTranslator(usa o tradutor do google e faz a tradução) para fazer a tradução tenho que colocar qual idioma que está no 'source'que seria a linguagem de entrada que sera escrita para a linguagem que deseja traduzir |'target' é a linguagem que desejo transforma meu texto para o idioma desejado

def traducao():
    try:
        descr = input('Texto que deseja traduzir: ').strip()
        if not descr:
            print("Entrada vazia. Por favor, digite um texto.")
            return
        traducao_en = GoogleTranslator(source='pt', target='en').translate(descr)
        print(f"Tradução: {traducao_en}")
    except Exception as e:
        print(f"Ocorreu um erro durante a tradução: {e}")
        
traducao()
