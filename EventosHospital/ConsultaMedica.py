from ..Eventos import Evento
from datetime import datetime
from typing import List
from ..Recursos import Recurso
from ..Enums import TipoEvento
from RecursosHospital.PersonalMedico import PersonalMedico

class ConsultaMedica(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, fin: datetime,
                 recursos: List[Recurso], paciente: str, motivo: str):
        super().__init__(id, nombre, TipoEvento.CONSULTA, inicio, fin, recursos)
        self.paciente = paciente
        self.motivo = motivo
    
    def validar_factibilidad(self) -> bool:
        # Validar que haya al menos un médico
        return any(isinstance(r, PersonalMedico) for r in self.recursos)
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'paciente': self.paciente,
            'motivo': self.motivo
        })
        return data