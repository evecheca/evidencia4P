create database Industria
 Use Industria

Create table MaquinaDeCoser(
id_coser int auto_increment,
modelo int not null,
velocidad_actual int,
velocidad_maxima int not null,
tipo_puntada varchar(20),
tipo_tela int,
constraint maquinacoser_id_pk PRIMARY KEY(id_coser),
constraint maquinacoser_modelos FOREIGN KEY(MODELO)
REFERENCES modelos(id_serie),
constraint maquinacoser_telas_fk FOREIGN KEY(tipo_tela) 
REFERENCES tipo_telas(id_tela)
)