from datetime import datetime, timedelta
from src.models.cliente import db, Cliente, CodigoVerificacion
import random

class ClienteService:
    
    @staticmethod
    def login(correo, passwordd):
        return Cliente.query.filter_by(Correo=correo, Passwordd=passwordd).first()
    
    @staticmethod
    def registrar(id_cliente, nombre, correo, passwordd):
        if id_cliente == 0:
            query = Cliente.query.filter_by(Correo=correo).first()
            
            if query:
                return {'error': 'Correo ya registrado'}

            cliente = Cliente(Nombres=nombre, Correo=correo, Passwordd=passwordd)
            db.session.add(cliente)
            db.session.commit()
            return {'mensaje': 'Cliente registrado', 'insertID': cliente.id, 'status': 201}
        
        else:
            cliente = Cliente.query.get(id_cliente)
            if not cliente:
                return {'error': 'Cliente no esta registrado'}

            cliente.Nombres = nombre
            cliente.Correo = correo
            cliente.Passwordd = passwordd
            db.session.commit()
            return {'mensaje': 'Cliente actualizado correctamente', 'status': 200}

    @staticmethod
    def generarCodigo(correo):
        cliente = Cliente.query.filter_by(Correo=correo).first()
        
        if not cliente:
            return {'error': 'Correo no está registrado'}

        fecha_add = datetime.now() + timedelta(minutes=15)
        codigo = str(random.randint(1000, 9999))
        
        nuevoCodigo = CodigoVerificacion(
            idCliente = cliente.id,
            Codigo = codigo,
            FechaCaducidad = fecha_add
        )
        db.session.add(nuevoCodigo)
        db.session.commit()
        
        return {'id': cliente.id, 'codigo': codigo}
    
    @staticmethod
    def validarCodigo(id_cliente, codigo):
        ingreso = CodigoVerificacion.query.filter_by(idCliente=id_cliente, Codigo=str(codigo)).first()
        
        if not ingreso:
            return {'error': 'Codigo incorrecto'}
        
        ahora = datetime.now()
        diferencia = ingreso.FechaCaducidad - ahora
        
        if diferencia < 0:
            return {'estado': 'Vencido', 'mensaje': "Codigo caducado", 'valido': False}
        
        return {'estado': 'Valido', 'mensaje': "Codigo verificado", 'valido': True}




