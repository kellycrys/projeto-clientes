import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        try:
            database_url = os.getenv("DATABASE_URL")
            if database_url:
                conexao = psycopg2.connect(database_url)
            else:
                conexao = psycopg2.connect(
                    host=os.getenv("DB_HOST", "localhost"),
                    port=os.getenv("DB_PORT", "5432"),
                    user=os.getenv("DB_USER", "postgres"),
                    password=os.getenv("DB_PASSWORD", ""),
                    database=os.getenv("DB_NAME", "postgres")
                )
            return conexao
        except psycopg2.Error as erro:
            print(f"[ERRO DE CONEXÃO POSTGRESQL]: {erro}")
            return None
