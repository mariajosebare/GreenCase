CREATE DATABASE green_case;

USE green_case;

CREATE TABLE usuarios (
	IdUsuario VARCHAR(100) PRIMARY KEY,
    Nombre VARCHAR(50),
    Apellido VARCHAR(50),
    Password VARCHAR(255)
);

CREATE TABLE modulos (
    IdModulo VARCHAR(100) PRIMARY KEY,
    IdUsuario VARCHAR(100),
    Temperatura FLOAT DEFAULT 0,
    Humedad FLOAT DEFAULT 0,
    Ventialdor BIT DEFAULT 0,
    Calefactor BIT DEFAULT 0,
    Riego BIT DEFAULT 0,
    MinTemperatura FLOAT DEFAULT 0,
    MaxTemperatura FLOAT DEFAULT 0,
    MinHumedad FLOAT DEFAULT 0,
    MaxHumedad FLOAT DEFAULT 0,
    Prendido BIT DEFAULT 0,
    INDEX ix_usuario_modulo (IdUsuario),
    FOREIGN KEY (IdUsuario) REFERENCES usuarios (IdUsuario)
);