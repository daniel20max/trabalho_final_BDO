from main import insert, select, update, delete


def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])


def get_diretor(nome_completo):
    return select("diretores", "nome_completo", nome_completo)

def update_diretor(id, nome_completo):
    update("diretores", "id", id, ["id", "nome_completo"], [id, nome_completo])

def deletar_diretor(id):
    delete("diretores", "id", id)