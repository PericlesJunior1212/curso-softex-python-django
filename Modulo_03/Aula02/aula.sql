-- Active: 1759941948462@@127.0.0.1@3306
CREATE TABLE alunos (
    id integer primary key,
    nome text not null,
    idade integer
);

INSERT INTO alunos (nome, idade) VALUES ('João', 20);
INSERT INTO alunos (nome, idade) VALUES ('Maria', 28);

SELECT * FROM alunos;
SELECT nome, idade from alunos;

SELECT * FROM alunos WHERE nome= 'Maria' and idade=28;

UPDATE alunos SET idade = 21 WHERE nome = 'João';

DELETE FROM alunos where nome = 'Maria';
DELETE FROM alunos where id= 9 or id = 7 or id = 10;