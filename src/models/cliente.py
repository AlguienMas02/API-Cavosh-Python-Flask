from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Nombres = db.Column(db.String(30), nullable=False)
    Correo = db.Column(db.String(30), unique=True, nullable=True)
    Passwordd = db.Column(db.String(20), nullable=False)

    
    codigos = db.relationship('CodigoVerificacion', backref='cliente', lazy=True)
    # Forma de hacer una relación de una tabla a otra, con un llave foranea en la tabla de destino.

    def to_dict(self):
        return {
            'id': self.id,
            'Nombres': self.Nombres,
            'Correo': self.Correo
        }

class CodigoVerificacion(db.Model):
    __tablename__ = 'CodigoVerificacion'
    
    # NOTA: SQLAlchemy requiere una Primary Key obligatoriamente     
    idCliente = db.Column(db.Integer, db.ForeignKey('Cliente.id'), primary_key=True)
    Codigo = db.Column(db.String(4), nullable=False, primary_key=True) # PK compuesta
    FechaCaducidad = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'idCliente': self.idCliente,
            'Codigo': self.Codigo,
            'FechaCaducidad': self.FechaCaducidad.strftime('%Y-%m-%d %H:%M:%S')
        }