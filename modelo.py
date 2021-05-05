from main import insert, select


def insert_diretor(nome):
    insert("diretores", ['nome_completo'], [nome])


def get_diretor(nome):
    select("diretores", 'nome_completo', nome)