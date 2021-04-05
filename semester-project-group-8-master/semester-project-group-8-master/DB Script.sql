-- MySQL Script generated by MySQL Workbench
-- Mon Mar 22 12:58:34 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`PROFESSOR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PROFESSOR` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `FName` VARCHAR(15) NULL,
  `LName` VARCHAR(15) NOT NULL,
  `Prof_Type` VARCHAR(6) NULL,
  `Internal_ID` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `Internal_ID_UNIQUE` (`Internal_ID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CLASS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CLASS` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Program` VARCHAR(10) NULL,
  `Cat_Num` VARCHAR(10) NULL,
  `Name` VARCHAR(45) NULL,
  `Seats` INT NULL,
  `Credit Hours` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ROOM`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ROOM` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Building` VARCHAR(15) NULL,
  `Number` VARCHAR(10) NULL,
  `Capacity` INT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PROF_PREFERENCES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PROF_PREFERENCES` (
  `ProfID` INT NOT NULL,
  `Pref_Type` VARCHAR(6) NOT NULL,
  `Start` TIMESTAMP NOT NULL,
  `End` TIMESTAMP NOT NULL,
  INDEX `ProfID_idx` (`ProfID` ASC) VISIBLE,
  CONSTRAINT `ProfID`
    FOREIGN KEY (`ProfID`)
    REFERENCES `mydb`.`PROFESSOR` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SECTION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SECTION` (
  `Class` INT NOT NULL,
  `Section` INT NOT NULL,
  `Prof_id` INT NULL,
  `Room_id` INT NULL,
  `Start` DATETIME NULL,
  `End` DATETIME NULL,
  PRIMARY KEY (`Class`, `Section`),
  INDEX `FK_prof_id_idx` (`Prof_id` ASC) VISIBLE,
  INDEX `FK_room_id_idx` (`Room_id` ASC) VISIBLE,
  CONSTRAINT `FK_prof_id`
    FOREIGN KEY (`Prof_id`)
    REFERENCES `mydb`.`PROFESSOR` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_room_id`
    FOREIGN KEY (`Room_id`)
    REFERENCES `mydb`.`ROOM` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_class_id`
    FOREIGN KEY (`Class`)
    REFERENCES `mydb`.`CLASS` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `mydb` ;

-- -----------------------------------------------------
-- procedure procSelectAllProfessors
-- -----------------------------------------------------

DELIMITER $$
USE `mydb`$$
CREATE PROCEDURE procSelectAllProfessors ()
BEGIN
SELECT * FROM professor;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure procAddProfessor
-- -----------------------------------------------------

DELIMITER $$
USE `mydb`$$
CREATE PROCEDURE procAddProfessor (IN fname VarChar(15), lname VarChar(15), prof_type VarChar(5), interID VarChar(45))
BEGIN
INSERT INTO professor(FName, LName, Prof_Type, Internal_ID) VALUES (fname, lname, prof_type, interID);
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure procDeleteProfByName
-- -----------------------------------------------------

DELIMITER $$
USE `mydb`$$
CREATE PROCEDURE procDeleteProfByName (IN firstname VarChar(15), lastname VarChar(15))
BEGIN
DELETE FROM professor 
WHERE (professor.FName = firstname OR professor.FName IS NULL) AND professor.LName = lastname AND id > -1;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure procDeleteProfByInterID
-- -----------------------------------------------------

DELIMITER $$
USE `mydb`$$
CREATE PROCEDURE procDeleteProfByInterID (IN interID VarChar(45))
BEGIN
DELETE FROM professor 
WHERE professor.Internal_ID = interID AND id > -1;
END$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;