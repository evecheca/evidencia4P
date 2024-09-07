select id_serie,descripcion from modelos where id_serie=1
select t.descripcion as tipo_tela,m.descripcion  as modelo,tipo_puntada,velocidad_actual,velocidad_maxima from tipo_telas as t
join MaquinaDeCoser as maq on t.id_tela=maq.tipo_tela 
join modelos  as m on  m.id_serie= maq.modelo

select avg(velocidad_maxima) as promedio from MaquinaDeCoser
select descripcion,velocidad_actual,velocidad_maxima from MaquinaDeCoser,modelos 
where modelos.id_serie=MaquinaDeCoser.modelo and velocidad_maxima < 900

select descripcion ,id_coser as maquina from modelos,MaquinaDeCoser
where modelos.id_serie=MaquinaDeCoser.id_coser 