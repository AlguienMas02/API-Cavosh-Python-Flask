from flask import Blueprint
from src.controllers.clienteController import ClienteController

cliente_bp = Blueprint('cliente_bp', __name__)

cliente_bp.route('/login', methods=['POST'])(ClienteController.login)
cliente_bp.route('/registrar', methods=['POST'])(ClienteController.registrar)
cliente_bp.route('/generar_codigo', methods=['POST'])(ClienteController.generarCodigo)
cliente_bp.route('/validar_codigo', methods=['POST'])(ClienteController.validarCodigo)


