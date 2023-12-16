CREATE DATABASE IF NOT EXISTS BANQUES;

USE BANQUES;

CREATE TABLE IF NOT EXISTS compte(
	code_compte VARCHAR(50),
    type_compte VARCHAR(20),
    nom VARCHAR(20) NOT NULL,
    prenom VARCHAR(20) NOT NULL,
    email VARCHAR(50),
    num_tel VARCHAR(50) NOT NULL,
    mdp TEXT NOT NULL,
    pays VARCHAR(50) NOT NULL,
    ville VARCHAR(50) NOT NULL,
    quartier VARCHAR(50) NOT NULL,
    residence TEXT NOT NULL,
    proffesion VARCHAR(255) NOT NULL,
    date_creation DATETIME,
    solde_initial DOUBLE DEFAULT 0,
    solde DOUBLE,
    PRIMARY KEY(code_compte)
);

CREATE TABLE IF NOT EXISTS transactions(
	numero VARCHAR(50),
    code_compte VARCHAR(20) NOT NULL,
    date_transaction DATETIME NOT NULL,
    type_transaction CHAR NOT NULL,
    motif_transaction TEXT NOT NULL,
    PRIMARY KEY(numero),
    FOREIGN KEY(code_compte) REFERENCES compte(code_compte)
);