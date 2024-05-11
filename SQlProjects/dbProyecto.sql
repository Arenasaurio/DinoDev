-- MySQL Script generated by MySQL Workbench
-- Fri Apr 26 16:44:43 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema donaciones
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `donaciones` ;

-- -----------------------------------------------------
-- Schema donaciones
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `donaciones` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `donaciones` ;

-- -----------------------------------------------------
-- Table `donaciones`.`voluntario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `donaciones`.`voluntario` (
  `ID_Voluntario` INT NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `Edad` INT NOT NULL,
  `Genero` VARCHAR(1) NOT NULL,
  `CURP` VARCHAR(18) NOT NULL,
  `Estado` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ID_Voluntario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `donaciones`.`organizacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `donaciones`.`organizacion` (
  `ID_Organizacion` INT NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `Direccion` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`ID_Organizacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `donaciones`.`apoyo_organizacion_voluntario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `donaciones`.`apoyo_organizacion_voluntario` (
  `ID_Apoyo` INT NOT NULL AUTO_INCREMENT,
  `ID_Voluntario` INT NOT NULL,
  `ID_Organizacion` INT NOT NULL,
  `Fecha_Inicio` DATE NOT NULL,
  `Fecha_Fin` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`ID_Apoyo`),
  INDEX `ID_Voluntario` (`ID_Voluntario` ASC) VISIBLE,
  INDEX `ID_Organizacion` (`ID_Organizacion` ASC) VISIBLE,
  CONSTRAINT `apoyo_organizacion_voluntario_ibfk_1`
    FOREIGN KEY (`ID_Voluntario`)
    REFERENCES `donaciones`.`voluntario` (`ID_Voluntario`),
  CONSTRAINT `apoyo_organizacion_voluntario_ibfk_2`
    FOREIGN KEY (`ID_Organizacion`)
    REFERENCES `donaciones`.`organizacion` (`ID_Organizacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `donaciones`.`comunidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `donaciones`.`comunidad` (
  `ID_Comunidad` INT NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `Distancia` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`ID_Comunidad`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `donaciones`.`donante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `donaciones`.`donante` (
  `ID_Donante` INT NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `No_Control` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_Donante`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `donaciones`.`zapato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `donaciones`.`zapato` (
  `ID_Zapato` INT NOT NULL,
  `Talla` INT NOT NULL,
  `Tipo` VARCHAR(50) NOT NULL,
  `Color_Principal` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ID_Zapato`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
