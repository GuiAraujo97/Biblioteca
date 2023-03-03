import json
import unicodedata

# Lê o arquivo JSON no modo de leitura
with open('biblioteca.json') as arquivo:
    biblioteca = json.load(arquivo)


# Formata as informações do arquivo JSON para facilitar a busca
def formatar_pesquisa(pesquisa):
    pesquisa = str.upper(pesquisa)
    pesquisa = unicodedata.normalize('NFKD', pesquisa).encode('ASCII', 'ignore').decode()
    return pesquisa


# Pergunta ao usuário qual livro ele deseja consultar ou encontrar na biblioteca
titulo = input('Qual livro você deseja consultar ou encontrar a localização?: ')

# Busca o livro na base de dados da biblioteca (JSON)
for livro in biblioteca['livros']:
    if formatar_pesquisa(livro['titulo']) == formatar_pesquisa(titulo):
        print('Título:', livro['titulo'].title())
        print('Autor:', livro['autor'])
        print('Ano:', livro['ano'])
        local = livro['local']
        coluna = local[0]
        linha = local[1:3]
        print(f'O livro se encontra na estante {coluna}, na prateleira {linha}.')
        break
else:
    print('Livro não encontrado na biblioteca.')
