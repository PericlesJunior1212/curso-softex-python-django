-- Active: 1759941948462@@127.0.0.1@3306
-- Active: 1759941948462@@127.0.0.1@3306
CREATE TABLE usuarios (
    id integer primary key,
    primeiro_nome text not null,
    sobrenome text not null,
    email TEXT NOT NULL,
    senha INT
);

CREATE TABLE postagens (
    id integer primary key,
    titulo text not null,
    postagem text not null,
    id_autor INT
);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Pericles', 'Junior', 'pericles@gmail.com', 1324);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Jherika', 'Silva', 'jherika@gmail.com', 1894);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Gean', 'Carlos', 'gean@gmail.com', 12634);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Amanda', 'Junior', 'amanda@gmail.com', 4636);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Carlos', 'Pinto', 'carlos@gmail.com', 4698);


INSERT INTO postagens(titulo, postagem, id_autor) VALUES('BadBoy', 'y548j', 4632),
('Velozes', 'k45663k', 9856),
('Cara a Cara', 'q4546qh', 8932),
('Duro de Matar','l4563m', 7854),
('Spirit', 'u7823k', 2365);

SELECT * FROM usuarios;
SELECT * FROM postagens;

UPDATE usuarios SET primeiro_nome = 'Carol' WHERE email = 'jherika@gmail.com';
UPDATE usuarios SET email = 'jherikagatinha@gmail.com' WHERE email = 'jherika@gmail.com';
UPDATE usuarios SET email = 'carolana@gmail.com' WHERE email = 'jherikagatinha@gmail.com';

DELETE FROM usuarios WHERE id = 2;