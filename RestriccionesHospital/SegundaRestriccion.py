from ..Restricciones import Restriccion
from typing import List
from ..Recursos import Recurso
from ..Eventos import Evento

class RestriccionExclusionMutua(Restriccion):
    def __init__(self, recurso1: str, recurso2: str):
        self.recurso1 = recurso1
        self.recurso2 = recurso2
    
    def validar(self, recursos: List[Recurso], evento: Evento) -> bool:
        recursos_ids = [r.id for r in recursos]
        return not (self.recurso1 in recursos_ids and self.recurso2 in recursos_ids)
    
    def get_descripcion(self) -> str:
        return f"{self.recurso1} y {self.recurso2} no pueden usarse juntos"