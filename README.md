# Sonorización y visualización de nudos matemáticos

Repositorio base para el proyecto del **Laboratorio de Sonorización y Visualización de las Matemáticas**: exploración computacional, visual y sonora de estructuras matemáticas, con énfasis inicial en **teoría de nudos**.

Este repositorio reúne el plan de trabajo, la bitácora conceptual, el marco teórico inicial, los mapeos matemático-sonoros y una primera base de código en Python/Sonic Pi para generar ejemplos sonoros reproducibles.

## Idea central

El proyecto busca construir un puente entre:

```text
estructura matemática → representación computacional → mapeo acústico → pieza sonora / visualización / reporte
```

En la primera etapa se trabajará con nudos básicos, propiedades combinatorias y representaciones como palabras de trenza, diagramas de cruces y, de forma progresiva, invariantes como polinomios e invariantes computables.

## Plan general

### I. Introducción: 19 de mayo – 19 de junio

- Instalación y capacitación en Python.
- Introducción a Sonic Pi y generación de sonido en tiempo real.
- Diseño de mapeos entre variables matemáticas y parámetros acústicos.
- Introducción a la sonificación de datos en ciencia y arte.
- Introducción a teoría de nudos y sus representaciones matemáticas.

### II. Desarrollo de la sonorización: 19 de junio – 29 de diciembre

- Estudio y representación de nudos básicos.
- Herramientas computacionales para manipular estructuras asociadas a nudos.
- Estrategias de sonorización desde cruces, secuencias, trenzas, invariantes y estructura.
- Implementación en Python y Sonic Pi.
- Producción de ejemplos sonoros.

### III. Montaje y reporte final: 29 de diciembre – 18 de mayo de 2027

- Documentación del código.
- Organización del repositorio digital.
- Integración del material sonoro en una plataforma de difusión digital.
- Elaboración de informe final.

## Estructura del repositorio

```text
sonorizacion-nudos-repo/
├── README.md
├── requirements.txt
├── docs/
│   ├── 00_resumen_historial.md
│   ├── 01_plan_trabajo.md
│   ├── 02_marco_teorico.md
│   ├── 03_estado_del_arte_y_recursos.md
│   ├── 04_mapeos_sonoros.md
│   ├── 05_bitacora_decisiones.md
│   ├── 06_roadmap_2026_2027.md
│   ├── 07_reporte_final_plantilla.md
│   ├── 08_difusion_album.md
│   ├── 09_github_paso_a_paso.md
│   └── 10_glosario.md
├── bibliography/
│   └── referencias.bib
├── src/
│   ├── knots/
│   │   ├── __init__.py
│   │   ├── representations.py
│   │   └── trefoil.py
│   └── sonification/
│       ├── __init__.py
│       ├── mapping.py
│       └── synthesis.py
├── examples/
│   └── demo_trebol_sonificacion.py
├── sonic_pi/
│   └── trebol_basico.rb
├── notebooks/
│   └── 00_inicio.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── audio/
│   └── figures/
└── tests/
    └── test_mapping.py
```

## Instalación rápida

Desde la terminal, dentro de la carpeta del repositorio:

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate       # Windows PowerShell
pip install -r requirements.txt
```

## Primer ejemplo reproducible

Ejecuta:

```bash
python examples/demo_trebol_sonificacion.py
```

Esto genera una primera sonificación del nudo trébol en:

```text
outputs/audio/trebol_demo.wav
outputs/figures/trebol_eventos.png
```

## Ruta mínima del proyecto

1. Representar un nudo básico, por ejemplo el nudo trébol.
2. Extraer una estructura discreta: cruces, palabra de trenza, signos, secuencias.
3. Definir un mapeo sonoro: frecuencia, duración, intensidad, timbre.
4. Generar sonido con Python y/o Sonic Pi.
5. Documentar el proceso con figuras, audio y explicación matemática.
6. Repetir el procedimiento con más nudos y comparar resultados.

## Estado actual

Repositorio inicial de trabajo. Contiene una estructura organizada, documentos base y código demostrativo. La siguiente fase consiste en sustituir ejemplos simbólicos por datos matemáticos calculados o importados desde herramientas especializadas.

