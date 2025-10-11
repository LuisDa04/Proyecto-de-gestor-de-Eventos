from Enums import TipoRecurso
from typing import Dict

class StockManager:
    def __init__(self):
        self.stock = {
            TipoRecurso.CIRUJANO: 2,
            TipoRecurso.FISIOTERAPEUTA: 4,
            TipoRecurso.DOCTOR: 15,
            TipoRecurso.ENFERMEROS: 20,
            TipoRecurso.TECNICOS: 3,
            
            TipoRecurso.QUIROFANO: 2,
            TipoRecurso.CONSULTA: 12,
            TipoRecurso.UCI: 8,
            TipoRecurso.REHABILITACION_FISICA: 4,
            TipoRecurso.EXAMENES: 3,
            
            TipoRecurso.INSTRUMENTAL: float('inf'),
            TipoRecurso.SALA_ESPERA: 30
        }
        
        self.stock_disponible = self.stock.copy()
        
        self.asignaciones = {}
        
    def reservar_recursos(self, evento_id: str, recursos_solicitados: Dict[TipoRecurso, int]) -> bool:
        for tipo_recurso, cantidad in recursos_solicitados.items():
            if tipo_recurso == TipoRecurso.INSTRUMENTAL:
                continue
            
            if self.stock_disponible[tipo_recurso] < cantidad:
                return False
        
        for tipo_recurso, cantidad in recursos_solicitados.items():
            if tipo_recurso != TipoRecurso.INSTRUMENTAL:
                self.stock_disponible[tipo_recurso] -= cantidad
            
            if evento_id not in self.asignaciones:
                self.asignaciones[evento_id] = {}
            self.asignaciones[evento_id][tipo_recurso] = cantidad
        
        return True
    
    def liberar_recursos(self, evento_id: str):
        if evento_id in self.asignaciones:
            for tipo_recurso, cantidad in self.asignaciones[evento_id].items():
                if tipo_recurso != TipoRecurso.INSTRUMENTAL:
                    self.stock_disponible[tipo_recurso] += cantidad
            del self.asignaciones[evento_id]
            
    
    #Utilities
    def get_stock_disponible(self, tipo_recurso: TipoRecurso) -> int:
        return self.stock_disponible[tipo_recurso]
    
    def get_stock_total(self, tipo_recurso: TipoRecurso) -> int:
        return self.stock[tipo_recurso]
    
    def hay_suficientes_recursos(self, recursos_solicitados: Dict[TipoRecurso, int]) -> bool:
        for tipo_recurso, cantidad in recursos_solicitados.items():
            if tipo_recurso != TipoRecurso.INSTRUMENTAL:
                if self.stock_disponible[tipo_recurso] < cantidad:
                    return False
        return True

    def hay_espacio_en_sala_espera(self) -> bool:
        return self.stock_disponible[TipoRecurso.SALA_ESPERA] > 0
    
    def ocupar_sala_espera(self):
        if self.hay_espacio_en_sala_espera():
            self.stock_disponible[TipoRecurso.SALA_ESPERA] -= 1
            return True
        return False
    
    def liberar_sala_espera(self):
        if self.stock_disponible[TipoRecurso.SALA_ESPERA] < self.stock[TipoRecurso.SALA_ESPERA]:
            self.stock_disponible[TipoRecurso.SALA_ESPERA] += 1
    
        