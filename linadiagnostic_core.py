import datetime
import os

# Definición de la Paleta de Colores (Adiós al Verde)
CIELO = '\033[96m'    # Cyan / Azul Cielo
BLANCO = '\033[1;37m'  # Blanco Brillante
ROJO = '\033[91m'    # Rojo (solo para errores críticos)
RESET = '\033[0m'     # Volver a color normal

def generar_factura_real(nombre, detalles):
    b, i, t = detalles['base'], detalles['iva'], detalles['total']
    rep = detalles['inf_repuesto']
    nombre_archivo = f"FACTURA_{nombre.upper().replace(' ', '_')}.txt"
    
    # Diseño de la interfaz en terminal (Todo en Azul Cielo y Blanco)
    diseno_pantalla = f"""
{CIELO}██████████████████████████████████████████████████████
      SERVICIO TÉCNICO ESPECIALIZADO L.I.N.A.
██████████████████████████████████████████████████████{RESET}
{BLANCO}FECHA:{RESET} {datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}
{BLANCO}CLIENTE:{RESET} {nombre.upper()}
{CIELO}------------------------------------------------------{RESET}
{BLANCO}DETALLE DEL TRABAJO:{RESET}
- {rep}
{CIELO}------------------------------------------------------{RESET}
{BLANCO}SUBTOTAL:{RESET}           ${b:,.0f}
{BLANCO}IVA (19%):{RESET}          ${i:,.0f}
{CIELO}------------------------------------------------------{RESET}
{CIELO}>>> TOTAL A PAGAR:      ${t:,.0f} <<<{RESET}
{CIELO}------------------------------------------------------{RESET}
      {CIELO}Su técnico de confianza: Gerardo Martínez{RESET}
{CIELO}██████████████████████████████████████████████████████{RESET}
"""
    # Guardar en archivo (Texto puro para impresión)
    contenido_txt = diseno_pantalla.replace(CIELO, "").replace(RESET, "").replace(BLANCO, "")
    with open(nombre_archivo, "w") as f:
        f.write(contenido_txt)
    
    print(diseno_pantalla)
    print(f"{CIELO}✅ Registro completado exitosamente.{RESET}")
    print(f"{CIELO}📄 Factura creada como: {nombre_archivo}{RESET}")

# --- INICIO DEL PROGRAMA ---
# Limpiamos la pantalla para que no se vea nada del sistema antes de empezar
os.system('clear')

print(f"{CIELO}=============================================")
print(f"      GENERADOR DE FACTURAS L.I.N.A.")
print(f"============================================={RESET}")

try:
    cliente = input(f"{BLANCO}👤 Nombre del Cliente: {RESET}")
    base = float(input(f"{BLANCO}💰 Valor total del servicio: ${RESET}") or 0)
    detalle = input(f"{BLANCO}📝 Descripción del trabajo: {RESET}")
    
    iva = base * 0.19
    total = base + iva
    
    generar_factura_real(cliente, {'base': base, 'iva': iva, 'total': total, 'inf_repuesto': detalle})

except ValueError:
    print(f"\n{ROJO}❌ ERROR: Por favor, ingrese un valor numérico válido.{RESET}")