from enum import Enum

class TipoRecurso(Enum):
    QUIROFANO = "Quirófano" #para cirugia
    CIRUJANO = "Cirujano" #para quirofano
    FISIOTERAPEUTA = "Fisioterapeuta" #para fisioterapia
    DOCTOR = "Doctor" #todos los eventos necesitan un doctor, excepto las consultas y fisioterapia
    ENFERMEROS = "Enfermeros" #todos los eventos necesitan enfermeros
    CONSULTA = "Consulta" #sala de consultas (inculye urgencias)
    UCI = "UCI" #para terapia
    REHABILITACION_FISICA = "Sala de rehabilitacion fisica" #para fisioterapia
    INSTRUMENTAL = "Instrumental" #equipamiento basico necesario para tratar con cada paciente, infinito
    EXAMENES = "Sala de examenes" #necesaria para el examen medico
    CAMILLA = "Camilla" #cada sala tiene una cantidad limitada de camillas (Quirofano, Consulta, UCI, Rehabilitacion fisica)

class TipoEvento(Enum):
    CIRUGIA = "Cirugía"
    CONSULTA = "Consulta" 
    EXAMEN = "Examen Médico" #evento necesario antes de cirugia (en este caso toma prioridad)
    TERAPIA = "Terapia"
    FISIOTERAPIA = "Fisioterapia"
    URGENCIA = "Urgencia" #prioridad sobre los demas eventos en caso de falta de recursos (cuenta como consulta)