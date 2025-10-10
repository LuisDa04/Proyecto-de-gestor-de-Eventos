from enum import Enum

class TipoRecurso(Enum):
    CIRUJANO = "Cirujano" #para quirofano
    FISIOTERAPEUTA = "Fisioterapeuta" #para fisioterapia
    DOCTOR = "Doctor" #todos los eventos necesitan un doctor, excepto la fisioterapia
    ENFERMEROS = "Enfermeros" #todos los eventos necesitan enfermeros
    TECNICOS = "Operadores de equipos medicos" #trabajan en la sal de examenes
    
    QUIROFANO = "Quirófano" #para cirugia
    CONSULTA = "Consulta" #sala de consultas (inculye urgencias)
    UCI = "UCI" #para terapia
    REHABILITACION_FISICA = "Sala de rehabilitacion fisica" #para fisioterapia
    EXAMENES = "Sala de examenes" #necesaria para el examen medico
    
    INSTRUMENTAL = "Instrumental" #equipamiento basico necesario para tratar con cada paciente, infinito
    SALA_DE_ESPERA = "Espacios en la sala de espera" #en orden de llegada

class TipoEvento(Enum):
    CIRUGIA = "Cirugía"
    CONSULTA = "Consulta" 
    EXAMEN = "Examen Médico" #evento necesario antes de cirugia (en este caso toma prioridad)
    TERAPIA = "Terapia"
    FISIOTERAPIA = "Fisioterapia"
    URGENCIA = "Urgencia" #prioridad sobre los demas eventos en caso de falta de recursos (cuenta como consulta)
    
class EstadoPaciente(Enum):
    ESPERANDO = "En espera"
    ATENDIENDOSE = "Atendiendose"
    COMPLETADO = "Completado"