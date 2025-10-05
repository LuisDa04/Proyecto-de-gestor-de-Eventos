from ..Enums import TipoRecurso
from ..Recursos import Recurso
from typing import List
from datetime import timedelta
from ..Eventos import Evento

class Quirofano(Recurso):
    def __init__(self, id: str, nombre: str, equipamiento_especial: List[str]):
        super().__init__(id, nombre, TipoRecurso.QUIROFANO)
        self.equipamiento_especial = equipamiento_especial
        self.capacidad_maxima = timedelta(hours=8) 
        
    def validar_uso(self, evento: Evento) -> bool:
        duracion = evento.fin - evento.inicio
        return duracion <= self.capacidad_maxima
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'equipamiento_especial': self.equipamiento_especial,
            'capacidad_maxima_horas': self.capacidad_maxima.total_seconds() / 3600
        })
        return data
    