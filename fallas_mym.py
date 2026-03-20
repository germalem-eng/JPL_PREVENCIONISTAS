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
        notas = input("Notas: ")

        # Lógica de cálculo de deuda basada en Salario Vital 2026
        pago_justo = 135000 if horas < 24 else 450000
        deuda = pago_justo - pago

        with open("bitacora_libertad.txt", "a") as f:
            f.write(f"\nFECHA: {fecha}\nHORAS: {horas}\nPAGO RECIBIDO: ${pago}\nDEUDA ESTIMADA: ${deuda}\nNOTAS: {notas}\n" + "-"*40)
        
        print(f"\n{VERDE}✅ Guardado. Deuda acumulada en este turno: ${deuda:,.2f}{RESET}")
    
    else:
        print("\n--- REGISTRO TÉCNICO ---")
        cliente = input("Nombre del Cliente: ")
        falla = input("Falla detectada: ")
        with open("recuerdos_tecnicos.txt", "a") as f:
            f.write(f"\nFECHA: {datetime.datetime.now()}\nCLIENTE: {cliente}\nFALLA: {falla}\n" + "-"*30)
        print(f"\n{VERDE}✅ Servicio técnico registrado.{RESET}")

    input("\nPresione Enter para volver...")

def leer_bitacora():
    print("\n" + "📖 " * 5 + " LEYENDO RECUERDOS DE LIBERTAD " + "📖 " * 5)
    try:
        with open("bitacora_libertad.txt", "r") as f:
            contenido = f.read()
            if contenido:
                print(contenido)
            else:
                print(f"{ROJO}La bitácora está vacía, Ingeniero.{RESET}")
    except FileNotFoundError:
        print(f"{ROJO}L.I.N.A.: Aún no existe el archivo de recuerdos.{RESET}")
    
    input("\nPresione Enter para volver...") 
def generar_reporte_legal():
    print("\n" + "⚖️  " * 5 + " GENERANDO REPORTE DE DEUDA LABORAL " + "⚖️  " * 5)
    total_deuda = 0
    total_horas = 0
    try:
        with open("bitacora_libertad.txt", "r") as f:
            lineas = f.readlines()
            
        print(f"\n{VERDE}--- RESUMEN DE EVIDENCIA ACUMULADA ---{RESET}")
        for linea in lineas:
            if "HORAS:" in linea:
                h = float(linea.split(":")[1].strip())
                total_horas += h
            if "DEUDA ESTIMADA: $" in linea:
                d = float(linea.split("$")[1].strip())
                total_deuda += d
                print(linea.strip())
        
        print("-" * 40)
        print(f"TOTAL HORAS REGISTRADAS: {total_horas}")
        print(f"{ROJO}DEUDA TOTAL ESTIMADA: ${total_deuda:,.2f}{RESET}")
        print(f"{VERDE}L.I.N.A.: 'Este documento es su base para la liquidación, Ingeniero.'{RESET}")
        
    except FileNotFoundError:
        print(f"{ROJO}No hay datos para procesar.{RESET}")
    
    input("\nPresione Enter para volver al Centro de Control...")