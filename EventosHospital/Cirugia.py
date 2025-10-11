from Modelos.Eventos import Evento
from datetime import datetime, timedelta
from Enums import TipoRecurso, TipoEvento
from typing import Dict
import time
from Examen import ExamenMedico

class Cirugia(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, paciente: str, 
                 complejidad: str, requiere_examen: bool = True):
        if complejidad == "alta":
            duracion = timedelta(seconds=22)
        elif complejidad == "media":
            duracion = timedelta(seconds=18)
        else:  # baja
            duracion = timedelta(seconds=15)
            
        super().__init__(id, nombre, TipoEvento.CIRUGIA, inicio, inicio + duracion, paciente)
        self.complejidad = complejidad
        self.requiere_examen = requiere_examen

        if requiere_examen:
            self.crear_examen_previo()
    
    def crear_examen_previo(self):
        """Crea automáticamente el examen médico previo a la cirugía"""

        inicio_examen = self.inicio - timedelta(seconds=14)
        examen = ExamenMedico(
            id=f"EXAM_{self.id}",
            nombre=f"Examen pre-quirúrgico para {self.nombre}",
            inicio=inicio_examen,
            paciente=self.paciente,
            tipo_examen="pre-operatorio"
        )
        self.set_evento_previo(examen)
    
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        recursos = {
            TipoRecurso.QUIROFANO: 1,
            TipoRecurso.CIRUJANO: 1,
            TipoRecurso.DOCTOR: 1,
            TipoRecurso.ENFERMEROS: 2,  
            TipoRecurso.INSTRUMENTAL: 1
        }
        
        if self.complejidad == "alta":
            recursos[TipoRecurso.ENFERMEROS] = 4
            recursos[TipoRecurso.CIRUJANO] = 2 
        
        return recursos
    
    def ejecutar(self):
        """Simula la ejecución de la cirugía"""
        print(f"🔪 Iniciando cirugía {self.nombre} para {self.paciente}...")
        tiempo_espera = (self.fin - self.inicio).total_seconds()
        time.sleep(tiempo_espera)
        print(f"✅ Cirugía {self.nombre} completada para {self.paciente}")
        self.estado = "Completado"
    
    def to_dict(self):
        data = super().to_dict()
        data['complejidad'] = self.complejidad
        data['requiere_examen'] = self.requiere_examen
        return data