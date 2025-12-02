from flask import Blueprint, request, jsonify
from src.models.cliente import db, Cliente, CodigoVerificacion
from datetime import datetime, timedelta
import random

cliente_bp = Blueprint('cliente_bp', __name__)

@cliente_bp.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify(clientes)


@cliente_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    correo = data.get('correo')
    passwordd = data.get('passwordd')

    #Igual a select * from Cliente where Correo = _correo and Passwordd = _passwordd;
    usuario = Cliente.query.filter_by(Correo=correo, Passwordd=passwordd).first()

    if usuario:
        return {'message': 'Login exitoso', 'usuario': usuario.to_dict()}, 200
    else:
        return {'error': 'Credenciales incorrectas'}, 401



