from main import insert, select, update, delete, select_like


# ======================// Diretor \\===============================
def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])


def get_diretor(id_diretor):
    return select("diretores", "id", id_diretor)[0]


def update_diretor(id, nome_completo):
    update("diretores", "id", id, ["id", "nome_completo"], [id, nome_completo])


def deletar_diretor(id_usuario):
    delete("diretores", "id", id_usuario)


def select_diretores(nome_completo):
    return select_like("diretores", "nome_completo", f"%{nome_completo}%")


# ======================// Usuarios \\===============================

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


# ======================// Generos \\===============================


def insert_genero(nome):
    return insert("generos", ["nome"], [nome])


def get_genero(id_genero):
    return select("generos", "id", id_genero)[0]


def update_genero(id, nome):
    update("generos", "id", id, ["id", "nome"], [id, nome])


def deletar_genero(id_genero):
    delete("generos", "id", id_genero)


def select_genero(nome):
    return select_like("generos", "nome", nome)


# ======================// locacoes \\===============================

def insert_locacoes(data_inicio, data_fim, filmes_id, usuarios_id):
    return insert("locacoes", ["data_inicio", "data_fim", "filmes_id", "usuarios_id"],
                  [data_inicio, data_fim, filmes_id, usuarios_id])


def update_locacoes(id, data_inicio, data_fim, filmes_id, usuarios_id):
    update("locacoes", "id", id, ["data_inicio", "data_fim", "filmes_id", "usuarios_id"],
           [data_inicio, data_fim, filmes_id, usuarios_id])


def get_locacoes(id_locacoes):
    return select("locacoes", "id", id_locacoes)[0]


def deletar_locacoes(id_locacoes):
    delete("locacoes", "id", id_locacoes)


def select_locacoes(data_inicio):
    return select_like("locacoes", "data_inicio", data_inicio)


# ======================// Filme \\===============================

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
                  [titulo, ano, classificacao, preco, diretores_id, generos_id])


def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def get_filme(id_filme):
    return select("filmes", "id", id_filme)[0]


def deletar_filme(id_filme):
    delete("filmes", "id", id_filme)


def select_filme(titulo):
    return select_like("filmes", "titulo", f"%{titulo}%")


# ======================// Pagamento \\===============================

def insert_pagamento(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    return insert("pagamento", ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
                  [tipo, status, codigo_pagamento, valor, data, locacoes_id])


def update_pagamento(id, tipo, status, codigo_pagamento, valor, data, locacoes_id):
    update("pagamento", "id", id, ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
           [tipo, status, codigo_pagamento, valor, data, locacoes_id])


def get_pagamento(id_pagamento):
    return select("pagamento", "id", id_pagamento)[0]


def deletar_pagamento(id_pagamento):
    delete("pagamento", "id", id_pagamento)


def select_pagamento(titulo):
    return select_like("pagamento", "preco", f"%{titulo}%")
