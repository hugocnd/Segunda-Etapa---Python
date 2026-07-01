from flask import Blueprint, redirect, render_template, request, url_for
from models import Filme, Sala, Sessao, db
from datetime import datetime

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema", template_folder="../views/templates")


@cinema_bp.route("/")
def index():
    sessoes = Sessao.listar_com_detalhes()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":
        filme_id = request.form.get("filme_id")
        sala_id = request.form.get("sala_id")
        data_hora_texto = request.form.get("data_hora")
        preco_texto = request.form.get("preco")

        data_hora_objeto = datetime.strptime(data_hora_texto, '%Y-%m-%dT%H:%M')

        nova_sessao = Sessao(
            filme_id=int(filme_id),
            sala_id=int(sala_id),
            data_hora=data_hora_objeto, 
            preco=float(preco_texto)    
        )

        db.session.add(nova_sessao)
        db.session.commit()

        return redirect(url_for("cinema.index"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
