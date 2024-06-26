-- MySQL Script generated by MySQL Workbench
-- Fri Apr 26 16:46:01 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ferreteria
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ferreteria` ;

-- -----------------------------------------------------
-- Schema ferreteria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ferreteria` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `ferreteria` ;

-- -----------------------------------------------------
-- Table `ferreteria`.`producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ferreteria`.`producto` (
  `parte` CHAR(3) NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `color` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`parte`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `ferreteria`.`proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ferreteria`.`proveedor` (
  `prove` CHAR(3) NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `calidad` INT NULL DEFAULT NULL,
  PRIMARY KEY (`prove`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `ferreteria`.`registro_producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ferreteria`.`registro_producto` (
  `prove` CHAR(3) NOT NULL,
  `parte` CHAR(3) NOT NULL,
  `cantidad` INT NOT NULL DEFAULT '0',
  PRIMARY KEY (`prove`, `parte`),
  INDEX `parte` (`parte` ASC) VISIBLE,
  CONSTRAINT `registro_producto_ibfk_1`
    FOREIGN KEY (`prove`)
    REFERENCES `ferreteria`.`proveedor` (`prove`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `registro_producto_ibfk_2`
    FOREIGN KEY (`parte`)
    REFERENCES `ferreteria`.`producto` (`parte`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
