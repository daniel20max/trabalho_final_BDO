def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
    }


def diretor_from_db(diretor):
    return {
        "id": diretor["id"],
        "nome_completo": diretor["nome_completo"]
    }


def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }


def usuario_from_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"]
    }


def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""


def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else "",
    }


def genero_from_db(genero):
    return {
        "id": genero["id"],
        "nome": genero["nome"]
    }


def nome_genero_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else ""


def locacoes_from_web(**kwargs):
    return {
        "data_inicio": kwargs["data_inicio"] if "data_inicio" in kwargs else "",
        "data_fim": kwargs["data_fim"] if "data_fim" in kwargs else "",
        "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
        "usuarios_id": kwargs["usuarios_id"] if "usuarios_id" in kwargs else "",
    }


def locacoes_from_db(locacao):
    return {
        "id": locacao["id"],
        "data_inicio": locacao["data_inicio"].strftime('%d-%m-%Y'),
        "data_fim": locacao["data_fim"].strftime('%d-%m-%Y'),
        "filmes_id": locacao["filmes_id"],
        "usuarios_id": locacao["usuarios_id"]
    }


def data_locacoes_from_web(**kwargs):
    return kwargs["data_inicio"] if "data_inicio" in kwargs else ""


def filmes_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": str(kwargs["preco"]) if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else "",
    }


def filmes_from_db(filme):
    return {
        "id": filme["id"],
        "titulo": filme["titulo"],
        "ano": filme["ano"],
        "classificacao": filme["classificacao"],
        "preco": str(filme["preco"]),
        "diretores_id": filme["diretores_id"],
        "generos_id": filme["generos_id"]
    }


def filmes_titulos_from_web(**kwargs):
    return kwargs["titulo"] if "titulo" in kwargs else ""


def pagamento_from_web(**kwargs):
    return {
        "tipo": kwargs["tipo"] if "tipo" in kwargs else "",
        "status": kwargs["status"] if "status" in kwargs else "",
        "codigo_pagamento": kwargs["codigo_pagamento"] if "codigo_pagamento" in kwargs else "",
        "valor": str(kwargs["valor"]) if "valor" in kwargs else "",
        "data": kwargs["data"] if "data" in kwargs else "",
        "locacoes_id": kwargs["locacoes_id"] if "locacoes_id" in kwargs else "",
    }


def pagamento_from_db(pagamento):
    return {
        "id": pagamento["id"],
        "tipo": pagamento["tipo"],
        "status": pagamento["status"],
        "codigo_pagamento": pagamento["codigo_pagamento"],
        "valor": str(pagamento["valor"]),
        "data": pagamento["data"].strftime('%d-%m-%Y'),
        "locacoes_id": pagamento["locacoes_id"]
    }


def pagamento_tipo_from_web(**kwargs):
    return kwargs["tipo"] if "tipo" in kwargs else ""

def consultar_filme_id_from_web(**kwargs):
    return {
        "id": kwargs["id"] if "id" in kwargs else "",
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "data_inicio": kwargs["data_inicio"] if "data_inicio" in kwargs else "",
        "status": kwargs["status"] if "status" in kwargs else "",
    }

def consultar_filme_id_from_db(consulta_filme):
    return {
        "id": consulta_filme["id"],
        "titulo": consulta_filme["titulo"],
        "nome_completo": consulta_filme["nome_completo"],
        "data_inicio": consulta_filme["data_inicio"].strftime('%d-%m-%Y'),
        "status": consulta_filme["status"],
    }