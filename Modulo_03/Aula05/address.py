import sqlite3
from database import DatabaseConnection


class CourseModel:
    """Gerencia a tabela endereços."""

    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn
        self._create_table()

    def _create_table(self):
        """Cria a tabela de endereços."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS enderecos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endereco TEXT NOT NULL UNIQUE,
                
            );
        """
        )
        self.db_conn.close()

    def create_address(self, endereco):
        """Cria um novo endereço."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                "INSERT INTO endereco (endereco) VALUES (?,);",
                (endereco),
            )
            print(f"[SUCESSO] Endereço: '{endereco}' inserido ao aluno.")
        except sqlite3.IntegrityError:
            print(f"[ERRO] Endereço: '{endereco}' já inserido ao um aluno.")
        finally:
            self.db_conn.close()
            
        def get_students_by_course(self, id_):
        """Busca todos os alunos matriculados em um curso específico.
        (Consulta N:N - Curso -> Alunos)
        """
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            SELECT a.id, a.nome, a.email, m.data_matricula
            FROM alunos a
            INNER JOIN matriculas m ON a.id = m.id_aluno
            WHERE m.id_curso = ?;
            """,
            (id_curso,),
        )
        students = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return students
