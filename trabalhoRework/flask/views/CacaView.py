import json
from flask import redirect, render_template, request
from flask_classful import FlaskView, route
import dao
from daoClass import index
from characteristcs import todasCaracteristicasAvatares


crud = index.Avatar()

class CacaView(FlaskView):
    route_base = '/'

    def index(self):
        return "<br>"

    @route('/alterar/<int:id>', methods=['POST'])
    @route('/cadastrar', methods=['POST'])
    def cadastrar(self, id: int = None):
        if id:
            dao.editar(dict(request.form))
        else:
            #dao.adicionar(dict(request.form))
            print(dict(request.form))
            dao.adicionar(dict(request.form))
            #crud.interactFile(dict(request.form))
        return redirect("/inicio")

    @route('/deletar/<int:id>', methods=['GET'])
    def deletar(self, id: int):
        dao.deletar(id)
        return redirect("/listar")

    @route('/cadastro/<int:id>', methods=['GET'])
    @route('/cadastro', methods=['GET'])
    def form(self, id: int = None):
        if id:
            return render_template("form.html", dados=dao.selecionar(id))

        return render_template("form.html", dados=[])

    @route('/listar', methods=['GET'])
    def listar(self):
        return render_template("listar.html", avatares=dao.selecionarTodos(), data_json=json.dumps(dao.selecionarTodos()), caracteristicas=todasCaracteristicasAvatares)

    @route('/inicio', methods=['GET'])
    def index(self):
        return render_template("index.html", has_avatar=len(dao.selecionarTodos()) > 0)