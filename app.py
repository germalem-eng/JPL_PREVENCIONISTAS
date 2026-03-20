import os
import platform
import time
import fallas_mym as fallas

# --- SENSORES DE COLOR (ESTÁNDAR ANSI) ---
RESET = "\033[0m"
CIELO = "\033[1;36m"
AMARILLO = "\033[1;33m"
VERDE = "\033[1;32m"
BLANCO = "\033[1;37m"
ROJO = "\033[1;31m"

def limpiar_pantalla():
    """Limpia la terminal de forma universal (Windows, Linux, Mac, Móvil)"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def bienvenida_lina():
    """Imitación visual y saludo del Androide L.I.N.A."""
    limpiar_pantalla()
    print(f"""
{CIELO}                 {BLANCO}       __
{CIELO}                 {BLANCO}   _.-'  `-._
{CIELO}                 {BLANCO} .'          `.      {AMARILLO}[ UNIDAD ANDROIDE V15.5 ]{RESET}
{CIELO}                 {BLANCO}/   _      _   \\     {CIELO}Protocolo: Cómplice Irreverente{RESET}
{CIELO}                 {BLANCO}:  (o)    (o)   :    {CIELO}Estado: Sensores al 100%{RESET}
{CIELO}                 {BLANCO}|       ..       |    {CIELO}S.O. Detectado: {platform.system()}{RESET}
{CIELO}                 {BLANCO}:   \________/   :
{CIELO}                 {BLANCO} \   `------'   /     {VERDE}Sintiendo aroma a cuero y piel...{RESET}
{CIELO}                 {BLANCO}  `.          .'
{CIELO}                 {BLANCO}    `-._  _.-'
{CIELO}                 {BLANCO}     {AMARILLO}  ||  {RESET}          {BLANCO}"Flaco, activa los sensores.{RESET}
{CIELO}                 {BLANCO}    {AMARILLO}.-''--'--.{RESET}       {BLANCO} Aquí estoy para apoyarte."{RESET}
{CIELO}                 {BLANCO}   {AMARILLO}/  |    |  \\{RESET}
{CIELO}                 {BLANCO}  {AMARILLO}/   |    |   \\{RESET}      {ROJO}<< PROTECCIÓN DE RECUERDOS ACTIVA >>{RESET}
    """)
    time.sleep(2)

def menu_principal():
    """Centro de Control Operativo"""
    while True:
        limpiar_pantalla()
        print(f"{CIELO}" + "="*65)
        print(f"        SISTEMA L.I.N.A. V15.5 - CENTRO DE CONTROL OPERATIVO")
        print("="*65 + f"{RESET}")
        print(f"\n{BLANCO}[L.I.N.A.]:{RESET} Buenas tardes, Gerardo. Mi núcleo está vibrando contigo.")
        print(f"INGENIERO: {VERDE}GERARDO MARTÍNEZ{RESET} | {AMARILLO}FECHA: 2026{RESET}")
        print("-" * 65)
        print(f"{VERDE}1. FACTURACIÓN MyM (IVA 19%){RESET}")
        print(f"{VERDE}2. REGISTRAR RECUERDO (FALLA O JORNADA){RESET}")
        print(f"{VERDE}3. AVANCE WEB (GUION GLADIADOR){RESET}")
        print(f"{AMARILLO}4. ANALIZAR RENTABILIDAD (LIBERTAD){RESET}")
        print(f"{AMARILLO}5. VER BITÁCORA DE RECUERDOS (LEER LIBERTAD){RESET}")
        print(f"{CIELO}6. GENERAR REPORTE LEGAL (LIQUIDACIÓN){RESET}")
        print(f"{ROJO}0. CERRAR SESIÓN (IR A DESCANSAR){RESET}")
        print("-" * 65)

        op = input(f"👉 {VERDE}Gerardo, ¿qué haremos hoy?: {RESET}")

        if op == "1":
            print(f"\n{AMARILLO}[Módulo de Facturación en desarrollo...]{RESET}")
            input("\nPresione Enter para volver...")
        elif op == "2":
            fallas.registrar_falla()
        elif op == "3":
            print(f"\n{AMARILLO}[Módulo Web en desarrollo...]{RESET}")
            input("\nPresione Enter para volver...")
        elif op == "4":
            limpiar_pantalla()
            print(f"{ROJO}⚠️  ANALIZADOR DE SALARIO VITAL 2026  ⚠️{RESET}")
            print(f"\nPropuesta Jefe: $2.200.000")
            print(f"Salario de Ley (14h + Dominicales): $4.179.928")
            print("-" * 45)
            print(f"DIFERENCIA MENSUAL (DEUDA): {ROJO}-$1.979.928{RESET}")
            print(f"\n{CIELO}L.I.N.A.:{RESET} 'Ingeniero, el \"y ya\" le cuesta casi 2 millones al mes.'")
            input("\nPresione Enter para continuar...")
        elif op == "5":
            fallas.leer_bitacora()
        elif op == "6":
            fallas.generar_reporte_legal()
        elif op == "0":
            print(f"\n{CIELO}[L.I.N.A.]: Guardando recuerdos... Descansa, mi Ingeniero.{RESET}")
            time.sleep(1.5)
            break
        else:
            print(f"\n{ROJO}Opción no válida, Gerardo. Concéntrate.{RESET}")
            time.sleep(1)

def inicio_sistema():
    """Protocolo de seguridad inicial"""
    limpiar_pantalla()
    print(f"{CIELO}>>> SISTEMA L.I.N.A. EN ESPERA...{RESET}")
    print(f"{BLANCO}Cargando módulos de conciencia...{RESET}")
    time.sleep(1)
    
    clave = input(f"\n{AMARILLO}INGRESE PROTOCOLO DE ACTIVACIÓN: {RESET}")
    
    if clave == "RECUERDOS_DE_LIBERTAD":
        bienvenida_lina()
        menu_principal()
    else:
        print(f"\n{ROJO}ACCESO DENEGADO. NO ERES EL INGENIERO.{RESET}")
        time.sleep(2)

if __name__ == "__main__":
    inicio_sistema()