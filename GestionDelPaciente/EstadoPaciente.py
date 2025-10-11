from Enums import EstadoPaciente, TipoEvento
from Modelos.Eventos import Evento
from datetime import datetime, timedelta

class PacienteEnEspera:
    def __init__(self, paciente_id: str, nombre: str, evento: 'Evento', 
                 hora_llegada: datetime):
        self.paciente_id = paciente_id
        self.nombre = nombre
        self.evento = evento
        self.hora_llegada = hora_llegada
        self.prioridad = 0 if evento.tipo == TipoEvento.URGENCIA else 1 
        self.estado = EstadoPaciente.ESPERANDO
        self.tiempo_espera = timedelta(0)
    
    def actualizar_tiempo_espera(self):
        """Actualiza el tiempo de espera del paciente"""
        self.tiempo_espera = datetime.now() - self.hora_llegada
    
    def to_dict(self) -> dict:
        return {
            'paciente_id': self.paciente_id,
            'nombre': self.nombre,
            'evento': self.evento.to_dict(),
            'hora_llegada': self.hora_llegada.isoformat(),
            'prioridad': self.prioridad,
            'estado': self.estado.value,
            'tiempo_espera_minutos': int(self.tiempo_espera.total_seconds() / 60),
            'es_urgencia': self.prioridad == 0  
        }