# motor_inferencia.py
from base_conocimiento import obtener_configuracion_base, obtener_luces_rgb

class SistemaExpertoPC:
    def __init__(self):
        self.base_de_hechos = {}
        self.alertas_sistema = []

    def evaluar_requisitos(self, marca, presupuesto, uso, red, rgb):
        self.base_de_hechos = {
            "marca_preferida": marca,
            "presupuesto_nivel": presupuesto,
            "uso_nivel": uso,
            "conexion_red": red,
            "quiere_rgb": rgb
        }

        config_inicial = obtener_configuracion_base(presupuesto, uso, marca)
        
        if "error" in config_inicial:
            return {"exito": False, "mensaje": config_inicial["error"], "alertas": []}
            
        componentes_finales = config_inicial["componentes"].copy()
        
        if "flags" in config_inicial:
            for flag_nombre, flag_valor in config_inicial["flags"].items():
                self.base_de_hechos[flag_nombre] = flag_valor

        if self.base_de_hechos["conexion_red"] == "wifi":
            componentes_finales["Receptor de Red"] = "Receptor Wi-Fi agregado."
        
        if self.base_de_hechos["quiere_rgb"] == "si" and "Luces RGB" not in componentes_finales:
            componentes_finales["Sistema RGB"] = obtener_luces_rgb(presupuesto)

        self._ejecutar_reglas_por_flags(componentes_finales)

        return {
            "exito": True, 
            "componentes": componentes_finales,
            "alertas": self.alertas_sistema
        }

    def _ejecutar_reglas_por_flags(self, componentes):
        # Reglas de CPU
        if self.base_de_hechos.get("Componente_CPU") == "Gama Alta":
            if "PSU" in componentes:
                componentes["PSU"] += " (Exigencia: Certificación 80 Plus Gold)"
            componentes["Chasis Recomendado"] = "Gabinete High Airflow con soporte radiador 360mm."
            self.alertas_sistema.append(
                "Detectamos hardware de Gama Alta. Aplique pasta térmica premium (> 8.5 W/mK)."
            )
            
        # NUEVO: Reglas de Cuello de Botella (Monitor)
        nivel_gpu = self.base_de_hechos.get("Nivel_GPU")
        if nivel_gpu == "Media-Alta":
            componentes["Monitor Sugerido"] = "Monitor 1440p (2K) a 144Hz."
        elif nivel_gpu in ["Alta", "Ultra"]:
            componentes["Monitor Sugerido"] = "Monitor 4K a 120Hz/144Hz."
            self.alertas_sistema.append(
                "PREVENCIÓN DE CUELLO DE BOTELLA: Tu tarjeta gráfica es muy potente. "
                "Usarla con un monitor 1080p limitará severamente su potencial. Invierte en un buen monitor 4K o 1440p UltraWide."
            )

    # NUEVO: Motor de Justificación
    def generar_justificacion(self):
        justificacion = (
            f"El sistema ha tomado estas decisiones basándose en su presupuesto '{self.base_de_hechos['presupuesto_nivel']}' "
            f"y su necesidad orientada a '{self.base_de_hechos['uso_nivel']}'.\n"
        )
        
        if self.base_de_hechos['marca_preferida'] != "sin preferencia":
            justificacion += f"- Se priorizó la arquitectura {self.base_de_hechos['marca_preferida'].capitalize()} según su elección explícita en la primera pregunta realizada.\n"
            
        if self.base_de_hechos.get("Componente_CPU") == "Gama Alta":
            justificacion += "- Al estar en una categoría de hardware extrema, se dedujo internamente la necesidad de modificar el chasis y agregar exigencias a la fuente de poder para evitar sobrecalentamientos.\n"
            
        if self.base_de_hechos.get("Nivel_GPU") in ["Media-Alta", "Alta", "Ultra"]:
            justificacion += "- El sistema analizó la potencia gráfica deducida (Flag: GPU Fuerte) y agregó un monitor acorde a la lista para evitar cuellos de botella visuales.\n"
            
        return justificacion