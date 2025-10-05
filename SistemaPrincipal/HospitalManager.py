from typing import List, Dict
from Recursos import Recurso
from Eventos import Evento
from Restricciones import Restriccion
from datetime import datetime, timedelta, Optional
import json
from EventosHospital.Cirugia import Cirugia

class SistemaPlanificacionHospital:
    def __init__(self):
        self.recursos: Dict[str, Recurso] = {}
        self.eventos: Dict[str, Evento] = {}
        self.restricciones: List[Restriccion] = []
        self.calendario: Dict[datetime, List[Evento]] = {}
    
    def agregar_recurso(self, recurso: Recurso):
        self.recursos[recurso.id] = recurso
    
    def agregar_restriccion(self, restriccion: Restriccion):
        self.restricciones.append(restriccion)
    
    def planificar_evento(self, evento: Evento) -> bool:
        # Validar disponibilidad de recursos
        if not self.validar_disponibilidad_recursos(evento):
            return False
        
        # Validar restricciones
        if not self.validar_restricciones(evento):
            return False
        
        # Validar factibilidad del evento
        if not evento.validar_factibilidad():
            return False
        
        # Reservar recursos
        for recurso in evento.recursos:
            recurso.disponible = False
        
        # Agregar evento
        self.eventos[evento.id] = evento
        self.actualizar_calendario(evento)
        
        return True
    
    def validar_disponibilidad_recursos(self, evento: Evento) -> bool:
        for recurso in evento.recursos:
            if not recurso.disponible:
                # Verificar si el recurso está ocupado en el horario del evento
                eventos_conflicto = self.buscar_conflictos_recurso(recurso, evento.inicio, evento.fin)
                if eventos_conflicto:
                    return False
        return True
    
    def buscar_conflictos_recurso(self, recurso: Recurso, inicio: datetime, fin: datetime) -> List[Evento]:
        conflictos = []
        for evento in self.eventos.values():
            if recurso in evento.recursos:
                if (inicio < evento.fin and fin > evento.inicio):
                    conflictos.append(evento)
        return conflictos
    
    def validar_restricciones(self, evento: Evento) -> bool:
        for restriccion in self.restricciones:
            if not restriccion.validar(evento.recursos, evento):
                return False
        return True
    
    def buscar_hueco_disponible(self, duracion: timedelta, recursos_necesarios: List[str], 
                               inicio_busqueda: datetime = None) -> Optional[datetime]:
        if inicio_busqueda is None:
            inicio_busqueda = datetime.now()
        
        # Buscar en las próximas 24 horas en intervalos de 30 minutos
        for horas in range(0, 24):
            for minutos in [0, 30]:
                inicio_posible = inicio_busqueda + timedelta(hours=horas, minutes=minutos)
                fin_posible = inicio_posible + duracion
                
                # Simular evento temporal para validación
                evento_temp = Cirugia("temp", "Temporal", inicio_posible, fin_posible, 
                                    [self.recursos[r] for r in recursos_necesarios], "Temp", "Temp")
                
                if self.validar_disponibilidad_recursos(evento_temp) and self.validar_restricciones(evento_temp):
                    return inicio_posible
        
        return None
    
    def actualizar_calendario(self, evento: Evento):
        fecha = evento.inicio.date()
        if fecha not in self.calendario:
            self.calendario[fecha] = []
        self.calendario[fecha].append(evento)
    
    def guardar_estado(self, archivo: str):
        estado = {
            'recursos': [r.to_dict() for r in self.recursos.values()],
            'eventos': [e.to_dict() for e in self.eventos.values()],
            'restricciones': [{
                'tipo': type(r).__name__,
                'descripcion': r.get_descripcion()
            } for r in self.restricciones]
        }
        
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(estado, f, indent=2, ensure_ascii=False)
    
    def cargar_estado(self, archivo: str):
        with open(archivo, 'r', encoding='utf-8') as f:
            estado = json.load(f)
        
        # Reconstruir recursos (simplificado)
        for recurso_data in estado['recursos']:
            # Aquí implementar la lógica para reconstruir los objetos Recurso
            pass