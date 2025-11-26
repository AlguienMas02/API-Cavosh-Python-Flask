from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db_uri():
    return 'mysql+mysqlconnector://root:@localhost:3306/CavoshCafe'