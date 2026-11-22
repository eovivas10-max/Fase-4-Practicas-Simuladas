from abc import ABC, abstractmethod  # Importa ABC y abstractmethod para definir clases y métodos abstractos
from excepciones import ParametroFaltanteError  # Importa la excepción personalizada por falta de parámetros

class EntidadBase(ABC):  # Clase abstracta base que heredan las entidades del sistema
    """Clase abstracta que representa una entidad general del sistema Software FJ."""  # Documenta el propósito de la clase

    def __init__(self, id_entidad: str):  # Constructor que recibe el identificador único de la entidad
        if not id_entidad or not str(id_entidad).strip():  # Verifica que el ID no esté vacío ni solo con espacios
            raise ParametroFaltanteError("El identificador de la entidad es obligatorio.")  # Lanza error si falta el ID
        self._id_entidad = str(id_entidad).strip()  # Guarda el ID limpio en un atributo protegido

    @property  # Expone el atributo protegido como propiedad de solo lectura
    def id_entidad(self) -> str:  # Getter para obtener el identificador de la entidad
        """Retorna el identificador único de la entidad."""  # Documenta el método getter
        return self._id_entidad  # Devuelve el valor almacenado en _id_entidad

    @abstractmethod  # Marca el método como obligatorio para todas las subclases concretas
    def describir(self) -> str:  # Método abstracto para obtener una descripción legible de la entidad
        """Devuelve una descripción de la entidad."""  # Documenta el contrato del método abstracto
        pass  # Sin implementación en la clase base abstracta
