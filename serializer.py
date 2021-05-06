def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
    }


def diretor_from_db(*args):
    return {
        "nome_completo": args[0],
    }
