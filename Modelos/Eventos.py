from abc import ABC, abstractmethod
from Enums import TipoEvento, TipoRecurso
from typing import Dict, Optional
from datetime import datetime

class Evento(ABC):
    @abstractmethod
    def __init__(self, id: str, nombre: str, tipo: TipoEvento, 
                 inicio: datetime, fin: datetime, paciente: str, sistema_hospital=None):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.inicio = inicio
        self.fin = fin
        self.paciente = paciente
        self.prioridad = 0 if tipo == TipoEvento.URGENCIA else 1 
        self.estado = "Pendiente"
        self.evento_previo: Optional['Evento'] = None
        self.sistema_hospital = sistema_hospital
    
    @abstractmethod
    def get_recursos_necesarios(self) -> Dict[TipoRecurso, int]:
        pass
    
    def set_sistema_hospital(self, sistema):
        """Establece la referencia al sistema hospitalario"""
        self.sistema_hospital = sistema
    
    def set_evento_previo(self, evento_previo: 'Evento'):
        self.evento_previo = evento_previo
        if self.sistema_hospital:
            evento_previo.set_sistema_hospital(self.sistema_hospital)
    
    def tiene_evento_previo(self) -> bool:
        return self.evento_previo is not None
    
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
            'es_urgencia': self.prioridad == 0,
            'evento_previo': self.evento_previo.id if self.evento_previo else None
        }