from flask import Flask, jsonify, request
from main import query
from valida import valida_diretor, valida_usuario, valida_genero, valida_locacoes
from modelo import insert_diretor, get_diretor, update_diretor, deletar_diretor, select_usuarios, insert_usuario, \
    get_usuario, update_usuario, delete_usuario, select_diretores, select_genero, deletar_genero, update_genero, \
    insert_genero, get_genero, insert_locacoes, select_locacoes, deletar_locacoes, update_locacoes, get_locacoes
from serializer import nome_usuario_from_web, diretor_from_db, diretor_from_web, usuario_from_db, usuario_from_web, \
    nome_genero_from_web, genero_from_db, genero_from_web, data_locacoes_from_web, locacoes_from_db, locacoes_from_web

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return jsonify(query("SHOW schemas"))
    elif request.method == "POST":
        return request.json


@app.route("/diretores", methods=["GET", "POST"])
def diretor_GetPost():
    if request.method == "GET":
        nome_completo = nome_usuario_from_web(**request.args)
        diretores = select_diretores(nome_completo)
        diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
        return jsonify(diretores_from_db)
    elif request.method == "POST":
        diretor = diretor_from_web(**request.json)
        if valida_diretor(**diretor):
            id_diretor = insert_diretor(**diretor)
            diretor_new = get_diretor(id_diretor)
            return jsonify(diretor_from_db(diretor_new))
        else:
            return jsonify({"Valor": "Nao adicionado a tabela"})


@app.route("/diretores/<int:id>", methods=["PUT", "PATCH", "DELETE"])
def diretor_delete_update(id):
    if request.method == "DELETE":
        try:
            deletar_diretor(id)
            return jsonify({"Valor": "Deletado"})
        except:
            return jsonify({"Valor": "Nao deletado"})
    elif request.method == "PUT" or "PATCH":
        diretor = diretor_from_web(**request.json)
        if valida_diretor(**diretor):
            update_diretor(id, **diretor)
            diretor_alterado = get_diretor(id)
            return jsonify(diretor_from_db(diretor_alterado))
        else:
            return jsonify({"Erro": "Valor nao alterado"})


@app.route("/usuarios", methods=["GET", "POST"])
def usuario_getpost():
    if request.method == "GET":
        nome_completo = nome_usuario_from_web(**request.args)
        usuarios = select_usuarios(nome_completo)
        usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
        return jsonify(usuarios_from_db)
    elif request.method == "POST":
        usuario = usuario_from_web(**request.json)
        if valida_usuario(**usuario):
            id_usuario = insert_usuario(**usuario)
            usuario_cadastrado = get_usuario(id_usuario)
            return jsonify(usuario_from_db(usuario_cadastrado))
        else:
            return jsonify({"erro": "Usuario invalido"})


@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH", "DELETE"])
def usuario_delete_update(id):
    if request.method == "DELETE":
        try:
            delete_usuario(id)
            return jsonify({"Valor": "Deletado"})
        except:
            return jsonify({"Erro": "Valor nao alterado"})
    elif request.method == "PUT" or "PATCH":
        usuario = usuario_from_web(**request.json)
        if valida_usuario(**usuario):
            update_usuario(id, **usuario)
            usuario_cadastrado = get_usuario(id)
            return jsonify(usuario_from_db(usuario_cadastrado))
        else:
            return jsonify({"Erro": "Valor nao alterado"})


@app.route("/generos", methods=["GET", "POST"])
def genero_getpost():
    if request.method == "GET":
        nome = nome_genero_from_web(**request.args)
        generos = select_genero(nome)
        generos_from_db = [genero_from_db(genero) for genero in generos]
        return jsonify(generos_from_db)
    elif request.method == "POST":
        genero = genero_from_web(**request.json)
        if valida_genero(**genero):
            id_genero = insert_genero(**genero)
            genero_novo = get_genero(id_genero)
            return jsonify(genero_from_db(genero_novo))
        else:
            return jsonify({"erro": "Genero invalido"})

@app.route("/generos/<int:id>", methods=["DELETE", "PUT", "PATCH"])
def genero_delete_update(id):
    if request.method == "DELETE":
        try:
            deletar_genero(id)
            return jsonify({"Valor": "Deletado"})
        except:
            return jsonify({"Erro": "Valor nao Excluido"})
    elif request.method == "PUT" or "PATCH":
        genero = genero_from_web(**request.json)
        if valida_genero(**genero):
            update_genero(id, **genero)
            genero_novo = get_genero(id)
            return jsonify(genero_from_db(genero_novo))
        else:
            return jsonify({"Erro": "Valor nao foi alterado"})


@app.route("/locacoes", methods=["GET", "POST"])
def locacoes_getpost():
    if request.method == "GET":
        data = data_locacoes_from_web(**request.args)
        locacao = select_locacoes(data)
        locacao_from_db = [locacoes_from_db(locacoes) for locacoes in locacao]
        return jsonify(locacao_from_db)
    elif request.method == "POST":
        data = locacoes_from_web(**request.json)
        if valida_locacoes(**data):
            id_locacoes = insert_locacoes(**data)
            data_add = get_locacoes(id_locacoes)
            return jsonify(usuario_from_db(data_add))
        else:
            return jsonify({"Erro": "Valor nao adicionado"})






if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
