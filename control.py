from flask import Flask, jsonify, request
from main import query
from main import update, select, insert, delete
from valida import valida_diretor
from modelo import insert_diretor, get_diretor
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
        return jsonify(delete("diretores", "id", request.json["id"]))

@app.route("/diretores/<int:id>", methods=["PUT"])
def idiomas(id):
    nome = request.json["nome_completo"]
    update("diretores", "id", id, ["nome_completo"], [nome])
    return jsonify(query("SELECT * FROM diretores WHERE id = %s", (id,)))


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
