from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db

# db = SQLAlchemy()

class Venta(db.Model):
    __tablename__ = 'venta'
    
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Venta {self.producto} - {self.fecha}>"
