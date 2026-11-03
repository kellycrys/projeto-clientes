import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        try:
            conexao = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                port=int(os.getenv("DB_PORT", 3306)),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=os.getenv("DB_NAME", "clientes_db")
            )
            return conexao
        except mysql.connector.Error as erro:
            print(f"[ERRO DE CONEXÃO MYSQL]: {erro}")
            return None
