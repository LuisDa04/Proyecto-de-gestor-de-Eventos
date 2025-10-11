from Modelos.Eventos import Evento
from datetime import datetime, timedelta
from Enums import TipoRecurso, TipoEvento
from typing import Dict
import time

class ExamenMedico(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, paciente: str, tipo_examen: str):
        duracion = timedelta(seconds=12)
        super().__init__(id, nombre, TipoEvento.EXAMEN, inicio, inicio + duracion, paciente)
        self.tipo_examen = tipo_examen
    
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        return {
            TipoRecurso.EXAMENES: 1,
            TipoRecurso.DOCTOR: 1,
            TipoRecurso.ENFERMEROS: 1,
            TipoRecurso.TECNICOS: 1,
            TipoRecurso.INSTRUMENTAL: 1
        }
    
    def ejecutar(self):
        """Simula la ejecución del examen médico"""
        print(f"🔍 Iniciando examen médico para {self.paciente}...")
        tiempo_espera = (self.fin - self.inicio).total_seconds()
        time.sleep(tiempo_espera)
        print(f"✅ Examen médico completado para {self.paciente}")
        self.estado = "Completado"
    
    def to_dict(self):
        data = super().to_dict()
        data['tipo_examen'] = self.tipo_examen
        return data