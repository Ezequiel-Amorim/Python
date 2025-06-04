import json
from random import randint
import os

# Caminho do arquivo onde as skills serão salvas
ARQUIVO_SKILLS = "skills.json"

# Função para criar uma nova skill
def create_skill():
    lvreq = randint(0, 100)
    name = input('Nome da skill: ')
    dano = 2 * lvreq
    return {"nome": name, "lvreq": lvreq, "dano": dano}

# Função para exibir uma skill
def livro_skills(skill):
    print(f'Nome da skill: {skill["nome"]}  |  LV: {skill["lvreq"]}  |  Dano: {skill["dano"]}')

# Função para salvar a lista de skills no arquivo JSON
def salvar_skills(lista):
    with open(ARQUIVO_SKILLS, 'w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

# Função para carregar as skills do arquivo JSON
def carregar_skills():
    if os.path.exists(ARQUIVO_SKILLS):
        with open(ARQUIVO_SKILLS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []  # Se não existir, retorna lista vazia

# Carregar skills salvas
lista_skills = carregar_skills()

# Criar nova skill e adicionar à lista
nova_skill = create_skill()
lista_skills.append(nova_skill)

# Salvar lista atualizada
salvar_skills(lista_skills)

# Exibir todas as skills
print("\n--- Livro de Skills ---")
for skill in lista_skills:
    livro_skills(skill)
