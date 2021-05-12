from datetime import date

from mysql.connector import connect

show_schemas = "SHOW SCHEMAS"
params = None


def execute(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="locadora") as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid

def query(sql, params=None):
    with connect(host="localhost", user="root", password="root", database="locadora") as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()


def insert(tabela, colunas, valores):
    return execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)


def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])


def select(tabela, chave=1, valor_chave=1, limit=100, offset=0):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} = %s LIMIT {limit} offset {offset}""", (valor_chave,))

def select_like(tabela, chave=1, valor_chave=1, limit=100, offset=0):
    return query(f"""SELECT * FROM {tabela} WHERE {chave} LIKE %s LIMIT {limit} offset {offset}""", (f"%{valor_chave}%",))

#delete("diretores", "id", 23)
#delete("diretores","nome_completo","douglas")
#insert("diretores", ["nome_completo"], ["Douglas"])
#update('diretores',"id", 24, ['id','nome_completo'],['3','pedrin'])
#select("diretores","nome_completo","john")
#insert("usuarios", ["nome_completo","CPF"], ["Daniel Max","32165498740"])
#insert("locacoes",["data_inicio", "data_fim", "filmes_id", "usuarios_id"],["2020-07-05" , "2020-07-10", 1, 1])
#insert("filmes",["titulo","ano","classificacao","preco","diretores_id","generos_id"],["um dia de furia","2021","10","6.66",1,1])