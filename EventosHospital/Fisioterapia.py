from Modelos.Eventos import Evento
from datetime import datetime, timedelta
from Enums import TipoRecurso, TipoEvento
from typing import Dict
import time

class Fisioterapia(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, paciente: str, tipo_terapia: str):
        duracion = timedelta(seconds=10)
        super().__init__(id, nombre, TipoEvento.FISIOTERAPIA, inicio, inicio + duracion, paciente)
        self.tipo_terapia = tipo_terapia
    
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        return {
            TipoRecurso.REHABILITACION_FISICA: 1,
            TipoRecurso.FISIOTERAPEUTA: 1,
            TipoRecurso.ENFERMEROS: 1,
            TipoRecurso.INSTRUMENTAL: 1
        }
    
    def ejecutar(self):
        """Simula la ejecución de fisioterapia"""
        print(f"💪 Iniciando fisioterapia para {self.paciente}...")
        tiempo_espera = (self.fin - self.inicio).total_seconds()
        time.sleep(tiempo_espera)
        print(f"✅ Fisioterapia completada para {self.paciente}")
        self.estado = "Completado"
    
    def to_dict(self):
        data = super().to_dict()
        data['tipo_terapia'] = self.tipo_terapia
        return data