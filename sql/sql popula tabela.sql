SELECT * FROM autor;
SELECT * FROM emprestimo;
SELECT * FROM editora;
SELECT * FROM genero;
SELECT * FROM livro;
SELECT * FROM livro_has_autor;
SELECT * FROM livro_has_editora;
SELECT * FROM livro_has_genero;
SELECT * FROM usuario;


INSERT INTO autor(nome) 
VALUES ('J. K. Rowling');

INSERT INTO usuario(login,senha,nome,cpf,bairro,rua,numero,cidade,estado,data_nascimento,bibliotecario,ativo) 
VALUES ('joao','teste','João Vítor de Paiva Moreira','123.123.123-12','Jardim das hortencias','Rua Antonio Bueno de Almeida','50','Monte Belo','MG','2001-07-26',0,1);

INSERT INTO genero(nome)
VALUES('Fantasia');

INSERT INTO editora(nome)
VALUES('Scholastic');

INSERT INTO livro(nome,edicao) 
VALUES('Harry Potter e o Calice de Fogo',1);

INSERT INTO livro_has_autor(livro_id,autor_id) 
VALUES(1,1);

INSERT INTO livro_has_editora(livro_id,editora_id) 
VALUES(1,1);

INSERT INTO livro_has_genero(livro_id,genero_id) 
VALUES(1,1);

INSERT INTO usuario(login,senha,nome,cpf,bairro,rua,numero,cidade,estado,data_nascimento,bibliotecario,ativo) 
VALUES ('admin','admin','admin','000.000.000-00','admin','admin','0','admin','admin','1970-01-01',1,1);

INSERT INTO emprestimo(devolvido,data_emprestimo,data_devolucao,data_estimada_devolucao,usuario_bibliotecario_id,usuario_cliente_id,livro_id) 
VALUES(0,'2022-10-25',NULL,'2022-11-08',2,1,1);

-- --------------------------------------------------------------------------------------------------------------------------------------------

UPDATE emprestimo SET devolvido = 1,data_devolucao='2022-11-05' WHERE id = 1;

-- --------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO autor(nome) 
VALUES ('Rick Riordan');

INSERT INTO livro(nome,edicao) 
VALUES('Percy Jackson e o Ladrão de Raios',1);

INSERT INTO livro_has_autor(livro_id,autor_id) 
VALUES(2,2);

INSERT INTO livro_has_editora(livro_id,editora_id) 
VALUES(2,1);

INSERT INTO livro_has_genero(livro_id,genero_id) 
VALUES(2,1);

INSERT INTO emprestimo(devolvido,data_emprestimo,data_devolucao,data_estimada_devolucao,usuario_bibliotecario_id,usuario_cliente_id,livro_id)
VALUES(0,'2022-11-06',NULL,'2022-11-20',2,1,2);

SELECT * FROM autor;
SELECT * FROM emprestimo;
SELECT * FROM editora;
SELECT * FROM genero;
SELECT * FROM livro;
SELECT * FROM livro_has_autor;
SELECT * FROM livro_has_editora;
SELECT * FROM livro_has_genero;
SELECT * FROM usuario;