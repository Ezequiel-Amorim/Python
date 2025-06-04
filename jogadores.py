from random import randint, choice
import json
import os

ARQUIVO_JOGADORES = 'jogadores.json'

# Criação de personagens (Jogadores)
def create_player():
    nivel = randint(0, 80)
    lista_classes = ['Lutador', 'Guerreiro', 'Mago', 'Assassino', 'Ferreiro', 'Assassino', 'Arqueiro']
    name = input('Nick: ')
    classe = choice(lista_classes)
    return {
        'Name': name,
        'Classe': classe,
        'LV': nivel,
        'HP': 100 * nivel,
        'Dano': 8 * nivel
    }

# Exibição do personagem
def ui_player(player):
    print(f'Nome : {player["Name"]} | LV : {player["LV"]} | Classe : {player["Classe"]}')
    print(f'HP: {player["HP"]} | Dano: {player["Dano"]}')
    print('-' * 40)

# Salvar lista de jogadores em arquivo JSON
def salva_player(lista):
    with open(ARQUIVO_JOGADORES, 'w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

# Carregar lista de jogadores de arquivo JSON
def carregar_player():
    if os.path.exists(ARQUIVO_JOGADORES):
        with open(ARQUIVO_JOGADORES, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []  # Corrigido: estava dentro do if

# Programa principal
lista_jogadores = carregar_player()

novo_player = create_player()
lista_jogadores.append(novo_player)

salva_player(lista_jogadores)

print("\n=== / Lista de Jogadores / ===")
for player in lista_jogadores:
    ui_player(player)
