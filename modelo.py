from main import insert, select, update, delete, select_like

#======================// Diretor \\===============================
def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])


def get_diretor(nome_completo):
    return select("diretores", "nome_completo", nome_completo)

def update_diretor(id, nome_completo):
    update("diretores", "id", id, ["id", "nome_completo"], [id, nome_completo])

def deletar_diretor(id):
    delete("diretores", "id", id)

#======================// Usuarios \\===============================

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)

def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)