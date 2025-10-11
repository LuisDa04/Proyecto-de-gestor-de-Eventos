from Modelos.Eventos import Evento
from datetime import datetime, timedelta
from Enums import TipoEvento, TipoRecurso
from typing import Dict
import time

class Consulta(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, paciente: str, tipo_consulta: str):
        duracion = timedelta(seconds=8)
        super().__init__(id, nombre, TipoEvento.CONSULTA, inicio, inicio + duracion, paciente)
        self.tipo_consulta = tipo_consulta
    
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        return {
            TipoRecurso.CONSULTA: 1,
            TipoRecurso.DOCTOR: 1,
            TipoRecurso.ENFERMEROS: 1,
            TipoRecurso.INSTRUMENTAL: 1
        }
    
    def ejecutar(self):
        """Simula la ejecución de una consulta"""
        print(f"🩺 Iniciando consulta para {self.paciente}...")
        tiempo_espera = (self.fin - self.inicio).total_seconds()
        time.sleep(tiempo_espera)
        print(f"✅ Consulta completada para {self.paciente}")
        self.estado = "Completado"
    
    def to_dict(self):
        data = super().to_dict()
        data['tipo_consulta'] = self.tipo_consulta
        return data