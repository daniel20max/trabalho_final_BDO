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
    if data_inicio == 0:
        return False

    if data_fim == 0:
        return False

    if filmes_id == 0:
        return False

    if usuarios_id == 0:
        return False

    return True


def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if titulo == 0:
        return False

    if ano == 0:
        return False

    if classificacao == 0:
        return False

    if preco == 0:
        return False

    if diretores_id == 0:
        return False

    if generos_id == 0:
        return False

    return True


def valida_pagamento(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    if tipo == 0:
        return False

    if status == 0:
        return False

    if codigo_pagamento == 0:
        return False

    if valor == 0:
        return False

    if data == 0:
        return False

    if locacoes_id == 0:
        return False

    return True
