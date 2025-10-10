from ..Restricciones import Restriccion
from typing import List
from ..Recursos import Recurso
from Eventos import Evento

class RestriccionCorequisito(Restriccion):
    def __init__(self, recurso_principal: str, recursos_requeridos: List[str]):
        self.recurso_principal = recurso_principal
        self.recursos_requeridos = recursos_requeridos
    
    def validar(self, recursos: List[Recurso], evento: Evento) -> bool:
        recursos_ids = [r.id for r in recursos]
        
        # Si está el recurso principal, deben estar todos los requeridos
        if self.recurso_principal in recursos_ids:
            for requerido in self.recursos_requeridos:
                if requerido not in recursos_ids:
                    return False
        return True
    
    def get_descripcion(self) -> str:
        return f"Si se usa {self.recurso_principal}, también deben usarse: {', '.join(self.recursos_requeridos)}"