from datetime import datetime

from . import db


class Operacao(db.Model):
    """Model — dados e acesso ao banco (tabela operacoes)."""

    __tablename__ = "operacoes"
    
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Float, nullable=False)
    num2 = db.Column(db.Float, nullable=False) 
    operacao = db.Column(db.String, nullable=False)
    etapas = db.Column(db.String, nullable=False)
    resultado = db.Column(db.String, nullable=False, default=0)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Produto {self.id} {self.nome}>"

    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado, criado_em):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
            criado_em=criado_em
        )
        db.session.add(resultado)
        db.session.commit()

    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.criado_em.desc()).limit(limite).all()
        )

    def __repr__(self):
        return f"<Operacao {self.id}: {self.etapas}>"