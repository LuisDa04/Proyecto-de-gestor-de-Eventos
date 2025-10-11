from abc import ABC, abstractmethod
from Enums import TipoRecurso
from Eventos import Evento

class Recurso(ABC):
    @abstractmethod
    def __init__(self, id: str, nombre: str, tipo: TipoRecurso):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.disponible = True
        
    @abstractmethod
    def validar_uso(self, evento: 'Evento') -> bool:
        pass
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo.value,
            'disponible': self.disponible
        }