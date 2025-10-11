from abc import ABC, abstractmethod
from Enums import TipoEvento, TipoRecurso
from typing import Dict
from datetime import datetime

class Evento(ABC):
    @abstractmethod
    def __init__(self, id: str, nombre: str, tipo: TipoEvento, 
                 inicio: datetime, fin: datetime, paciente: str):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.inicio = inicio
        self.fin = fin
        self.paciente = paciente
        self.prioridad = 0 if tipo == TipoEvento.URGENCIA else 1 
        self.estado = "Pendiente"
    
    @abstractmethod
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        pass
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo.value,
            'inicio': self.inicio.isoformat(),
            'fin': self.fin.isoformat(),
            'paciente': self.paciente,
            'prioridad': self.prioridad,
            'estado': self.estado,
            'es_urgencia': self.prioridad == 0 
        }