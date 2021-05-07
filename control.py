from flask import Flask, jsonify, request
from main import query
from main import update, select, insert, delete
from valida import valida_diretor, valida_diretor_id
from modelo import insert_diretor, get_diretor, update_diretor, deletar_diretor
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
            return jsonify({"Erro":"valor nao deletado"})


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


@app.route("/generos", methods=["GET", "POST", "DELETE", "PATCH"])
def genero():
    if request.method == "GET":
        return jsonify(select("generos"))
    elif request.method == "POST":
        return jsonify(insert("generos", ["nome"], [request.json["nome"]]))
    elif request.method == "DELETE":
        return jsonify(delete("generos", "id", request.json["id"]))
    elif request.method == "PATCH":
        return jsonify(update("generos", "id", request.json["id"]))


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
