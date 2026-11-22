# Sistema Integral de Gestión de Clientes, Servicios y Reservas — Software FJ

Proyecto desarrollado en Python bajo el paradigma orientado a objetos para la actividad **Fase 4 - Prácticas simuladas** del curso **Programación (213023)** de la UNAD[cite: 1, 6, 14].

## Características principales
- Gestión en memoria mediante objetos y listas internas (sin bases de datos)[cite: 6, 8, 14].
- Jerarquía de clases con abstracción (`EntidadBase`, `Servicio`), herencia, polimorfismo y encapsulación (`Cliente`)[cite: 7, 14].
- Excepciones personalizadas, bloques `try / except / else / finally` y encadenamiento (`raise ... from ...`)[cite: 7, 14].
- Registro de eventos y errores en `logs/software_fj.log`[cite: 8, 10, 14].
- Simulación de 12 operaciones en `main.py` con documentación línea por línea[cite: 3, 8, 14].

## Estructura del proyecto
- `excepciones.py`: Excepciones personalizadas del sistema[cite: 7, 9, 14].
- `Registro.py`: Configuración y funciones de registro de eventos y errores[cite: 10, 14].
- `entidad.py`: Clase abstracta base `EntidadBase`[cite: 7, 12, 14].
- `cliente.py`: Clase `Cliente` con encapsulación y validaciones[cite: 7, 14].
- `servicios.py`: Clase abstracta `Servicio` y clases derivadas (`ReservaSala`, `AlquilerEquipo`, `AsesoriaEspecializada`)[cite: 6, 7, 11, 14].
- `reserva.py`: Clase `Reserva` con gestión de estados y procesamiento seguro[cite: 7, 14].
- `main.py`: Simulación secuencial de operaciones sin base de datos[cite: 3, 6, 8, 14].
