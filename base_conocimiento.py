# base_conocimiento.py

def obtener_luces_rgb(presupuesto):
    luces = {
        "bajo": "Tira de Luces Rgb Neon Chassis (15600)",
        "medio": "Raidmax NV-A120R3 120mm RGB Fan",
        "alto": "Lian Li Ventilador Uni SI 120 3 Unidades"
    }
    return luces.get(presupuesto)

def seleccionar_procesador(gama, marca):
    opciones = {
        "baja": {
            "intel": ("Intel Core i3-12100F", "Socket LGA 1700"),
            "amd": ("AMD Ryzen 3 4100", "Socket AM4"),
            "sin preferencia": ("Intel Core i3-12100F / AMD Ryzen 3 4100", "Socket LGA 1700 (Intel) o AM4 (AMD)")
        },
        "media": {
            "intel": ("Intel Core i5-13400F", "Socket LGA 1700"),
            "amd": ("AMD Ryzen 5 5600X", "Socket AM4"),
            "sin preferencia": ("Intel Core i5-13400F / AMD Ryzen 5 5600X", "Socket LGA 1700 / AM4")
        },
        "alta": {
            "intel": ("Intel Core i7-13700K", "Socket LGA 1700"),
            "amd": ("AMD Ryzen 7 7800X3D", "Socket AM5"),
            "sin preferencia": ("Intel Core i7-13700K / AMD Ryzen 7 7800X3D", "Socket LGA 1700 (Intel) o AM5 (AMD)")
        }
    }
    return opciones[gama][marca]

def obtener_configuracion_base(presupuesto, uso, marca):
    if presupuesto == "medio" and uso == "livianos":
        presupuesto = "bajo"
    
    if presupuesto == "bajo":
        cpu, placa = seleccionar_procesador("baja", marca)
    elif presupuesto == "medio":
        cpu, placa = seleccionar_procesador("media", marca)
    else:
        cpu, placa = seleccionar_procesador("alta", marca)

    configuraciones = {
        "bajo": {
            "livianos": {
                "componentes": {
                    "CPU": cpu,
                    "Placa Base": placa,
                    "RAM": "8 GB",
                    "Tarjeta Grafica": "RTX 3050 (200 USD)",
                    "SSD": "512GB (50 USD)",
                    "PSU": "550W",
                    "Disipador": "25 USD"
                },
                "flags": {"Nivel_GPU": "Entrada"}
            },
            "pesados": {"error": "No es posible armar una PC Gamer con un presupuesto bajo."},
            "streaming": {"error": "No es posible streaming de alta calidad ni armar una PC Gamer con un presupuesto bajo."}
        },
        "medio": {
            "pesados": {
                "componentes": {
                    "CPU": cpu,
                    "Placa Base": placa,
                    "RAM": "16 GB",
                    "Tarjeta Grafica": "RTX 4070",
                    "SSD": "1TB (116 USD)",
                    "PSU": "650W",
                    "Disipador": "50 USD"
                },
                "flags": {"Nivel_GPU": "Media-Alta"}
            },
            "streaming": {
                "componentes": {
                    "CPU": cpu,
                    "Placa Base": placa,
                    "RAM": "32 GB",
                    "Tarjeta Grafica": "RTX 5070",
                    "SSD": "1TB (116 USD)",
                    "PSU": "750W",
                    "Disipador": "50 USD",
                    "Luces RGB": "Sí incluye por defecto"
                },
                "flags": {"Nivel_GPU": "Alta"}
            }
        }
    }
    
    if presupuesto == "alto":
        return {
            "componentes": {
                "CPU": cpu,
                "Placa Base": placa,
                "RAM": "32 GB",
                "Tarjeta Grafica": "RTX 5080",
                "SSD": "2TB (369 USD)",
                "PSU": "850W",
                "Refrigeracion Liquida": "180 USD",
                "Luces RGB": "Sí incluye por defecto"
            },
            "flags": {"Componente_CPU": "Gama Alta", "Nivel_GPU": "Ultra"}
        }
        
    return configuraciones.get(presupuesto, {}).get(uso)