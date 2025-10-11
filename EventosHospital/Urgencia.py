from Modelos.Eventos import Evento
from datetime import datetime, timedelta
from Enums import TipoRecurso, TipoEvento
from typing import Dict
from Terapia import Terapia
import time

class Urgencia(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, paciente: str, gravedad: str, sistema_hospital=None):
        if gravedad == "critica":
            duracion = timedelta(seconds=12)
        else:
            duracion = timedelta(seconds=7)
            
        super().__init__(id, nombre, TipoEvento.URGENCIA, inicio, inicio + duracion, paciente, sistema_hospital)
        self.gravedad = gravedad
        self.requiere_terapia = (gravedad == "critica")
        
        # Si es crítica, crear automáticamente terapia posterior
        if self.requiere_terapia:
            self.crear_terapia_posterior()
    
    def crear_terapia_posterior(self):
        """Crea automáticamente terapia intensiva después de la urgencia crítica"""
        inicio_terapia = self.fin + timedelta(seconds=2)
        
        self.evento_posterior = Terapia(
            id=f"TER_{self.id}",
            nombre=f"Terapia post-urgencia para {self.nombre}",
            inicio=inicio_terapia,
            paciente=self.paciente,
            tipo_terapia="intensiva",
            gravedad_urgencia=self.gravedad,
            sistema_hospital=self.sistema_hospital 
        )
    
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        recursos = {
            TipoRecurso.CONSULTA: 1,
            TipoRecurso.DOCTOR: 1,
            TipoRecurso.ENFERMEROS: 2,
            TipoRecurso.INSTRUMENTAL: 1
        }
        
        if self.gravedad == "critica":
            recursos[TipoRecurso.ENFERMEROS] = 4
            recursos[TipoRecurso.DOCTOR] = 2
        
        return recursos
    
    def ejecutar(self):
        """Ejecuta la urgencia y si es crítica, programa la terapia automáticamente"""
        print(f"🚨 ATENCIÓN URGENCIA para {self.paciente} - Gravedad: {self.gravedad}")
        tiempo_espera = (self.fin - self.inicio).total_seconds()
        time.sleep(tiempo_espera)
        print(f"✅ Urgencia atendida para {self.paciente}")
        self.estado = "Completado"
        
        # Si es crítica y tiene terapia posterior, PROGRAMARLA AHORA SÍ
        if hasattr(self, 'evento_posterior') and self.evento_posterior and self.sistema_hospital:
            print(f"🔄 Programando terapia intensiva para {self.paciente}...")
            
            # Planificar la terapia en el sistema
            resultado = self.sistema_hospital.planificar_evento_directo(
                self.evento_posterior, 
                f"PAC_{self.id}", 
                self.paciente
            )
            
            if resultado['exitoso']:
                print(f"   ✅ Terapia planificada exitosamente")
            else:
                print(f"   ❌ Error al planificar terapia: {resultado['mensaje']}")
    
    def to_dict(self):
        data = super().to_dict()
        data['gravedad'] = self.gravedad
        data['requiere_terapia'] = self.requiere_terapia
        if hasattr(self, 'evento_posterior'):
            data['evento_posterior'] = self.evento_posterior.id
        return data