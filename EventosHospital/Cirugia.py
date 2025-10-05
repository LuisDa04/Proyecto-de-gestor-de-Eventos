from Eventos import Evento
from datetime import datetime
from typing import List
from Recursos import Recurso
from Enums import TipoEvento
from RecursosHospital.PersonalMedico import PersonalMedico
from RecursosHospital.Quirofano import Quirofano

class Cirugia(Evento):
    def __init__(self, id: str, nombre: str, inicio: datetime, fin: datetime, 
                 recursos: List[Recurso], tipo_cirugia: str, paciente: str):
        super().__init__(id, nombre, TipoEvento.CIRUGIA, inicio, fin, recursos)
        self.tipo_cirugia = tipo_cirugia
        self.paciente = paciente
    
    def validar_factibilidad(self) -> bool:
        # Validar que haya al menos un cirujano y un quirófano
        tiene_cirujano = any(isinstance(r, PersonalMedico) and 
                           'Cirujano' in r.especialidad for r in self.recursos)
        tiene_quirofano = any(isinstance(r, Quirofano) for r in self.recursos)
        
        return tiene_cirujano and tiene_quirofano
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo_cirugia': self.tipo_cirugia,
            'paciente': self.paciente
        })
        return data