# Database definition
# Creator:		Yves Huguenin
# Date:			09.11.2019
# $VER:			0.1
#
# Schema for Mysql database
#.########################################################

CREATE SCHEMA IF NOT EXISTS ksw_gok;
USE ksw_gok;

DROP TABLE IF EXISTS T_tank_list;
CREATE TABLE `T_tank_list` 
(
	`id` 					int(10) 				unsigned NOT NULL AUTO_INCREMENT,
	`serial` 			int(10) 				unsigned NOT NULL,
	`type` 				int(11) 				NOT NULL,
	`capacite` 		int(11) 				NOT NULL,
	`hauteur` 		float 					NOT NULL,
	`produit` 			int(11) 				DEFAULT NULL,
	`localisation`	tinytext 				DEFAULT NULL,
	`rem_max` 		float 					DEFAULT NULL,
	`min_alarm` 	float 					DEFAULT NULL,
	`min_hors` 		varchar(45) 		DEFAULT NULL,
	PRIMARY KEY (`id`),
	UNIQUE KEY `id_UNIQUE` (`id`),
	UNIQUE KEY `serial_UNIQUE` (`serial`)
);

DROP TABLE IF EXISTS `T_produits`
CREATE TABLE `T_produits` 
(
	`id` 					INT 						UNSIGNED NOT NULL AUTO_INCREMENT,
	`id_produits` 	INT 						NOT NULL,
	`langue` 			VARCHAR(5) 		NOT NULL,
	`desciption`		VARCHAR(45) 	NOT NULL,
	PRIMARY KEY (`id`),
	UNIQUE INDEX `id_UNIQUE` (`id` ASC) 
);
