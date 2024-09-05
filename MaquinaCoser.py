from MaquinaCoser import Class


Class MaquinaDeCoser():  
    
   
 def __init__(self,modelo, velocidad,tipo_puntada,tipo_tela, estado):
    
    self._modelo=modelo
    self._velocidad_actual=velocidad
    self._velocidad_maxima=velocidad
    self._tipo_puntada=tipo_puntada
    self._tipo_tela=tipo_tela
    self._estado=estado
 
def _str_(self):
    return f"La Maquina de Coser Industrial es { self._modelo},{self._tipo_puntada},{self._tipo_tela}"   

def encender_apagar_(self,estado):
    if(self._estado== True):
        self.velocidad_actual = self.velocidad_maxima // 2 # Velocidad inicial media
        return f"La Maquina de coser esta encendida a una velocidad de {self.velocidad_actual}"
    else:
        self.velocidad_actual =0
        return f"La Maquina de coser esta apagado" 

def Coser(self):
    if (self._estado==True and self._tipo_tela=="algodon"):
        self._tipo_puntada="Cadeneta"
        
    elif (self._estado==True and self._tipo_tela=="Cuero"):  
         self._tipo_puntada="overlock"
    elif  (self._estado==True and self._tipo_tela=="lino"): 
          self._tipo_puntada=" zigzag"  
    else:
        return f"La Maquina esta apagada, encenderla para trabajar"      
   
def ajustar_velocidad(self, nueva_velocidad):   
    if(self._estado==True) : 
       if 0 <= nueva_velocidad <= self.velocidad_maxima:
           self.velocidad_actual = nueva_velocidad
           return f"La maquina {self._modelo} velocidad ha sido ajustada a {self.velocidad_actual} puntadaspor minutos"
       else:
           return f"La velocidad supera la maxima tolerada, la velocidad maxima permitida es {self._velocidad_maxima}"
    else:
       return f"La máquina no está encendida. Enciéndala primero para ajustar la velocidad."    
   
   maquina=MaquinaDeCoser(10,cadeneta,algodon,true)