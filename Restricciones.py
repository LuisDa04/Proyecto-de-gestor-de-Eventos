from abc import ABC, abstractmethod
from typing import List
from Recursos import Recurso
from Eventos import Evento

class Restriccion(ABC):
    @abstractmethod
    def validar(self, recursos: List[Recurso], evento: 'Evento') -> bool:
        pass
    
    def get_info(self) -> str:
        pass