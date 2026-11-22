from abc import ABC, abstractmethod  # Importa herramientas para clases y métodos abstractos
from entidad import EntidadBase  # Importa la clase base de entidades
from excepciones import (  # Importa excepciones personalizadas del sistema
    CalculoInconsistenteError,
    ParametroFaltanteError,
    ServicioNoDisponibleError,
)
from Registro import registrar_evento  # Importa la función de registro de eventos

class Servicio(EntidadBase, ABC):  # Clase abstracta Servicio que hereda de EntidadBase y ABC
    """Clase abstracta base para los servicios ofrecidos por Software FJ."""  # Documenta la clase Servicio

    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, disponible: bool = True):  # Constructor base
        super().__init__(id_servicio)  # Valida y asigna id_entidad en EntidadBase
        if not nombre or not str(nombre).strip():  # Verifica que el servicio tenga un nombre válido
            raise ParametroFaltanteError("El nombre del servicio es obligatorio.")  # Lanza error si falta el nombre
        if tarifa_base is None:  # Verifica que se haya proporcionado una tarifa base
            raise ParametroFaltanteError("La tarifa base del servicio es obligatoria.")  # Lanza error si falta tarifa
        if float(tarifa_base) <= 0:  # Comprueba que la tarifa base sea positiva
            raise CalculoInconsistenteError("La tarifa base debe ser mayor que cero.")  # Lanza error por cálculo inválido
        self._nombre = str(nombre).strip()  # Guarda el nombre del servicio
        self._tarifa_base = float(tarifa_base)  # Guarda la tarifa base como flotante
        self._disponible = bool(disponible)  # Indica si el servicio está disponible para reservar

    @property  # Expone la disponibilidad como propiedad
    def disponible(self) -> bool:  # Getter para consultar si el servicio está disponible
        """Indica si el servicio se encuentra disponible."""  # Documenta el getter
        return self._disponible  # Retorna el estado de disponibilidad

    @disponible.setter  # Permite actualizar la disponibilidad del servicio
    def disponible(self, estado: bool):  # Setter de disponibilidad
        self._disponible = bool(estado)  # Convierte y guarda el nuevo estado booleano

    def validar_disponibilidad(self):  # Verifica que el servicio pueda utilizarse antes de operar
        """Valida si el servicio está disponible; si no, lanza ServicioNoDisponibleError."""  # Documenta el método
        if not self._disponible:  # Si el servicio está marcado como no disponible
            raise ServicioNoDisponibleError(f"El servicio '{self._nombre}' no está disponible.")  # Lanza excepción

    @abstractmethod  # Obliga a cada clase hija a validar sus propios parámetros
    def validar_parametros(self, unidades: int):  # Método abstracto de validación de parámetros
        """Valida los parámetros específicos (como duración o cantidad) del servicio."""  # Documenta el método
        pass  # Implementado en cada subclase

    @abstractmethod  # Obliga a cada clase hija a calcular su costo según su lógica
    def calcular_costo(self, unidades: int, descuento_pct: float = 0.0, impuesto_pct: float = 0.0) -> float:  # Costo polimórfico
        """Calcula el costo total aplicando descuento e impuesto opcionales."""  # Documenta el método
        pass  # Implementado en cada subclase

    def _calcular_monto_ajustado(self, subtotal: float, descuento_pct: float, impuesto_pct: float) -> float:  # Auxiliar interno
        """Aplica descuento e impuesto validando que el resultado sea consistente."""  # Documenta el cálculo auxiliar
        if descuento_pct < 0 or descuento_pct >= 100:  # Valida que el porcentaje de descuento esté en un rango válido
            raise CalculoInconsistenteError("El porcentaje de descuento debe estar entre 0 y menor a 100.")  # Error de cálculo
        if impuesto_pct < 0:  # Valida que el porcentaje de impuesto no sea negativo
            raise CalculoInconsistenteError("El porcentaje de impuesto no puede ser negativo.")  # Error de cálculo
        if subtotal < 0:  # Valida que el subtotal no sea negativo
            raise CalculoInconsistenteError("El subtotal calculado no puede ser negativo.")  # Error de cálculo
        con_descuento = subtotal * (1 - (descuento_pct / 100.0))  # Aplica el descuento porcentual al subtotal
        total = con_descuento * (1 + (impuesto_pct / 100.0))  # Aplica el impuesto porcentual sobre el monto descontado
        if total < 0:  # Verifica consistencia final del total
            raise CalculoInconsistenteError("El costo final resultante es inconsistente.")  # Lanza error si es negativo
        return round(total, 2)  # Redondea el total a dos decimales

class ReservaSala(Servicio):  # Primera clase hija: servicio de reserva de salas
    """Servicio especializado para la reserva de salas por horas."""  # Documenta ReservaSala

    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, capacidad: int, disponible: bool = True):  # Constructor
        super().__init__(id_servicio, nombre, tarifa_base, disponible)  # Inicializa atributos comunes de Servicio
        if capacidad is None or int(capacidad) <= 0:  # Valida que la sala tenga una capacidad positiva
            raise CalculoInconsistenteError("La capacidad de la sala debe ser mayor que cero.")  # Error de validación
        self._capacidad = int(capacidad)  # Guarda la capacidad máxima de personas
        registrar_evento(f"Servicio de sala creado: {self._id_entidad} ({self._nombre})")  # Registra creación en log

    def validar_parametros(self, unidades: int):  # Sobrescribe validación para horas de reserva
        """Valida que la duración en horas sea un entero positivo."""  # Documenta el método
        if unidades is None:  # Verifica presencia del parámetro de horas
            raise ParametroFaltanteError("Debe indicar la cantidad de horas para la sala.")  # Lanza error si falta
        if not isinstance(unidades, int) or isinstance(unidades, bool) or unidades <= 0:  # Valida entero > 0
            raise CalculoInconsistenteError("Las horas de reserva de sala deben ser un entero mayor a 0.")  # Error de valor

    def calcular_costo(self, unidades: int, descuento_pct: float = 0.0, impuesto_pct: float = 0.0) -> float:  # Sobrescribe cálculo
        """Calcula el costo de reservar la sala por la cantidad de horas indicadas."""  # Documenta cálculo
        self.validar_disponibilidad()  # Verifica disponibilidad antes de calcular
        self.validar_parametros(unidades)  # Valida las horas solicitadas
        subtotal = self._tarifa_base * unidades  # Multiplica tarifa por hora por número de horas
        return self._calcular_monto_ajustado(subtotal, descuento_pct, impuesto_pct)  # Aplica descuento e impuesto

    def describir(self) -> str:  # Sobrescribe describir con polimorfismo
        """Devuelve la descripción de la sala."""  # Documenta describir
        estado = "Disponible" if self._disponible else "No disponible"  # Texto legible de disponibilidad
        return f"Sala [{self._id_entidad}] {self._nombre} | Cap: {self._capacidad} | {estado}"  # Retorna descripción

class AlquilerEquipo(Servicio):  # Segunda clase hija: servicio de alquiler de equipos
    """Servicio especializado para el alquiler de equipos tecnológicos."""  # Documenta AlquilerEquipo

    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, codigo_equipo: str, disponible: bool = True):  # Constructor
        super().__init__(id_servicio, nombre, tarifa_base, disponible)  # Inicializa atributos base de Servicio
        if not codigo_equipo or not str(codigo_equipo).strip():  # Verifica que el equipo tenga código de inventario
            raise ParametroFaltanteError("El código del equipo es obligatorio.")  # Lanza error si falta código
        self._codigo_equipo = str(codigo_equipo).strip()  # Guarda el código del equipo
        registrar_evento(f"Servicio de alquiler creado: {self._id_entidad} ({self._codigo_equipo})")  # Registra en log

    def validar_parametros(self, unidades: int):  # Sobrescribe validación para días de alquiler
        """Valida que los días de alquiler sean un entero positivo."""  # Documenta el método
        if unidades is None:  # Verifica que se indique la cantidad de días
            raise ParametroFaltanteError("Debe indicar la cantidad de días de alquiler.")  # Error de parámetro faltante
        if not isinstance(unidades, int) or isinstance(unidades, bool) or unidades <= 0:  # Valida entero > 0
            raise CalculoInconsistenteError("Los días de alquiler deben ser un entero mayor a 0.")  # Error de cálculo

    def calcular_costo(self, unidades: int, descuento_pct: float = 0.0, impuesto_pct: float = 0.0) -> float:  # Sobrescribe cálculo
        """Calcula el costo del alquiler según los días solicitados y descuentos/impuestos."""  # Documenta cálculo
        self.validar_disponibilidad()  # Verifica disponibilidad del equipo
        self.validar_parametros(unidades)  # Valida los días de alquiler
        subtotal = self._tarifa_base * unidades  # Calcula subtotal por días
        return self._calcular_monto_ajustado(subtotal, descuento_pct, impuesto_pct)  # Aplica ajustes porcentuales

    def describir(self) -> str:  # Sobrescribe describir con polimorfismo
        """Devuelve la descripción del equipo en alquiler."""  # Documenta describir
        estado = "Disponible" if self._disponible else "No disponible"  # Texto de disponibilidad
        return f"Equipo [{self._id_entidad}] {self._nombre} (Cod: {self._codigo_equipo}) | {estado}"  # Retorna descripción

class AsesoriaEspecializada(Servicio):  # Tercera clase hija: asesorías especializadas
    """Servicio especializado para asesorías técnicas o profesionales."""  # Documenta AsesoriaEspecializada

    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, especialidad: str, disponible: bool = True):  # Constructor
        super().__init__(id_servicio, nombre, tarifa_base, disponible)  # Inicializa atributos base de Servicio
        if not especialidad or not str(especialidad).strip():  # Verifica que se especifique el área de asesoría
            raise ParametroFaltanteError("La especialidad de la asesoría es obligatoria.")  # Error si falta especialidad
        self._especialidad = str(especialidad).strip()  # Guarda la especialidad de la asesoría
        registrar_evento(f"Asesoría creada: {self._id_entidad} - {self._especialidad}")  # Registra en log

    def validar_parametros(self, unidades: int):  # Sobrescribe validación para sesiones/horas de asesoría
        """Valida que la cantidad de sesiones de asesoría sea un entero positivo."""  # Documenta el método
        if unidades is None:  # Verifica que se haya pasado la cantidad de sesiones
            raise ParametroFaltanteError("Debe indicar el número de sesiones de asesoría.")  # Error por parámetro faltante
        if not isinstance(unidades, int) or isinstance(unidades, bool) or unidades <= 0:  # Valida entero > 0
            raise CalculoInconsistenteError("Las sesiones de asesoría deben ser un entero mayor a 0.")  # Error de cálculo

    def calcular_costo(self, unidades: int, descuento_pct: float = 0.0, impuesto_pct: float = 0.0) -> float:  # Sobrescribe cálculo
        """Calcula el costo de la asesoría según el número de sesiones y parámetros opcionales."""  # Documenta cálculo
        self.validar_disponibilidad()  # Verifica disponibilidad de la asesoría
        self.validar_parametros(unidades)  # Valida la cantidad de sesiones
        subtotal = self._tarifa_base * unidades  # Calcula subtotal por sesiones
        return self._calcular_monto_ajustado(subtotal, descuento_pct, impuesto_pct)  # Aplica descuento e impuesto

    def describir(self) -> str:  # Sobrescribe describir con polimorfismo
        """Devuelve la descripción de la asesoría especializada."""  # Documenta describir
        estado = "Disponible" if self._disponible else "No disponible"  # Texto de disponibilidad
        return f"Asesoría [{self._id_entidad}] {self._nombre} ({self._especialidad}) | {estado}"  # Retorna descripción
