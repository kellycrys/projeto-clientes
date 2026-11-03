from config.database import Database
import psycopg2.extras

class ClienteRepository:
    def inserir(self, cliente):
        conexao = Database.get_connection()
        if not conexao:
            return None
        cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql = """
            INSERT INTO clientes 
            (tipo, nome, cpf, cnpj, razao_social, whatsapp, email, cidade, estado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        valores = (
            cliente.get("tipo"),
            cliente.get("nome"),
            cliente.get("cpf"),
            cliente.get("cnpj"),
            cliente.get("razao_social"),
            cliente.get("whatsapp"),
            cliente.get("email"),
            cliente.get("cidade"),
            cliente.get("estado")
        )
        try:
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()
            conexao.commit()
            if resultado:
                cliente["id"] = resultado["id"]
            return cliente
        except Exception as e:
            print(f"Erro ao inserir cliente: {e}")
            return None
        finally:
            cursor.close()
            conexao.close()

    def buscar_todos(self):
        conexao = Database.get_connection()
        if not conexao:
            return []
        cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            cursor.execute("SELECT * FROM clientes ORDER BY id DESC")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar clientes: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

    def buscar_filtrados(self, tipo=None, cidade=None, estado=None):
        conexao = Database.get_connection()
        if not conexao:
            return []
        cursor = conexao.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        condicoes = []
        valores = []
        if tipo:
            condicoes.append("tipo = %s")
            valores.append(tipo)
        if cidade:
            condicoes.append("cidade ILIKE %s")
            valores.append(f"%{cidade}%")
        if estado:
            condicoes.append("estado = %s")
            valores.append(estado)
        sql = "SELECT * FROM clientes"
        if condicoes:
            sql += " WHERE " + " AND ".join(condicoes)
        sql += " ORDER BY id DESC"
        try:
            cursor.execute(sql, tuple(valores))
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar clientes filtrados: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, id_cliente, cliente):
        conexao = Database.get_connection()
        if not conexao:
            return False
        cursor = conexao.cursor()
        sql = """
            UPDATE clientes 
            SET tipo = %s, nome = %s, cpf = %s, cnpj = %s, 
                razao_social = %s, whatsapp = %s, email = %s, 
                cidade = %s, estado = %s
            WHERE id = %s
        """
        valores = (
            cliente.get("tipo"),
            cliente.get("nome"),
            cliente.get("cpf"),
            cliente.get("cnpj"),
            cliente.get("razao_social"),
            cliente.get("whatsapp"),
            cliente.get("email"),
            cliente.get("cidade"),
            cliente.get("estado"),
            id_cliente
        )
        try:
            cursor.execute(sql, valores)
            conexao.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def remover(self, id_cliente):
        conexao = Database.get_connection()
        if not conexao:
            return False
        cursor = conexao.cursor()
        try:
            cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao remover cliente: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()
