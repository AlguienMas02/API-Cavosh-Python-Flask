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
        else:
            return {'error': 'Datos incorrectos'}, 401

    @staticmethod
    def guardar():
        data = request.json
        _id = data.get('id', 0)
        nombre = data.get('nombres')
        correo = data.get('correo')
        passwordd = data.get('passwordd')

        response = ClienteService.registrar_o_actualizar(_id, nombre, correo, passwordd)
        
        if 'error' in response:
            return jsonify(response), 404
            
        # Agregamos mensaje de éxito para el frontend
        response['mensaje'] = 'Código generado'
        return response, 200
    
    @staticmethod
    def validarCodigo():
        data = request.json
        _id = data.get('id')
        _codigo = data.get('codigo')
            
        response = ClienteService.validar_codigo(_id, _codigo)
        
        if 'error' in response:
            return response, 404
            
        if not response.get('valido'):
            return response, 400
            
        return response, 200
                
        
        
        