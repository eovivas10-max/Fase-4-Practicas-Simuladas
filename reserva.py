from cliente import Cliente  # Importa la clase Cliente para asociar la reserva a un cliente válido
from entidad import EntidadBase  # Importa la clase abstracta base de entidades del sistema
from excepciones import (  # Importa excepciones personalizadas del sistema
    OperacionNoPermitidaError,
    ParametroFaltanteError,
    ReservaInvalidaError,
)
from Registro import registrar_error, registrar_evento  # Importa funciones de registro de eventos y errores
from servicios import Servicio  # Importa la clase abstracta Servicio

class Reserva(EntidadBase):  # Define la clase Reserva heredando de EntidadBase
    """Representa una reserva de servicio para un cliente en Software FJ."""  # Documenta la clase Reserva

    ESTADOS_VALIDOS = ("PENDIENTE", "CONFIRMADA", "CANCELADA")  # Tupla de estados permitidos para una reserva

    def __init__(  # Constructor de la clase Reserva
        self,
        id_reserva: str,
        cliente: Cliente,
        servicio: Servicio,
        duracion: int,
        descuento_pct: float = 0.0,
        impuesto_pct: float = 0.0,
    ):
        super().__init__(id_reserva)  # Valida y asigna el identificador único de la reserva
        if cliente is None:  # Comprueba que se haya suministrado un objeto cliente
            raise ParametroFaltanteError("La reserva requiere un cliente asignado.")  # Error por parámetro faltante
        if not isinstance(cliente, Cliente):  # Verifica que el argumento sea instancia de Cliente
            raise ReservaInvalidaError("El objeto proporcionado no corresponde a un Cliente válido.")  # Error de reserva
        if servicio is None:  # Comprueba que se haya suministrado un objeto servicio
            raise ParametroFaltanteError("La reserva requiere un servicio asignado.")  # Error por parámetro faltante
        if not isinstance(servicio, Servicio):  # Verifica que el argumento sea instancia de Servicio
            raise ReservaInvalidaError("El objeto proporcionado no corresponde a un Servicio válido.")  # Error de reserva

        servicio.validar_disponibilidad()  # Verifica que el servicio esté disponible antes de crear la reserva
        servicio.validar_parametros(duracion)  # Valida que la duración sea coherente con el servicio

        self._cliente = cliente  # Almacena la referencia al cliente
        self._servicio = servicio  # Almacena la referencia al servicio
        self._duracion = duracion  # Almacena la duración (horas, días o sesiones)
        self._descuento_pct = float(descuento_pct)  # Almacena el porcentaje de descuento opcional
        self._impuesto_pct = float(impuesto_pct)  # Almacena el porcentaje de impuesto opcional
        self._estado = "PENDIENTE"  # Inicializa la reserva en estado PENDIENTE
        self._costo_total = 0.0  # Inicializa el costo total calculado en 0.0

        registrar_evento(  # Registra la creación de la reserva en el archivo de logs
            f"Reserva creada [{self._id_entidad}] para {self._cliente.nombre} - Servicio: {self._servicio.id_entidad}"
        )

    @property  # Expone el estado actual de la reserva como propiedad de solo lectura
    def estado(self) -> str:  # Getter para consultar el estado de la reserva
        """Retorna el estado actual de la reserva."""  # Documenta el método getter
        return self._estado  # Devuelve el estado almacenado

    @property  # Expone el costo total calculado como propiedad de solo lectura
    def costo_total(self) -> float:  # Getter para consultar el costo total de la reserva
        """Retorna el costo total calculado de la reserva."""  # Documenta el método getter
        return self._costo_total  # Devuelve el costo total

    def confirmar(self):  # Confirma la reserva si su estado actual lo permite
        """Cambia el estado de la reserva a CONFIRMADA si está PENDIENTE."""  # Documenta confirmar
        if self._estado == "CANCELADA":  # Impide confirmar una reserva previamente cancelada
            raise OperacionNoPermitidaError(  # Lanza excepción por operación inválida según el estado
                f"No se puede confirmar la reserva '{self._id_entidad}' porque está CANCELADA."
            )
        if self._estado == "CONFIRMADA":  # Evita confirmar dos veces la misma reserva
            raise OperacionNoPermitidaError(  # Lanza excepción por operación no permitida
                f"La reserva '{self._id_entidad}' ya se encuentra CONFIRMADA."
            )
        self._estado = "CONFIRMADA"  # Actualiza el estado a CONFIRMADA
        registrar_evento(f"Reserva [{self._id_entidad}] CONFIRMADA.")  # Registra confirmación en el log

    def cancelar(self):  # Cancela la reserva si no ha sido cancelada antes
        """Cambia el estado de la reserva a CANCELADA si no estaba ya cancelada."""  # Documenta cancelar
        if self._estado == "CANCELADA":  # Verifica si ya está en estado CANCELADA
            raise OperacionNoPermitidaError(  # Lanza excepción por operación no permitida
                f"La reserva '{self._id_entidad}' ya fue CANCELADA anteriormente."
            )
        self._estado = "CANCELADA"  # Cambia el estado a CANCELADA
        registrar_evento(f"Reserva [{self._id_entidad}] CANCELADA.")  # Registra cancelación en el log

    def procesar(self) -> float:  # Calcula el costo, confirma la reserva y maneja errores con encadenamiento
        """Calcula el costo del servicio y confirma la reserva de forma segura."""  # Documenta procesar
        try:  # Bloque principal para calcular costo y confirmar la reserva
            costo = self._servicio.calcular_costo(  # Invoca cálculo polimórfico con descuentos e impuestos
                self._duracion,
                descuento_pct=self._descuento_pct,
                impuesto_pct=self._impuesto_pct,
            )
            self._costo_total = costo  # Guarda el costo calculado en la reserva
            self.confirmar()  # Confirma la reserva una vez calculado el costo
        except OperacionNoPermitidaError:  # Propaga errores de estado sin alterar su tipo
            raise  # Re-lanza la excepción original
        except Exception as exc:  # Captura cualquier error inesperado durante el cálculo o confirmación
            registrar_error(f"Fallo al procesar la reserva '{self._id_entidad}'", exc)  # Registra error y causa
            raise ReservaInvalidaError(  # Encadena el error dentro de ReservaInvalidaError
                f"No fue posible procesar la reserva '{self._id_entidad}'."
            ) from exc  # Conserva la excepción original en __cause__
        else:  # Se ejecuta únicamente si el bloque try terminó sin excepciones
            registrar_evento(  # Registra el procesamiento exitoso de la reserva
                f"Reserva [{self._id_entidad}] procesada con éxito. Total: ${self._costo_total:.2f}"
            )
            return self._costo_total  # Retorna el costo total confirmado
        finally:  # Se ejecuta siempre, ocurra o no una excepción
            registrar_evento(f"Fin de intento de procesamiento para reserva [{self._id_entidad}].")  # Traza final

    def describir(self) -> str:  # Implementa describir de forma polimórfica
        """Devuelve una descripción completa de la reserva."""  # Documenta describir
        return (  # Retorna cadena formateada con los datos de la reserva
            f"Reserva [{self._id_entidad}] | Estado: {self._estado} | "
            f"Cliente: {self._cliente.nombre} | Servicio: {self._servicio.id_entidad} | "
            f"Duración: {self._duracion} | Total: ${self._costo_total:.2f}"
        )
