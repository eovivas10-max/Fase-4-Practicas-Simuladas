# Excepciones personalizadas de Software FJ  # Encabezado indicando el propósito del módulo
# Todas heredan de una clase base para poder capturarlas juntas si hace falta.  # Explica la ventaja de la herencia en excepciones

class ErrorSoftwareFJ(Exception):  # Clase base personalizada que hereda de la Exception nativa de Python
    """Error general del sistema; de aquí salen las demás."""  # Documenta la excepción raíz del dominio
    pass  # No añade atributos o métodos adicionales sobre Exception

class ClienteInvalidoError(ErrorSoftwareFJ):  # Excepción específica para errores en datos de clientes
    """Datos del cliente incorrectos (nombre vacío, correo mal escrito, etc.)."""  # Documenta cuándo ocurre este error
    pass  # Hereda comportamiento estándar de ErrorSoftwareFJ

class ParametroFaltanteError(ErrorSoftwareFJ):  # Excepción para parámetros obligatorios ausentes o nulos
    """Se llamó a un método sin un dato obligatorio."""  # Documenta cuándo lanzar esta excepción
    pass  # Hereda comportamiento estándar de ErrorSoftwareFJ

class ServicioNoDisponibleError(ErrorSoftwareFJ):  # Excepción cuando un servicio no está disponible para usarse
    """El servicio pedido no existe o no se puede usar en este momento."""  # Documenta el escenario de disponibilidad
    pass  # Hereda comportamiento estándar de ErrorSoftwareFJ

class ReservaInvalidaError(ErrorSoftwareFJ):  # Excepción para intentos de reserva inválidos o mal formados
    """Intento de reserva incorrecto (duración negativa, datos incompletos...)."""  # Documenta errores de reserva
    pass  # Hereda comportamiento estándar de ErrorSoftwareFJ

class OperacionNoPermitidaError(ErrorSoftwareFJ):  # Excepción para cambios de estado o acciones no permitidas
    """Operación que el estado actual no permite (ej: cancelar algo ya cancelado)."""  # Documenta restricciones de estado
    pass  # Hereda comportamiento estándar de ErrorSoftwareFJ

class CalculoInconsistenteError(ErrorSoftwareFJ):  # Excepción para resultados numéricos o cálculos incoherentes
    """El cálculo de un costo dio un resultado que no tiene sentido."""  # Documenta inconsistencias en cálculos
    pass  # Hereda comportamiento estándar de ErrorSoftwareFJ
