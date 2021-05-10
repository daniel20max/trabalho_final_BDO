from flask import Flask, jsonify, request
from main import query
from main import update, select, insert, delete
from valida import valida_diretor, valida_diretor_id, valida_usuario
from modelo import insert_diretor, get_diretor, update_diretor, deletar_diretor, select_usuarios, insert_usuario, \
    get_usuario
from serializer import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return jsonify(query("SHOW schemas"))
    elif request.method == "POST":
        return request.json


@app.route("/diretores", methods=["GET", "POST", "DELETE"])
def diretor():
    if request.method == "GET":
        return jsonify(query("Select * From diretores"))
    elif request.method == "POST":
        diretor = diretor_from_web(**request.json)
        if valida_diretor(**diretor):
            insert_diretor(**diretor)
            diretor_novo = get_diretor(diretor['nome_completo'])
            return jsonify(diretor_from_db(diretor_novo))
        else:
            return jsonify({"erro": "diretor invalido"})
    elif request.method == "DELETE":
        diretor = diretor_from_web_id(**request.json)
        if valida_diretor_id(**diretor):
            deletar_diretor(**diretor)
            diretor_deletado = deletar_diretor(diretor("id"))
            return jsonify(diretor_from_db_id(diretor_deletado))
        else:
            return jsonify({"Erro": "valor nao deletado"})


@app.route("/diretores/<int:id>", methods=["PATCH"])
def patch_diretor(id):
    if request.method == "PATCH":
        diretor = diretor_from_web(**request.json)
        if valida_diretor(**diretor):
            update_diretor(id, **diretor)
            diretor_alterado = get_diretor(diretor(id))
            return jsonify(diretor_from_db(diretor_alterado))
        else:
            return jsonify({"Erro": "Valor nao alterado"})


@app.route("/usuarios", methods=["GET"])
def usuarios_get():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)


@app.route("/usuarios", methods=["POST"])
def usuarios_post():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


<<<<<<< Updated upstream
@app.route("/generos", methods=["GET", "POST", "DELETE", "PATCH"])
def genero():
=======
@app.route("/pagamento", methods=["GET", "POST"])
def pagamento_getpost():
>>>>>>> Stashed changes
    if request.method == "GET":
        return jsonify(select("generos"))
    elif request.method == "POST":
<<<<<<< Updated upstream
        return jsonify(insert("generos", ["nome"], [request.json["nome"]]))
    elif request.method == "DELETE":
        return jsonify(delete("generos", "id", request.json["id"]))
    elif request.method == "PATCH":
        return jsonify(update("generos", "id", request.json["id"]))
=======
        pagamento = pagamento_from_web(**request.json)
        if valida_pagamento(**pagamento):
            id_pagamento = insert_pagamento(**pagamento)
            id_pagamento_add = get_pagamento(id_pagamento)
            return jsonify(pagamento_from_db(id_pagamento_add))
        else:
            return jsonify({"Erro": "Valor nao adicionado"})


@app.route("/pagamento/<int:id>", methods=["DELETE", "PUT", "PATCH"])
def pagamento_delete_update(id):
    if request.method == "DELETE":
        try:
            deletar_pagamento(id)
            return jsonify({"Valor": "Deletado"})
        except:
            return jsonify({"Erro": "Valor nao Excluido"})
    elif request.method == "PUT" or "PATCH":
        pagamento = pagamento_from_web(**request.json)
        if valida_pagamento(**pagamento):
            update_pagamento(id, **pagamento)
            pagamento_novo = get_pagamento(id)
            return jsonify(pagamento_from_db(pagamento_novo))
        else:
            return jsonify({"Erro": "Valor nao foi alterado"})

>>>>>>> Stashed changes


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
