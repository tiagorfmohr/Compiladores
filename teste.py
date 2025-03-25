#o arquivo texto_teste.txt precisa estar no diretório C:\Users\%USUARIO%

import os
import re

def processar_arquivo_texto(nome_arquivo):
    """
    Processa um arquivo de texto, extrai caracteres, filtra, numera linhas e cria tabela de referências cruzadas.
    """
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(nome_arquivo):
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
            print(f"Diretório atual: {os.getcwd()}")
            print(f"Conteúdo do diretório: {os.listdir()}")
            return

        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # 1. Extração de caracteres ASCII
        caracteres_ascii = [ord(char) for char in conteudo]

        # 2. Filtragem de caracteres indesejados
        caracteres_filtrados = [
            char for char in caracteres_ascii if char not in [ord(c) for c in [' ', '\n', '\t', '\r']]
        ]

        print("Caracteres ASCII filtrados:")
        print(caracteres_filtrados)
        print("-" * 40)

        # 3. Listagem numerada e 4. Tabela de referências cruzadas
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            tabela_referencias = {}
            for numero, linha in enumerate(linhas, 1):
                print(f"{numero}: {linha.strip()}")
                palavras = re.findall(r'\b\w+\b', linha.lower())
                for palavra in palavras:
                    if palavra not in tabela_referencias:
                        tabela_referencias[palavra] = []
                    tabela_referencias[palavra].append(numero)

            print("-" * 40)
            print("Tabela de referências cruzadas:")
            for palavra, numeros_linhas in sorted(tabela_referencias.items()):
                print(f"{palavra}: {numeros_linhas}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Exemplo de uso
processar_arquivo_texto("texto_teste.txt")