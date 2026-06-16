from models import db
from models.filme import Filme
from models.sala import Sala

def popular_dados():
    if Filme.query.count() > 0:
        return
    
    filmes = [
        Filme(titulo="Vingadores: Ultimato", duracao=181, classificacao="12"),
        Filme(titulo="Divertidamente 2", duracao=96, classificacao="L"),
    ]

    salas = [
        Sala(numero=1, capacidade=120),
        Sala(numero=2, capacidade=80),
    ]

    db.session.add_all(filmes + salas)
    db.session.commit()
