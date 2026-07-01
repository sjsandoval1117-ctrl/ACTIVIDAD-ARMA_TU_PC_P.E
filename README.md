# Sistema Experto: Armado de PC Gamer 🖥️⚙️

Este proyecto es un **Sistema Experto basado en reglas** desarrollado en Python, diseñado para asesorar a los usuarios en la selección y compra de componentes para armar una PC Gamer. Utiliza un motor de inferencia con encadenamiento hacia adelante para deducir requerimientos técnicos complejos a partir de entradas sencillas del usuario.

## 🔗 Enlace a la Base de Datos Documental
La lógica completa, las reglas de producción y los nodos de decisión que alimentan este sistema se encuentran documentados en el siguiente enlace:
[Documento de Base de Datos - Nodos y Reglas](https://docs.google.com/document/d/1KAqunlgVcY_6NsRhhOPHjkJU9NIcBMfT1VAY_-h6eOs/edit?usp=sharing)

## ✨ Características Principales
* **Motor de Inferencia Modular:** Separa la interfaz de usuario, la base de hechos y las reglas de negocio.
* **Prevención de Cuellos de Botella:** Identifica configuraciones gráficas potentes y ajusta las recomendaciones de periféricos (monitores) para maximizar el rendimiento.
* **Módulo de Justificación:** El sistema es capaz de explicar paso a paso ("Caja de Cristal") el porqué de sus decisiones técnicas.
* **Persistencia de Datos:** Permite exportar la configuración final y las alertas de ensamblaje a un archivo de texto (`.txt`) a modo de ticket de compra.

## 📂 Estructura del Proyecto
El sistema se compone de 4 módulos principales:
1. `main.py`: Interfaz de usuario por consola y controlador principal del flujo.
2. `motor_inferencia.py`: Cerebro del sistema experto. Evalúa hechos, dispara reglas y genera alertas y justificaciones.
3. `base_conocimiento.py`: Base de datos estática. Contiene el mapeo de procesadores, tarjetas gráficas y componentes base por presupuesto.
4. `exportador_datos.py`: Módulo de persistencia encargado de generar el archivo físico con los resultados.

## 🚀 Cómo ejecutar el sistema
### Requisitos
* Python 3.x instalado en tu sistema.
* No requiere librerías externas (solo módulos nativos de Python: `os`, `datetime`).

### Instrucciones
1. Clona o descarga este repositorio asegurando que los 4 archivos `.py` estén en la misma carpeta.
2. Abre una terminal (o la consola integrada de VS Code) y navega hasta el directorio del proyecto.
3. Ejecuta el archivo principal con el siguiente comando:
   ```bash
   python main.py
