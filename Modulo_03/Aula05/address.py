import sqlite3
from database import DatabaseConnection


class AddressModel:
    """Gerencia a tabela 'enderecos'."""

    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn
        self._create_table()

    def _create_table(self):
        """Cria a tabela de endereços."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS enderecos (
                id_address INTEGER PRIMARY KEY AUTOINCREMENT,
                endereco TEXT NOT NULL UNIQUE
                
            );
            """
        )
        self.db_conn.close()

    def create_address(self, endereco):
        """Cria um novo endereço."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                "INSERT INTO enderecos (endereco) VALUES (?);",
                (endereco,),
            )
            print(f"[SUCESSO] Endereço: '{endereco}' inserido.")
        except sqlite3.IntegrityError:
            print(f"[ERRO] Endereço: '{endereco}' já existe.")
        finally:
            self.db_conn.close()

    def get_students_by_address(self, id_address):
        """
        Retorna todos os alunos associados ao endereço informado.
        Observação: assume que a tabela `alunos` tem a coluna `id_address`.
        """
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            "SELECT id, nome, email, id_address FROM alunos WHERE id_address = ?;",
            (id_address,),
        )
        students = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return students
