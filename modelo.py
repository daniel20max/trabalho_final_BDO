from main import insert, select


def insert_diretor(nome_completo):
    insert("diretores", ["nome_completo"], [nome_completo])


def get_diretor(nome_completo):
    select("diretores", "nome_completo", nome_completo)
