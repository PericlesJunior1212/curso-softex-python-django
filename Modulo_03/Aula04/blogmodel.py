import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel:
  

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        """Método privado para criar a tabela de usuários."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
              CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL UNIQUE,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
                
                
            );
            
            """
        )
        self.db_conn.close()
        
    def create_user(self, titulo, conteudo):
        """Cria uma nova postagem."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO post (titulo, conteudo)
                VALUES (?, ?);
            """,
                (titulo, conteudo),
            )
            print("Postagem criada com sucesso!")
        except sqlite3.IntegrityError:
            print(f"Erro: A postagem '{titulo}' já está em uso.")
        finally:    
        