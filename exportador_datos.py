# exportador_datos.py
import datetime
import os

def exportar_ticket_txt(resultado, justificacion, nombre_archivo="ticket_ensamble.txt"):
    try:
        # Obtenemos la ruta actual para guardar el archivo en la misma carpeta
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_completa = os.path.join(ruta_actual, nombre_archivo)
        
        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            archivo.write("====================================================\n")
            archivo.write("      TICKET DE ENSAMBLE - SISTEMA EXPERTO          \n")
            archivo.write("====================================================\n")
            archivo.write(f"Fecha de consulta: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            archivo.write("[ COMPONENTES RECOMENDADOS ]\n")
            for componente, detalle in resultado["componentes"].items():
                archivo.write(f" - {componente}: {detalle}\n")
            
            if resultado["alertas"]:
                archivo.write("\n[ ALERTAS DE RENDIMIENTO ]\n")
                for alerta in resultado["alertas"]:
                    archivo.write(f" ! {alerta}\n")
                    
            if justificacion:
                archivo.write("\n[ JUSTIFICACIÓN DEL EXPERTO ]\n")
                archivo.write(justificacion + "\n")
                
            archivo.write("\n====================================================\n")
            archivo.write("Gracias por utilizar nuestro sistema experto.\n")
            
        return True, ruta_completa
    except Exception as e:
        return False, str(e)