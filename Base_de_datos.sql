create database Industria
 Use Industria
 
 CREATE TABLE tipo_telas(
id_tela int AUTO_INCREMENT,
descripcion varchar(20) NOT NULL,
CONSTRAINT pk_tipos_telas PRIMARY KEY(id_tela)
)
CREATE TABLE modelos(
id_serie int auto_increment,
descripcion varchar(20) not null,
constraint pk_modelos PRIMARY KEY(id_serie)
);

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

INSERT INTO modelos (descripcion)
           values("serger")
INSERT INTO modelos (descripcion)
           values("doble punta")      
INSERT INTO modelos (descripcion)
           values("Brother")    
 
 INSERT INTO tipo_telas(descripcion)
                    values("algodon")
                    
   INSERT INTO tipo_telas(descripcion)
                   values("cuero")  
    INSERT INTO tipo_telas(descripcion)                
                    values("lino")
   INSERT INTO tipo_telas(descripcion)                
                    values("modal")                   
                   
   INSERT INTO MaquinaDeCoser(modelo,velocidad_actual,velocidad_maxima,tipo_puntada,tipo_tela )
                      values( 1,10,700,"cadeneta",1)
   INSERT INTO MaquinaDeCoser(modelo,velocidad_actual,velocidad_maxima,tipo_puntada,tipo_tela )
                      values( 2,20,800,"zigzag",2)  
   INSERT INTO MaquinaDeCoser(modelo,velocidad_actual,velocidad_maxima,tipo_puntada,tipo_tela )
                      values( 3,15,750,"overlock",3)                  
                    
select id_serie,descripcion from modelos where id_serie=1    

select avg(velocidad_maxima) as promedio from MaquinaDeCoser

select t.descripcion as tipo_tela,m.descripcion  as modelo,tipo_puntada,velocidad_actual,velocidad_maxima from tipo_telas as t
join MaquinaDeCoser as maq on t.id_tela=maq.tipo_tela 
join modelos  as m on  m.id_serie= maq.modelo

select descripcion,velocidad_actual,velocidad_maxima from MaquinaDeCoser,modelos 
where modelos.id_serie=MaquinaDeCoser.modelo and velocidad_maxima < 900

select descripcion ,id_coser as maquina from modelos,MaquinaDeCoser
where modelos.id_serie=MaquinaDeCoser.id_coser                 
                    