from ..Recursos import Recurso
from typing import List
from ..Enums import TipoRecurso
from datetime import timedelta
from ..Eventos import Evento

class PersonalMedico(Recurso):
    def __init__(self, id: str, nombre: str, especialidad: str, 
                 certificaciones: List[str], horas_maximas: int = 12):
        super().__init__(id, nombre, TipoRecurso.PERSONAL_MEDICO)
        self.especialidad = especialidad
        self.certificaciones = certificaciones
        self.horas_maximas_diarias = timedelta(hours=horas_maximas)
    
    def validar_uso(self, evento: Evento) -> bool:
        duracion = evento.fin - evento.inicio
        return duracion <= self.horas_maximas_diarias
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'especialidad': self.especialidad,
            'certificaciones': self.certificaciones,
            'horas_maximas_diarias': self.horas_maximas_diarias.total_seconds() / 3600
        })
        return data