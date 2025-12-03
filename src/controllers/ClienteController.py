from flask import request, jsonify
from src.services.clienteService import ClienteService

class ClienteController:
    
    @staticmethod
    def login():
        data = request.json
        correo = data.get('correo')
        passwordd = data.get('passwordd')

        usuario = ClienteService.login(correo, passwordd)
        
        if usuario:
            return {'mensaje': 'Login exitoso', 'usuario': usuario.to_dict()}, 200

