SELECT * FROM autores;
SELECT * FROM cliente;
SELECT * FROM emprestimo;
SELECT * FROM genero;
SELECT * FROM livro;
SELECT * FROM livro_has_autores;
SELECT * FROM livro_has_genero;
SELECT * FROM usuario;


INSERT INTO autores(nome) 
VALUES ('J. K. Rowling');

INSERT INTO cliente(nome,cpf,bairro,rua,numero,cidade,estado,data_nascimento) 
VALUES ('João Vítor de Paiva Moreira','123.123.123-12','Jardim das hortencias','Rua Antonio Bueno de Almeida','50','Monte Belo','MG','2001-07-26');

INSERT INTO genero(nome)
VALUES('Fantasia');

INSERT INTO livro(nome) 
VALUES('Harry Potter e o Calice de Fogo');

INSERT INTO livro_has_autores(livro_id,autores_id) 
VALUES(1,1);

INSERT INTO livro_has_genero(livro_id,genero_id) 
VALUES(1,1);

INSERT INTO usuario(login,senha,nome) 
VALUES('admin','admin','admin');

INSERT INTO emprestimo(devolvido,data_emprestimo,data_devolucao,data_estimada_devolucao,usuario_id,cliente_id,livro_id) 
VALUES(0,'2022-10-25',NULL,'2022-11-08',1,1,1);

-- --------------------------------------------------------------------------------------------------------------------------------------------

UPDATE emprestimo SET devolvido = 1,data_devolucao='2022-11-05' WHERE id = 1

-- --------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO autores(nome) 
VALUES ('Rick Riordan');

INSERT INTO livro(nome) 
VALUES('Percy Jackson e o Ladrão de Raios');

INSERT INTO livro_has_autores(livro_id,autores_id) 
VALUES(2,2);

INSERT INTO livro_has_genero(livro_id,genero_id) 
VALUES(2,1);

INSERT INTO emprestimo(devolvido,data_emprestimo,data_devolucao,data_estimada_devolucao,usuario_id,cliente_id,livro_id) 
VALUES(0,'2022-11-06',NULL,'2022-11-20',1,1,2);