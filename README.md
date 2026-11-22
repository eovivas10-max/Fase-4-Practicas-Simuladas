# Sistema Integral de Gestión de Clientes, Servicios y Reservas — Software FJ

Proyecto desarrollado en Python bajo el paradigma orientado a objetos para la actividad **Fase 4 - Prácticas simuladas** del curso **Programación (213023)** de la UNAD

## Características principales
- Gestión en memoria mediante objetos y listas internas (sin bases de datos)
- Jerarquía de clases con abstracción (`EntidadBase`, `Servicio`), herencia, polimorfismo y encapsulación (`Cliente`)
- Excepciones personalizadas, bloques `try / except / else / finally` y encadenamiento (`raise ... from ...`)
- Registro de eventos y errores en `logs/software_fj.log`
- Simulación de 12 operaciones en `main.py` con documentación línea por línea

## Estructura del proyecto
- `excepciones.py`: Excepciones personalizadas del sistema
- `Registro.py`: Configuración y funciones de registro de eventos y errores
- `entidad.py`: Clase abstracta base `EntidadBase`
- `cliente.py`: Clase `Cliente` con encapsulación y validaciones.
- `servicios.py`: Clase abstracta `Servicio` y clases derivadas (`ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`)
- `reserva.py`: Clase `Reserva` con gestión de estados y procesamiento seguro.
- `main.py`: Simulación secuencial de operaciones sin base de datos.
