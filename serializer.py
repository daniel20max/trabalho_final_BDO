def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
    }


def diretor_from_db(*args):
    return {
        "nome_completo": args[0],
    }


def diretor_from_web_id(**kwargs):
    return {
        "id": kwargs["id"] if "id" in kwargs else "",
    }


def diretor_from_db_id(*args):
    return {
        "id": args[0],
    }