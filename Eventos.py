from abc import ABC, abstractmethod
from Enums import TipoEvento
from Recursos import Recurso
from typing import List
from datetime import datetime

class Evento(ABC):
    @abstractmethod
    def __init__(self, id: str, nombre: str, tipo: TipoEvento, 
                 inicio: datetime, fin: datetime, recursos: List[Recurso]):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.inicio = inicio
        self.fin = fin
        self.recursos = recursos
        self.estado = "Pendiente"  # Pendiente, Confirmado, Cancelado
        
    @abstractmethod
    def validar_factibilidad(self) -> bool:
        pass
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo.value,
            'inicio': self.inicio.isoformat(),
            'fin': self.fin.isoformat(),
            'recursos': [r.id for r in self.recursos],
            'estado': self.estado
        }