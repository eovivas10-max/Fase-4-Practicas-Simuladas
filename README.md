# Sistema Integral de Gestión de Clientes, Servicios y Reservas — Software FJ  # Título principal del repositorio

Proyecto desarrollado en Python bajo el paradigma orientado a objetos para la actividad **Fase 4 - Prácticas simuladas** del curso **Programación (213023)** de la UNAD.  # Contexto académico del proyecto

## Características principales  # Sección de características
- Gestión en memoria mediante objetos y listas internas (sin bases de datos).  # Requisito de persistencia en memoria
- Jerarquía de clases con abstracción (`EntidadBase`, `Servicio`), herencia, polimorfismo y encapsulación (`Cliente`).  # Principios POO aplicados
- Excepciones personalizadas, bloques `try / except / else / finally` y encadenamiento (`raise ... from ...`).  # Manejo de errores exigido
- Registro de eventos y errores en `logs/software_fj.log`.  # Trazabilidad en archivo de logs
- Simulación de 12 operaciones en `main.py` con documentación línea por línea.  # Pruebas y documentación

## Estructura del proyecto  # Sección de archivos del repositorio
- `excepciones.py`: Excepciones personalizadas del sistema.  # Descripción de excepciones.py
- `Registro.py`: Configuración y funciones de registro de eventos y errores.  # Descripción de Registro.py
- `entidad.py`: Clase abstracta base `EntidadBase`.  # Descripción de entidad.py
- `cliente.py`: Clase `Cliente` con encapsulación y validaciones.  # Descripción de cliente.py
- `servicios.py`: Clase abstracta `Servicio` y clases derivadas (`ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`).  # Descripción de servicios.py
- `reserva.py`: Clase `Reserva` con gestión de estados y procesamiento seguro.  # Descripción de reserva.py
- `main.py`: Simulación secuencial de operaciones sin base de datos.  # Descripción de main.py
