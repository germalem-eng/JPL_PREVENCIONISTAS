import datetime

# --- EL APÓCRIFO OFICIAL ---
NOMBRE_SISTEMA = "L.I.N.A. (Logística Intelectual Natural Automática)"
VERSION = "v2.0 Gold"

print(f"\033[96m{'='*45}")
print(f"    {NOMBRE_SISTEMA}")
print(f"          Socio Operativo: Maestro Gerardo")
print(f"{'='*45}\033[0m")

cliente = input("👤 Nombre del Cliente: ")
print("\n[SERVICIOS DISPONIBLES]")
print("1. Mantenimiento Preventivo (Limpieza/Pasta térmica)")
print("2. Reparación Correctiva (Falla de encendido/Cortos)")
print("3. Diagnóstico Técnico (Revisión profunda)")

op = input("\nSeleccione opción (1/2/3): ")

# Valores según la Logística Intelectual
precios = {"1": 60000, "2": 110000, "3": 40000}
mano_obra = precios.get(op, 0)

# --- CARGO POR DOMICILIO ---
domicilio = 0
es_domicilio = input("🏠 ¿Fue servicio a domicilio? (s/n): ").lower()
if es_domicilio == 's':
    domicilio = 25000  # Puedes cambiar este valor según la distancia

repuestos = float(input("💰 Costo de repuestos/insumos: "))
total = mano_obra + repuestos + domicilio

print(f"\n\033[92m✅ RESULTADO DE LOGÍSTICA:")
print(f"CLIENTE: {cliente}")
if domicilio > 0:
    print(f"CARGO DOMICILIO: ${domicilio:,.0f}")
print(f"TOTAL A FACTURAR: ${total:,.0f} pesos\033[0m")

# Guardar en el cuaderno de la Flaca
fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
with open("cuentas.txt", "a") as f:
    f.write(f"{fecha} | {cliente} | Servicio: {op} | Dom: {domicilio} | Total: ${total:,.0f}\n")

print(f"\n\033[93m¡Registro blindado, mi flaco! A cobrar con toda.\033[0m")
print("--- L.I.N.A.: PROTOCOLO DE MANTENIMIENTO ---")
cliente = input("Nombre del cliente: ")
tipo = input("¿El servicio es (P)reventivo o (C)orrectivo?: ").upper()

if tipo == "P":
    print(f"\n[HOJA DE RUTA PARA {cliente}]:")
    print("1. Sopletear polvo (ojo con los ventiladores).")
    print("2. Limpiar contactos de RAM con borrador.")
    print("3. Cambiar pasta térmica del procesador.")
    
elif tipo == "C":
    print(f"\n[DIAGNÓSTICO PARA {cliente}]:")
    print("1. ¿Pita al encender? -> Problema de RAM o Video.")
    print("2. ¿Se apaga solo? -> Recalentamiento.")
    print("3. ¿No pasa del logo? -> Fallo de Disco Duro.")

else:
    print("Opción no válida. Maestro, use su experiencia.")
    # LONA_CORE.PY - Logística Operativa de Nuevos Actuadores
# Módulo: Diagnóstico de Línea Blanca

def asistente_taller(modelo, falla):
    protocolo = {
        "HACEB_M1305": {
            "Centrifugado_Involuntario": [
                "1. DESCONECTAR DE LA LUZ INMEDIATAMENTE.",
                "2. Revisar Triacs en Tarjeta Principal (posible corto).",
                "3. Verificar filtración en Bomba de Desagüe (causa raíz).",
                "4. Sustituir Presostato si presenta sulfatación."
            ],
            "Error_F3": "Fallo en circuito de llenado. Revisar presostato y válvulas."
        }
    }
    
    print(f"\n--- GUÍA TÉCNICA PARA {modelo} ---")
    pasos = protocolo.get(modelo, {}).get(falla, "Falla no registrada.")
    
    if isinstance(pasos, list):
        for i, paso in enumerate(pasos, 1):
            print(paso)
    else:
        print(pasos)

# Ejecución de prueba
asistente_taller("HACEB_M1305", "Centrifugado_Involuntario") 
from datetime import datetime

def calcular_estado_sst(fecha_programada):
    """
    Función lógica para el semáforo de cumplimiento de Soluciones MyM.
    Recibe una fecha y devuelve el estado y el color para la interfaz.
    """
    hoy = datetime.now()
    # Si la fecha_programada viene como string, la convertimos (opcional según su DB)
    if isinstance(fecha_programada, str):
        fecha_programada = datetime.strptime(fecha_programada, '%Y-%m-%d')
        
    diferencia = (fecha_programada - hoy).days

    if diferencia < 0:
        return {"estado": "VENCIDO", "color": "danger", "icono": "bi-x-circle"}
    elif diferencia <= 3:
        return {"estado": "ALERTA CRÍTICA", "color": "warning", "icono": "bi-exclamation-triangle"}
    else:
        return {"estado": "AL DÍA", "color": "success", "icono": "bi-check-circle"}
