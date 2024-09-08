
class MaquinaDeCoser:   
   
 def __init__(self,modelo, velocidad,tipo_puntada,tipo_tela, estado):
     self._modelo=modelo
     self._velocidad_actual=velocidad
     self._velocidad_maxima=velocidad
     self._tipo_puntada=tipo_puntada
     self._tipo_tela=tipo_tela
     self._estado=estado
 
 def _str_(self):
     return f"La Maquina de Coser Industrial es { self._modelo},{self._tipo_puntada},{self._tipo_tela}"  
 
 def get_velocidad_maxima(self): 
     return self._velocidad_maxima

 def set_velocidad_actual(self,velocidad_actual):
     self._velocidad_actual = velocidad_actual
 
 def get_velocidad_actual(self):
     return self._velocidad_actual    

 
 def encender(self,estado):
       if(self._estado== True):
            return f"La Maquina de coser esta encendida"
       else:  
            return f"La Maquina de coser esta apagada"   
                
         

 def coser(self):
       if (self._estado==True and self._tipo_tela==1):
        self.__tipo_puntada="Cadeneta"
        return f"el tipo de tela es algodon y el tipo de puntada es cadeneta"
       elif (self._estado==True and self._tipo_tela==2):  
         self.__tipo_puntada="overlock"
         return f"el tipo de tela es cuero y el tipo de puntada es overlock"
       elif  (self._estado==True and self._tipo_tela==3): 
          self._tipo_puntada="zigzag"  
          return f" el tipo de tela es lino y el tipo de puntada es zigzag" 
       else:
        return f"La Maquina esta apagada, encenderla para trabajar"      
   
 def ajustar_velocidad(self, nueva_velocidad):   
       if(self._estado==True) : 
        if 0 <= nueva_velocidad <= self.velocidad_maxima:
           self._velocidad_actual = nueva_velocidad
           return f"La maquina {self._modelo} velocidad ha sido ajustada a {self._velocidad_actual} puntadaspor minutos"
        else:
           return f"La velocidad supera la maxima tolerada, la velocidad maxima permitida es {self._velocidad_maxima}"
       else: 
           return f"La máquina no está encendida. Enciéndala primero para ajustar la velocidad."    
   
  