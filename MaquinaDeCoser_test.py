from MaquinaCoser import MaquinaDeCoser
import pytest

def test_encender(estado=True):
    maquina = MaquinaDeCoser(1,10,700,"cadeneta",1)
    resultado = maquina.encender(estado)
    assert resultado == "La Maquina de coser esta encendida"
    
    
def test_coser_algodon():
        maquina = MaquinaDeCoser(1,10,700,"cadeneta",1)
        maquina.encender(True)
        maquina._tipo_tela = 1
        resultado = maquina.coser()
        assert(resultado, "El tipo de tela es algodón y el tipo de puntada es Cadeneta")

def test_coser_cuero():
        maquina = MaquinaDeCoser(1,10,700,"Overlock",2)   
        maquina.encender(True)
        maquina._tipo_tela = 2
        resultado = maquina.coser()
        assert(resultado, "El tipo de tela es cuero y el tipo de puntada es Overlock")    

def test_coser_lino():
        maquina = MaquinaDeCoser(1,10,700,"zigzag",3)   
        maquina.encender(True)
        maquina._tipo_tela = 3
        resultado = maquina.coser()
        assert(resultado, "El tipo de tela es lino y el tipo de puntada es zigzag")  
 
def test_coser_apagada():
        maquina = MaquinaDeCoser(1,10,700,"zigzag",3)
        maquina.encender(False)
        resultado = maquina.coser()
        assert(resultado, "La Maquina está apagada, encenderla para trabajar")              
def test_ajustar_velocidad_dentro_del_rango():
        maquina = MaquinaDeCoser(1,10,1000,"zigzag",3)
        resultado = maquina.ajustar_velocidad(500)  
        assert(resultado, f"La maquina velocidad ha sido ajustada a 500 puntadas por minutos")
        assert(maquina._velocidad_actual, 500)


def test_ajustar_velocidad_fuera_del_rango():
        maquina = MaquinaDeCoser(1,10,1000,"zigzag",3)
        resultado = maquina.ajustar_velocidad(1500)  
        assert(resultado, f"La velocidad supera la maxima tolerada, la velocidad maxima permitida es 1000")

def test_ajustar_velocidad_inicial():
        maquina = MaquinaDeCoser(1,300,1000,"zigzag",3)
        resultado = maquina.ajustar_velocidad(400)  
        assert(resultado, f"La velocidad ha sido ajustada a 400 puntadas por minutos")
        assert(maquina._velocidad_actual, 400)        
     
        