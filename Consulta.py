from main import query

def consultar_locacoes_id_do_filme(id):
    return query(f"""
select
	locacoes.id as locacao_id,
	filmes.id as filmes_id,
	filmes.titulo as titulo_do_filme,
    usuarios.nome_completo as nome_Usuario,
    data_inicio as data_locacao,
    pagamento.status  as status_da_compra    
from locacoes
inner join filmes on locacoes.filmes_id = filmes.id
inner join usuarios on locacoes.usuarios_id = usuarios.id
inner join pagamento on pagamento.locacoes_id = locacoes.id
where filmes.id = %s;
""",(id,))

def consultar_locacao_id(id):
    return query(f"""
  select
	locacoes.id as id_da_locacao,
    filmes.titulo as titulo,
    usuarios.nome_completo as usuarios
    from locacoes
inner join filmes on filmes.id = locacoes.filmes_id
inner join usuarios on locacoes.usuarios_id = usuarios.id
where locacoes.id = %s;
""", (id,))

def consultar_locacao_do_usuario_id(id):
    return query("""
select
	usuarios.id,
	usuarios.nome_completo as nome,
    filmes.titulo as titulo,
    locacoes.data_fim as Entregar
from locacoes
inner join filmes on filmes.id = locacoes.filmes_id
inner join usuarios on locacoes.usuarios_id = usuarios.id
where usuarios.id = %s
    """, (id,))

