from StockHospital.StockRecursos import StockManager
from collections import deque
from typing import Dict, Optional
from EstadoPaciente import PacienteEnEspera
from Enums import EstadoPaciente

class GestorSalaEspera:
    def __init__(self, stock_manager: StockManager):
        self.stock_manager = stock_manager
        self.cola_espera = deque()
        self.pacientes_en_espera: Dict[str, PacienteEnEspera] = {}
        self.historico_pacientes = []
    
    def agregar_paciente_espera(self, paciente: PacienteEnEspera) -> bool:
        if not self.stock_manager.ocupar_sala_espera():
            return False
        
        self.cola_espera.append(paciente)
        self.pacientes_en_espera[paciente.paciente_id] = paciente
        return True
    
    def remover_paciente_espera(self, paciente_id: str) -> Optional[PacienteEnEspera]:
        if paciente_id in self.pacientes_en_espera:
            paciente = self.pacientes_en_espera[paciente_id]
            
            if paciente in self.cola_espera:
                self.cola_espera.remove(paciente)
            
            self.stock_manager.liberar_sala_espera()
            
            paciente.estado = EstadoPaciente.COMPLETADO
            self.historico_pacientes.append(paciente)
            del self.pacientes_en_espera[paciente_id]
            
            return paciente
        return None
    
    def get_proximo_paciente(self) -> Optional[PacienteEnEspera]:
        """Obtiene el próximo paciente a atender (urgencias primero, luego por tiempo de espera)"""
        if not self.cola_espera:
            return None
        
        # Primero buscar urgencias (prioridad 0)
        urgencias = [p for p in self.cola_espera if p.prioridad == 0]
        if urgencias:
            # Ordenar urgencias por tiempo de llegada (más antiguo primero)
            return sorted(urgencias, key=lambda p: p.hora_llegada)[0]
        
        # Si no hay urgencias, tomar el más antiguo de prioridad 1
        normales = [p for p in self.cola_espera if p.prioridad == 1]
        if normales:
            return sorted(normales, key=lambda p: p.hora_llegada)[0]
        
        return None
    
    def actualizar_tiempos_espera(self):
        for paciente in self.pacientes_en_espera.values():
            paciente.actualizar_tiempo_espera()