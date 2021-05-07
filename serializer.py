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
        "data_inicio": locacao["data_inicio"],
        "data_fim": locacao["data_fim"],
        "filmes_id": locacao["filmes_id"],
        "usuarios_id": locacao["usuarios_id"]
    }

def data_locacoes_from_web(**kwargs):
    return kwargs["data_inicio"] if "data_inicio" in kwargs else ""
