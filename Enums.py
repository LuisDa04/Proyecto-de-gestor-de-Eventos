from enum import Enum

class TipoRecurso(Enum):
    QUIROFANO = "Quirófano"
    EQUIPO_MEDICO = "Equipo Médico"
    PERSONAL_MEDICO = "Personal Médico"
    SALA = "Sala"
    INSTRUMENTAL = "Instrumental"

class TipoEvento(Enum):
    CIRUGIA = "Cirugía"
    CONSULTA = "Consulta"
    EXAMEN = "Examen Médico"
    TERAPIA = "Terapia"
    URGENCIA = "Urgencia"