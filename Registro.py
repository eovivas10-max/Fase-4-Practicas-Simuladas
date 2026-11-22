import logging  # Importa el módulo estándar de Python para registro de eventos y errores
import os  # Importa el módulo os para gestionar rutas y directorios del sistema de archivos

# Carpeta y archivo donde se guardan los eventos y errores  # Comentario descriptivo de la ruta de logs
CARPETA_LOGS = "logs"  # Nombre de la carpeta donde se almacenará el archivo de registro
ARCHIVO_LOG = os.path.join(CARPETA_LOGS, "software_fj.log")  # Ruta completa del archivo de log de forma multiplataforma

# Si la carpeta no existe la creamos para que no falle al abrir el archivo  # Explica la creación preventiva del directorio
os.makedirs(CARPETA_LOGS, exist_ok=True)  # Crea la carpeta 'logs' si no existe sin lanzar error si ya existe

# Configuración básica: fecha, nivel y mensaje en cada línea  # Describe los parámetros de logging.basicConfig
logging.basicConfig(  # Configura el sistema de logging global
    filename=ARCHIVO_LOG,  # Define el archivo destino donde se escribirán los registros
    level=logging.INFO,  # Establece el nivel mínimo INFO para registrar eventos normales y errores
    format="%(asctime)s | %(levelname)s | %(message)s",  # Define el formato de cada línea con fecha, nivel y mensaje
    encoding="utf-8",  # Garantiza codificación UTF-8 para caracteres especiales y tildes
)

_logger = logging.getLogger("software_fj")  # Obtiene o crea una instancia de logger nombrada 'software_fj'

def registrar_evento(mensaje):  # Función para registrar eventos exitosos o informativos del sistema
    """Guarda un evento normal (algo que salió bien)."""  # Documenta el propósito de registrar_evento
    _logger.info(mensaje)  # Escribe el mensaje en el archivo de log con nivel INFO

def registrar_error(mensaje, excepcion=None):  # Función para registrar errores y opcionalmente su excepción asociada
    """Guarda un error. Si llega la excepción, se anota también su causa."""  # Documenta el manejo de errores y causas
    if excepcion is not None:  # Verifica si se proporcionó una instancia de excepción
        # Si el error venía encadenado (raise ... from ...), guardamos la causa original  # Explica inspección de __cause__
        causa = excepcion.__cause__  # Obtiene la excepción original que causó el encadenamiento, si existe
        if causa is not None:  # Comprueba si existe una causa encadenada
            mensaje = f"{mensaje} | causa: {type(causa).__name__}: {causa}"  # Añade tipo y detalle de la causa original
        mensaje = f"{mensaje} | {type(excepcion).__name__}: {excepcion}"  # Añade tipo y mensaje de la excepción actual
    _logger.error(mensaje)  # Escribe el registro de error en el archivo de log con nivel ERROR
