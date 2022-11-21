-- MySQL Script generated by MySQL Workbench
-- Mon Nov 21 15:30:21 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema biblioteca
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `biblioteca` DEFAULT CHARACTER SET utf8 ;
USE `biblioteca` ;

-- -----------------------------------------------------
-- Table `biblioteca`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` VARCHAR(14) NULL,
  `bairro` VARCHAR(45) NULL,
  `rua` VARCHAR(45) NULL,
  `numero` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `data_nascimento` DATE NULL,
  `bibliotecario` TINYINT NULL,
  `ativo` TINYINT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`livro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livro` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `edicao` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`autor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`livro_has_autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livro_has_autor` (
  `livro_id` INT NOT NULL,
  `autor_id` INT NOT NULL,
  PRIMARY KEY (`livro_id`, `autor_id`),
  INDEX `fk_livro_has_autores_autores1_idx` (`autor_id` ASC) VISIBLE,
  INDEX `fk_livro_has_autores_livro_idx` (`livro_id` ASC) VISIBLE,
  CONSTRAINT `fk_livro_has_autores_livro`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca`.`livro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livro_has_autores_autores1`
    FOREIGN KEY (`autor_id`)
    REFERENCES `biblioteca`.`autor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`genero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`genero` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`livro_has_genero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livro_has_genero` (
  `livro_id` INT NOT NULL,
  `genero_id` INT NOT NULL,
  PRIMARY KEY (`livro_id`, `genero_id`),
  INDEX `fk_livro_has_genero_genero1_idx` (`genero_id` ASC) VISIBLE,
  INDEX `fk_livro_has_genero_livro1_idx` (`livro_id` ASC) VISIBLE,
  CONSTRAINT `fk_livro_has_genero_livro1`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca`.`livro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livro_has_genero_genero1`
    FOREIGN KEY (`genero_id`)
    REFERENCES `biblioteca`.`genero` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`emprestimo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `devolvido` TINYINT NULL,
  `data_emprestimo` DATE NULL,
  `data_devolucao` DATE NULL,
  `data_estimada_devolucao` DATE NULL,
  `usuario_bibliotecario_id` INT NOT NULL,
  `usuario_cliente_id` INT NOT NULL,
  `livro_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_emprestimo_usuario1_idx` (`usuario_bibliotecario_id` ASC) VISIBLE,
  INDEX `fk_emprestimo_livro1_idx` (`livro_id` ASC) VISIBLE,
  INDEX `fk_emprestimo_usuario2_idx` (`usuario_cliente_id` ASC) VISIBLE,
  CONSTRAINT `fk_emprestimo_usuario1`
    FOREIGN KEY (`usuario_bibliotecario_id`)
    REFERENCES `biblioteca`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_emprestimo_livro1`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca`.`livro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_emprestimo_usuario2`
    FOREIGN KEY (`usuario_cliente_id`)
    REFERENCES `biblioteca`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`editora`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`editora` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `biblioteca`.`livro_has_editora`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioteca`.`livro_has_editora` (
  `livro_id` INT NOT NULL,
  `editora_id` INT NOT NULL,
  PRIMARY KEY (`livro_id`, `editora_id`),
  INDEX `fk_livro_has_editora_editora1_idx` (`editora_id` ASC) VISIBLE,
  INDEX `fk_livro_has_editora_livro1_idx` (`livro_id` ASC) VISIBLE,
  CONSTRAINT `fk_livro_has_editora_livro1`
    FOREIGN KEY (`livro_id`)
    REFERENCES `biblioteca`.`livro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_livro_has_editora_editora1`
    FOREIGN KEY (`editora_id`)
    REFERENCES `biblioteca`.`editora` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
