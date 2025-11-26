from src.config.db import db

class Cliente(db.Model):
    __tablename__ = 'Cliente'
    
    id = db.Column(db.Integer, primary_key=True)
    Nombres = db.Column(db.String(30), nullable=False)
    Correo = db.Column(db.String(30), unique=True)
    Passwordd = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombres': self.Nombres,
            'correo': self.Correo
        }



