# Database definition
# Creator:		Yves Huguenin
# Date:			10.11.2019
# $VER:			0.1
#
# Schema for Sqlite3 database
#.########################################################

DROP TABLE IF EXISTS T_tank_list;
CREATE TABLE T_tank_list 
(
	serial 				int 						NOT NULL UNIQUE,
	type 				int 						NOT NULL,
	capacite 			int 						NOT NULL,
	hauteur 			float 					NOT NULL,
	produit 			int 						DEFAULT NULL,
	localisation		tinytext 				DEFAULT NULL,
	rem_max 		float 					DEFAULT NULL,
	min_alarm 		float 					DEFAULT NULL,
	min_hors 			varchar(45) 		DEFAULT NULL
);

DROP TABLE IF EXISTS T_produits
CREATE TABLE T_produits 
(
	id_produits	 	INT 						NOT NULL,
	langue 			VARCHAR(5) 		NOT NULL,
	desciption		VARCHAR(45) 	NOT NULL
);
