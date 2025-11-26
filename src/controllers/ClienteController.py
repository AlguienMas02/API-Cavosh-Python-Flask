from flask import request, jsonify
import mysql.connector
from sqlalchemy import text
from src.config.db import db;

def getCliente():
    try:
        data = request.json
        correo = data.get('correo')
        password = data.get('password')
        id = 0

        sql = text("CALL sp_getCliente(:id, :correo, :password)")
        result = db.session.execute(sql, {'id': id, 'correo': correo, 'password': password})

        if result:
            cliente = dict(result)
            return jsonify({'mensaje': 'Login exitoso', 'cliente': cliente}), 200
        else:
            return jsonify({'mensaje': 'Credenciales incorrectas'}), 401

    except Exception as e:
        return jsonify({'error': e}), 500



