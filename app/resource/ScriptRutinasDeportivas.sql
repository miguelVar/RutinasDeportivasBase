-- -----------------------------------------------------
-- Schema rutinas
-- -----------------------------------------------------
DROP DATABASE IF EXISTS rutinas;
CREATE DATABASE IF NOT EXISTS rutinas;
USE rutinas ;

-- -----------------------------------------------------
-- Table tipo_ejercicio
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tipo_ejercicio (
  ID_TIPO_EJERCICIO SMALLINT(6) NOT NULL,
  DSC_TIPO_EJERCICIO VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (ID_TIPO_EJERCICIO))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table ejercicio
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ejercicio (
  ID_EJERCICIO INT(11) NOT NULL,
  ID_TIPO_EJERCICIO SMALLINT(6) NULL DEFAULT NULL,
  NOMBRE_EJERCICIO VARCHAR(50) NULL DEFAULT NULL,
  DSC_EJERCICIO VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (ID_EJERCICIO),
  CONSTRAINT ejercicio_ibfk_1
    FOREIGN KEY (ID_TIPO_EJERCICIO)
    REFERENCES tipo_ejercicio (ID_TIPO_EJERCICIO))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;