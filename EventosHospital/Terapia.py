from Modelos.Eventos import Evento
from datetime import datetime, timedelta
from Enums import TipoRecurso, TipoEvento
from typing import Dict
import time

class Terapia(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, paciente: str, 
                 tipo_terapia: str, gravedad_urgencia: str):
        if gravedad_urgencia == "critica":
            duracion = timedelta(seconds=18)
        else:
            duracion = timedelta(seconds=15)
            
        super().__init__(id, nombre, TipoEvento.TERAPIA, inicio, inicio + duracion, paciente)
        self.tipo_terapia = tipo_terapia
        self.gravedad_urgencia = gravedad_urgencia
    
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        recursos = {
            TipoRecurso.UCI: 1, 
            TipoRecurso.DOCTOR: 2,  
            TipoRecurso.ENFERMEROS: 3,  
            TipoRecurso.INSTRUMENTAL: 1
        }
        
        if self.gravedad_urgencia == "critica":
            recursos[TipoRecurso.ENFERMEROS] = 5  
            recursos[TipoRecurso.DOCTOR] = 3  
        
        return recursos
    
    def ejecutar(self):
        print(f"🏥 INICIANDO TERAPIA INTENSIVA para {self.paciente}...")
        print(f"   Tipo: {self.tipo_terapia}, Gravedad: {self.gravedad_urgencia}")
        tiempo_espera = (self.fin - self.inicio).total_seconds()
        time.sleep(tiempo_espera)
        print(f"✅ TERAPIA INTENSIVA completada para {self.paciente}")
        self.estado = "Completado"
    
    def to_dict(self):
        data = super().to_dict()
        data['tipo_terapia'] = self.tipo_terapia
        data['gravedad_urgencia'] = self.gravedad_urgencia
        return data