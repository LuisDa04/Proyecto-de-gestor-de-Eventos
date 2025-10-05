from ..Recursos import Recurso
from ..Enums import TipoRecurso
from ..Eventos import Evento

class EquipoMedico(Recurso):
    def __init__(self, id: str, nombre: str, requiere_operador: bool, 
                 mantenimiento_requerido: bool):
        super().__init__(id, nombre, TipoRecurso.EQUIPO_MEDICO)
        self.requiere_operador = requiere_operador
        self.mantenimiento_requerido = mantenimiento_requerido
    
    def validar_uso(self, evento: Evento) -> bool:
        return True  # Implementar validaciones específicas
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'requiere_operador': self.requiere_operador,
            'mantenimiento_requerido': self.mantenimiento_requerido
        })
        return data