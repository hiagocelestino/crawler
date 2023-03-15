from app import db
from enum import Enum
from app.repositories.erros.erros_personalizados import ErrorPersistirDados, ErrorBuscarDados

class Status(Enum):
    CONCLUIDO = 'CONCLUIDO'
    FALHA = 'FALHA'

class ConsultaDB(db.Model):
    __tablename__ = 'consulta'

    id = db.Column(db.Integer, primary_key=True)
    busca = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum(Status))
    resultado = db.Column(db.String)

    def add_consulta(self):
        try:
            session = db.session()
            session.add(self)
            session.commit()
        except Exception as e:
            print(e)
            raise ErrorPersistirDados

    def select_consulta(id_consulta):
        try:
            session = db.session()
            session.select(ConsultaDB).filter_by(id=id_consulta)
        except Exception as e:
            print(e)
            raise ErrorBuscarDados

    def _consulta_dict(self):
        return ({
            'id_consulta': self.id,
            'busca': self.busca,
            'resultado': self.resultado
        })