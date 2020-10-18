from flask_login import UserMixin
from sqlalchemy.orm import relationship
from server import db


class Exercise(db.Model, UserMixin):
    __tablename__ = 'ejercicio'

    id_ejercicio = db.Column(db.Integer, primary_key=True)
    id_tipo_ejercicio = db.Column(db.Integer, db.ForeignKey('tipo_ejercicio.id_tipo_ejercicio'))
    nombre_ejercicio = db.Column(db.String(50), nullable=True)
    dsc_ejercicio = db.Column(db.String(200), nullable=True)
    type_exercise = db.relationship('Type_Exercise', back_populates="exercise", cascade="all,delete")