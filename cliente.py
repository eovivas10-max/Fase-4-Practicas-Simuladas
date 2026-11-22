import re  # Importa el módulo de expresiones regulares para validar formatos de texto
from entidad import EntidadBase  # Importa la clase abstracta base de entidades
from excepciones import ClienteInvalidoError, ParametroFaltanteError  # Importa excepciones específicas
from Registro import registrar_evento  # Importa la función para registrar eventos exitosos en el log

class Cliente(EntidadBase):  # Define la clase Cliente heredando de EntidadBase
    """Representa un cliente de Software FJ con encapsulación y validaciones estrictas."""  # Documenta la clase

    def __init__(self, id_cliente: str, nombre: str, correo: str):  # Constructor de la clase Cliente
        super().__init__(id_cliente)  # Inicializa id_entidad y valida que no esté vacío
        self.nombre = nombre  # Asigna el nombre usando el setter (ejecuta validación)
        self.correo = correo  # Asigna el correo usando el setter (ejecuta validación)
        registrar_evento(f"Cliente registrado: {self._id_entidad} - {self._nombre}")  # Registra el alta en el log

    @property  # Define la propiedad de lectura para el nombre
    def nombre(self) -> str:  # Getter del atributo privado _nombre
        """Obtiene el nombre del cliente."""  # Documenta el getter
        return self._nombre  # Retorna el nombre encapsulado

    @nombre.setter  # Define el validador al asignar o modificar el nombre
    def nombre(self, valor: str):  # Setter que valida y guarda el nombre del cliente
        if valor is None:  # Comprueba si se pasó None en lugar de un texto
            raise ParametroFaltanteError("El nombre del cliente no puede ser nulo.")  # Lanza error de parámetro faltante
        nombre_limpio = str(valor).strip()  # Elimina espacios en blanco al inicio y al final
        if len(nombre_limpio) < 2:  # Verifica una longitud mínima razonable para un nombre
            raise ClienteInvalidoError("El nombre del cliente debe tener al menos 2 caracteres.")  # Lanza error de cliente inválido
        self._nombre = nombre_limpio  # Almacena el nombre validado en el atributo privado

    @property  # Define la propiedad de lectura para el correo electrónico
    def correo(self) -> str:  # Getter del atributo privado _correo
        """Obtiene el correo electrónico del cliente."""  # Documenta el getter
        return self._correo  # Retorna el correo encapsulado

    @correo.setter  # Define el validador al asignar o modificar el correo electrónico
    def correo(self, valor: str):  # Setter que valida el formato del correo electrónico
        if valor is None or not str(valor).strip():  # Verifica que el correo no sea nulo ni vacío
            raise ParametroFaltanteError("El correo del cliente es obligatorio.")  # Lanza error por falta de dato
        correo_limpio = str(valor).strip().lower()  # Normaliza el correo sin espacios y en minúsculas
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"  # Patrón básico para validar usuario@dominio.extensión
        if not re.match(patron_correo, correo_limpio):  # Evalúa si el correo cumple con el formato esperado
            raise ClienteInvalidoError(f"Correo electrónico inválido: '{valor}'.")  # Lanza error si el formato es incorrecto
        self._correo = correo_limpio  # Guarda el correo validado en el atributo privado

    def describir(self) -> str:  # Implementa el método abstracto heredado de EntidadBase
        """Devuelve una descripción resumida del cliente."""  # Documenta el método describir
        return f"Cliente [{self._id_entidad}] {self._nombre} ({self._correo})"  # Formatea y retorna la descripción
