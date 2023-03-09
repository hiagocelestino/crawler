from app import db

class ConsultaDB(db.Model):
    __tablename__ = 'consulta'

    id = db.Column(db.Integer, primary_key=True)
    busca = db.Column(db.String, nullable=False)
    resultado = db.Column(db.String)

    def add_consulta(self):
        session = db.session()
        session.add(busca=self.busca, resultado=self.resultado)
        session.commit()
    
    def _consulta_dict(self):
        return ({
            'id_consulta': self.id,
            'busca': self.busca,
            'resultado': self.resultado
        })