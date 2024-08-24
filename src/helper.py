from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

class Funciones:
    def __init__(self,archivo):
        self.archivo=archivo

    def crear_conexion_mysql(self):
        try:
            load_dotenv(self.archivo)
            # Leer variables de entorno
            username = os.getenv('DB_USERNAME')
            password = os.getenv('DB_PASSWORD')
            hostname = os.getenv('DB_HOST')
            dbname = os.getenv('DB_NAME')
            # Crear la conexión a la base de datos
            engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/{dbname}?charset=utf8mb4')
            return engine
        except Exception as e:
            print(f"Error: {e}")
            return None
        