# main.py
from motor_inferencia import SistemaExpertoPC
from exportador_datos import exportar_ticket_txt

def solicitar_entrada(mensaje, opciones_validas):
    while True:
        print(f"\n{mensaje}")
        for i, opcion in enumerate(opciones_validas, 1):
            print(f"{i}. {opcion.capitalize()}")
        
        seleccion = input("Elige el número de tu opción: ").strip()
        
        if seleccion.isdigit():
            indice = int(seleccion) - 1
            if 0 <= indice < len(opciones_validas):
                return opciones_validas[indice]
        print(">> Error: Entrada inválida. Por favor, selecciona un número de la lista.")

def iniciar_consola():
    print("="*60)
    print("      SISTEMA EXPERTO: ARMADO DE PC GAMER V3.0")
    print("="*60)
    
    marca = solicitar_entrada("1.Selecciona tu procesador preferido:", ["intel", "amd", "sin preferencia"])
    presupuesto = solicitar_entrada("2.Presupuesto disponible:", ["bajo", "medio", "alto"])
    uso = solicitar_entrada("3.Uso principal del equipo:", ["livianos", "pesados", "streaming"])
    red = solicitar_entrada("4.Tipo de conexión a red requerida:", ["wifi", "ethernet"])
    rgb = solicitar_entrada("5.¿Deseas incluir luces RGB adicionales?:", ["si", "no"])
    
    # Procesamiento del motor
    sistema = SistemaExpertoPC()
    resultado = sistema.evaluar_requisitos(marca, presupuesto, uso, red, rgb)
    
    if not resultado["exito"]:
        print(f"\n>> ALERTA DEL SISTEMA: {resultado['mensaje']}\n")
        return # Termina el programa si hay error lógico

    # Mostrar resultados en consola
    print("\n" + "="*60)
    print("               DIAGNÓSTICO DEL ENSAMBLE")
    print("="*60)
    
    print("\n[ COMPONENTES RECOMENDADOS ]")
    for componente, detalle in resultado["componentes"].items():
        print(f" • {componente}: {detalle}")
        
    if resultado["alertas"]:
        print("\n[ NOTAS DEL EXPERTO ]")
        for alerta in resultado["alertas"]:
            print(f" -> {alerta}")
            
    print("="*60)

    # NUEVO: Justificación del Sistema
    quiere_justificacion = solicitar_entrada("¿Deseas saber el razonamiento (Por qué) de estas decisiones?", ["si", "no"])
    texto_justificacion = ""
    if quiere_justificacion == "si":
        texto_justificacion = sistema.generar_justificacion()
        print("\n[ JUSTIFICACIÓN DEL SISTEMA EXPERTO ]")
        print(texto_justificacion)

    # NUEVO: Módulo de Exportación
    quiere_exportar = solicitar_entrada("¿Deseas exportar esta recomendación a un archivo de texto?", ["si", "no"])
    if quiere_exportar == "si":
        exito, ruta = exportar_ticket_txt(resultado, texto_justificacion)
        if exito:
            print(f"\n>> ¡Éxito! El ticket ha sido guardado correctamente en:\n>> {ruta}\n")
        else:
            print(f"\n>> Ocurrió un error al guardar el archivo: {ruta}\n")

if __name__ == "__main__":
    iniciar_consola()