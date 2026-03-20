import datetime

# Colores para la terminal
VERDE, ROJO, RESET = "\033[92m", "\033[91m", "\033[0m"

def registrar_falla():
    print("\n" + "🛡️ " * 5 + " BITÁCORA DE SOBERANÍA L.I.N.A. " + "🛡️ " * 5)
    print("1. Registro de Servicio Técnico (Clientes)")
    print("2. Registro de Jornada Laboral (PRUEBA LEGAL)")
    
    op_interna = input("\nGerardo, ¿qué tipo de registro haremos?: ")

    if op_interna == "2":
        print("\n--- REGISTRO DE JORNADA (CONTRA EL 'Y YA') ---")
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        horas = float(input("¿Cuántas horas trabajó hoy? (ej: 14 o 38): "))
        pago = float(input("¿Cuánto le pagaron por este turno?: "))
        notas = input("Notas (ej: 'No me afiliaron', 'Turno dominical'): ")

        # CÁLCULO DE DEUDA EN TIEMPO REAL
        pago_justo = 135000 if horas < 24 else 450000
        deuda = pago_justo - pago

        with open("bitacora_libertad.txt", "a") as f:
            f.write(f"\nFECHA: {fecha}\nHORAS: {horas}\nPAGO: ${pago}\nDEUDA ESTIMADA: ${deuda}\nNOTAS: {notas}\n" + "-"*40)
        
        print(f"\n{VERDE}✅ Guardado. Deuda acumulada en este turno: ${deuda:,.2f}{RESET}")
    
    else:
        print("\n--- REGISTRO TÉCNICO ---")
        cliente = input("Nombre del Cliente: ")
        marca = input("Marca/Modelo: ")
        falla = input("Falla detectada: ")
        with open("recuerdos_tecnicos.txt", "a") as f:
            f.write(f"\nCLIENTE: {cliente} - EQUIPO: {marca} - FALLA: {falla}\n")
        print(f"\n{VERDE}✅ Servicio técnico registrado.{RESET}")

    input("\nPresione Enter para volver al Centro de Control...")