from cliente import Cliente  # Importa la clase Cliente
from excepciones import ErrorSoftwareFJ, ReservaInvalidaError  # Importa excepciones base y de reserva
from Registro import registrar_error, registrar_evento  # Importa funciones para escribir en el archivo de logs
from reserva import Reserva  # Importa la clase Reserva
from servicios import AlquilerEquipo, AsesoriaEspecializada, ReservaSala  # Importa los 3 servicios especializados

def ejecutar_simulacion():  # Ejecuta la simulación exigida de al menos 10 operaciones en memoria
    """Simula 12 operaciones de clientes, servicios y reservas sin usar base de datos."""  # Documenta la simulación
    clientes = []  # Lista interna en memoria para almacenar clientes válidos (sin BD)
    servicios = []  # Lista interna en memoria para almacenar servicios válidos (sin BD)
    reservas = []  # Lista interna en memoria para almacenar reservas creadas/procesadas (sin BD)

    registrar_evento("=== Inicio de simulación Software FJ ===")  # Registra inicio de sesión en el log

    # --- OPERACIÓN 1: Registro válido de cliente ---  # Separador de operación 1
    try:  # Inicia bloque de prueba para registrar un cliente válido
        c1 = Cliente("CLI-01", "Laura Gómez", "laura.gomez@empresa.com")  # Crea cliente válido
    except ErrorSoftwareFJ as err:  # Captura errores de dominio del sistema
        registrar_error("Operación 1 fallida al crear cliente", err)  # Registra el error en el log
        print(f"[Op 1 - Error] {err}")  # Informa por consola sin detener el programa
    else:  # Se ejecuta si no hubo excepciones en try
        clientes.append(c1)  # Agrega el cliente a la lista en memoria
        print(f"[Op 1 - OK] {c1.describir()}")  # Muestra confirmación en consola
    finally:  # Se ejecuta siempre al cerrar el bloque
        print("[Op 1] Bloque finalizado.")  # Confirma cierre de la operación

    # --- OPERACIÓN 2: Registro inválido de cliente (correo mal formado) ---  # Separador de operación 2
    try:  # Intenta crear un cliente con correo inválido
        c2 = Cliente("CLI-02", "Carlos Ruiz", "correo-no-valido")  # Provoca ClienteInvalidoError
    except ErrorSoftwareFJ as err:  # Captura el error personalizado
        registrar_error("Operación 2 fallida por correo inválido", err)  # Registra en archivo de logs
        print(f"[Op 2 - Error controlado] {err}")  # Muestra error controlado
    else:  # Ejecuta solo si se creó el cliente sin errores
        clientes.append(c2)  # Guarda en lista interna
        print(f"[Op 2 - OK] {c2.describir()}")  # Muestra descripción
    finally:  # Cierra bloque de la operación 2
        print("[Op 2] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 3: Segundo registro válido de cliente ---  # Separador de operación 3
    try:  # Intenta registrar un segundo cliente válido
        c3 = Cliente("CLI-03", "Andrés Mendoza", "andres.mendoza@correo.co")  # Crea cliente válido
    except ErrorSoftwareFJ as err:  # Captura errores de dominio
        registrar_error("Operación 3 fallida al crear cliente", err)  # Registra en log
        print(f"[Op 3 - Error] {err}")  # Informa error
    else:  # Ejecuta si la creación fue exitosa
        clientes.append(c3)  # Almacena en lista en memoria
        print(f"[Op 3 - OK] {c3.describir()}")  # Muestra cliente registrado
    finally:  # Cierra bloque de la operación 3
        print("[Op 3] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 4: Registro inválido de cliente (nombre vacío) ---  # Separador de operación 4
    try:  # Intenta registrar un cliente con nombre vacío
        c4 = Cliente("CLI-04", "   ", "ana.torres@empresa.com")  # Provoca ClienteInvalidoError
    except ErrorSoftwareFJ as err:  # Captura error de validación
        registrar_error("Operación 4 fallida por nombre vacío", err)  # Registra en archivo de logs
        print(f"[Op 4 - Error controlado] {err}")  # Muestra mensaje controlado
    else:  # Ejecuta si no hubo error
        clientes.append(c4)  # Guarda en lista
        print(f"[Op 4 - OK] {c4.describir()}")  # Muestra descripción
    finally:  # Cierra bloque de la operación 4
        print("[Op 4] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 5: Creación correcta de servicio ReservaSala ---  # Separador de operación 5
    try:  # Crea un servicio de reserva de sala válido
        s1 = ReservaSala("SRV-SALA-1", "Sala Ejecutiva Norte", 50.0, capacidad=12, disponible=True)  # Crea sala
    except ErrorSoftwareFJ as err:  # Captura error de dominio
        registrar_error("Operación 5 fallida al crear sala", err)  # Registra en log
        print(f"[Op 5 - Error] {err}")  # Muestra error
    else:  # Ejecuta si se creó correctamente
        servicios.append(s1)  # Agrega a la lista de servicios
        print(f"[Op 5 - OK] {s1.describir()}")  # Muestra descripción
    finally:  # Cierra bloque de la operación 5
        print("[Op 5] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 6: Creación correcta de servicios AlquilerEquipo y AsesoriaEspecializada ---  # Separador de operación 6
    try:  # Crea dos servicios adicionales válidos
        s2 = AlquilerEquipo("SRV-EQ-1", "Proyector 4K", 35.0, codigo_equipo="EQ-409", disponible=True)  # Crea equipo
        s3 = AsesoriaEspecializada("SRV-ASE-1", "Arquitectura Cloud", 120.0, especialidad="Cloud", disponible=False)  # No disponible
    except ErrorSoftwareFJ as err:  # Captura error de dominio
        registrar_error("Operación 6 fallida al crear servicios", err)  # Registra en log
        print(f"[Op 6 - Error] {err}")  # Muestra error
    else:  # Ejecuta si ambos servicios se crearon bien
        servicios.extend([s2, s3])  # Agrega ambos servicios a la lista en memoria
        print(f"[Op 6 - OK] {s2.describir()} | {s3.describir()}")  # Muestra servicios creados
    finally:  # Cierra bloque de la operación 6
        print("[Op 6] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 7: Creación incorrecta de servicio (tarifa negativa / inconsistente) ---  # Separador de operación 7
    try:  # Intenta crear un servicio con tarifa base negativa
        s_malo = AlquilerEquipo("SRV-EQ-BAD", "Laptop Corporativa", -25.0, codigo_equipo="EQ-999")  # CalculoInconsistenteError
    except ErrorSoftwareFJ as err:  # Captura el error de cálculo/validación
        registrar_error("Operación 7 fallida por tarifa negativa", err)  # Registra en log
        print(f"[Op 7 - Error controlado] {err}")  # Muestra error controlado
    else:  # Ejecuta si no hubo error
        servicios.append(s_malo)  # Agrega a lista
        print(f"[Op 7 - OK] {s_malo.describir()}")  # Muestra descripción
    finally:  # Cierra bloque de la operación 7
        print("[Op 7] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 8: Reserva exitosa de sala con descuento e impuesto opcionales ---  # Separador de operación 8
    try:  # Crea y procesa una reserva válida de sala
        r1 = Reserva("RES-01", clientes[0], servicios[0], duracion=3, descuento_pct=10.0, impuesto_pct=19.0)  # Reserva sala
        total_r1 = r1.procesar()  # Calcula costo con parámetros opcionales y confirma
    except ErrorSoftwareFJ as err:  # Captura errores del sistema
        registrar_error("Operación 8 fallida en reserva de sala", err)  # Registra en log
        print(f"[Op 8 - Error] {err}")  # Muestra error
    else:  # Ejecuta si la reserva se procesó sin errores
        reservas.append(r1)  # Guarda la reserva en la lista en memoria
        print(f"[Op 8 - OK] {r1.describir()} (Calculado: ${total_r1:.2f})")  # Muestra resultado
    finally:  # Cierra bloque de la operación 8
        print("[Op 8] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 9: Reserva exitosa de alquiler de equipo ---  # Separador de operación 9
    try:  # Crea y procesa una reserva válida de alquiler de equipo
        r2 = Reserva("RES-02", clientes[1], servicios[1], duracion=2)  # Usa valores por defecto de descuento/impuesto
        total_r2 = r2.procesar()  # Procesa y confirma la reserva
    except ErrorSoftwareFJ as err:  # Captura errores de dominio
        registrar_error("Operación 9 fallida en reserva de equipo", err)  # Registra en log
        print(f"[Op 9 - Error] {err}")  # Muestra error
    else:  # Ejecuta si se procesó correctamente
        reservas.append(r2)  # Agrega a la lista de reservas
        print(f"[Op 9 - OK] {r2.describir()} (Calculado: ${total_r2:.2f})")  # Muestra resultado
    finally:  # Cierra bloque de la operación 9
        print("[Op 9] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 10: Reserva fallida por servicio no disponible ---  # Separador de operación 10
    try:  # Intenta reservar la asesoría marcada como disponible=False
        r3 = Reserva("RES-03", clientes[0], servicios[2], duracion=1)  # Lanza ServicioNoDisponibleError
    except ErrorSoftwareFJ as err:  # Captura error de disponibilidad
        registrar_error("Operación 10 fallida por servicio no disponible", err)  # Registra en log
        print(f"[Op 10 - Error controlado] {err}")  # Muestra error controlado
    else:  # Ejecuta solo si no hubo error
        reservas.append(r3)  # Agrega a lista
        print(f"[Op 10 - OK] {r3.describir()}")  # Muestra descripción
    finally:  # Cierra bloque de la operación 10
        print("[Op 10] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 11: Reserva fallida con encadenamiento explícito de excepciones (raise ... from ...) ---  # Separador op 11
    try:  # Simula una entrada externa corrupta al construir una reserva
        try:  # Bloque interno que provoca un error de tipo/valor
            duracion_invalida = int("no_es_numero")  # Provoca ValueError nativo de Python
        except ValueError as error_conversion:  # Captura el ValueError original
            raise ReservaInvalidaError(  # Encadena el ValueError dentro de ReservaInvalidaError
                "Duración inválida suministrada para la reserva RES-04."
            ) from error_conversion  # Vincula error_conversion como __cause__
    except ErrorSoftwareFJ as err:  # Captura la excepción encadenada
        registrar_error("Operación 11 fallida con encadenamiento", err)  # Registra error y su causa original
        print(f"[Op 11 - Error encadenado] {err} | Causa: {err.__cause__}")  # Muestra detalle en consola
    else:  # Ejecuta si no hubo error
        print("[Op 11 - OK] Duración válida.")  # Mensaje de éxito
    finally:  # Cierra bloque de la operación 11
        print("[Op 11] Bloque finalizado.")  # Traza de cierre

    # --- OPERACIÓN 12: Operación no permitida al cancelar dos veces una reserva ---  # Separador de operación 12
    try:  # Intenta cancelar la reserva r1 dos veces consecutivas
        reservas[0].cancelar()  # Primera cancelación: pasa a CANCELADA
        reservas[0].cancelar()  # Segunda cancelación: lanza OperacionNoPermitidaError
    except ErrorSoftwareFJ as err:  # Captura la excepción de operación no permitida
        registrar_error("Operación 12 fallida por doble cancelación", err)  # Registra en log
        print(f"[Op 12 - Error controlado] {err}")  # Muestra error controlado
    else:  # Ejecuta si no hubo error
        print("[Op 12 - OK] Reserva cancelada.")  # Mensaje de éxito
    finally:  # Cierra bloque de la operación 12
        print("[Op 12] Bloque finalizado.")  # Traza de cierre

    registrar_evento(  # Registra el resumen final de objetos en memoria al cerrar la simulación
        f"=== Fin de simulación | Clientes: {len(clientes)} | Servicios: {len(servicios)} | Reservas: {len(reservas)} ==="
    )
    print("\nSimulación completada sin interrupciones. Revisa el archivo 'logs/software_fj.log'.")  # Aviso final

if __name__ == "__main__":  # Verifica que el script se ejecute directamente y no al ser importado
    ejecutar_simulacion()  # Inicia la simulación completa
