import json

from flask import Blueprint, Response, request
ROUTINES = Blueprint('routines', __name__)
from app.models.type_execirse import Type_Exercise
from app.models.exercise import Exercise
from app.services import type_exercise_service, exercise_service


@ROUTINES.route('/health', methods=['GET', 'OPTIONS'])
def index():
    """Health of application"""
    return Response(json.dumps({'Status': 'OK'}))

@ROUTINES.route('/createtypeexercise', methods=['POST'])
def create_type_exercise():
    request_body = request.json
    type_id = request_body['type_id']
    dsc_tipo = request_body['dsc_tipo']
    type_exercise = Type_Exercise(id_tipo_ejercicio=type_id, dsc_tipo_ejercicio= dsc_tipo)
    try:
        type_exercise_service.save_type_exercise(type_exercise)
        response = json.dumps({"Message":"Creado satisfactoriamente"}), 200
        return response
    except Exception as e:
        print('Error: ',e)
        raise e

@ROUTINES.route('/createexercise', methods=['POST'])
def create_exercise():
    request_body = request.json
    id_ejercicio = request_body['id_ejercicio']
    id_tipo_ejercicio = request_body['id_tipo_ejercicio']
    nombre_ejercicio = request_body['nombre_ejercicio']
    dsc_ejercicio = request_body['dsc_ejercicio']
    exercise = Exercise(id_ejercicio=id_ejercicio, id_tipo_ejercicio=id_tipo_ejercicio,
                        nombre_ejercicio=nombre_ejercicio, dsc_ejercicio=dsc_ejercicio)
    try:
        exercise_service.save_exercise(exercise)
        response = json.dumps({"Message": "Creado satisfactoriamente"}), 200
        return response
    except Exception as e:
        print('Error:', e)
        raise e