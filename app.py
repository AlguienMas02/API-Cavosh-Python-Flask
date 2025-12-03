from flask import Flask
from src.config.db import Config
from src.models.cliente import db
from src.routes.clienteRoutes import cliente_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(cliente_bp, url_prefix='/api')

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)

