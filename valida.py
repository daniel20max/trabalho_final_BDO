def valida_diretor(nome_completo):
    if len(nome_completo) == 0:
        return False

    return True

def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) == 0:
        return False

    return True

def valida_genero(nome):
    if len(nome) == 0:
        return False

    return True

def valida_locacoes(data_inicio, data_fim, filmes_id, usuarios_id):
    if data_inicio != int:
        return False

    if data_fim != int:
        return False

    if len(filmes_id) == 0:
        return False

    if len(usuarios_id) == 0:
        return False

    return True