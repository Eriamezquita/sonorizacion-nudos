# Sonorización de nudos

Repositorio del proyecto **Sonorización de nudos**, una investigación académico-artística-computacional que busca traducir estructuras de la teoría matemática de nudos en material sonoro y musical.

El proyecto se sitúa en el cruce entre matemáticas, física, música, arte, filología, programación y tecnología. Su propósito inicial no es solamente producir audios, sino construir un lenguaje de traducción entre objetos topológicos y parámetros musicales.

## Idea central

Un nudo no genera automáticamente una canción cerrada.  
Un nudo puede generar un **espacio de improvisación**.

La sonificación se entiende aquí como un puente entre:

```text
estructura matemática → representación computacional → mapeo sonoro → gesto musical → forma compositiva
```

El nudo aporta restricciones, simetrías, recurrencias, cruces, orientaciones y patrones. La música organiza esos datos como altura, ritmo, timbre, duración, densidad, dinámica, silencio, repetición e improvisación.

## Objetivos generales

- Estudiar familias básicas de nudos y sus representaciones.
- Construir mapeos entre propiedades matemáticas y parámetros sonoros.
- Implementar prototipos en Python y Sonic Pi.
- Generar ejemplos reproducibles de sonificación.
- Documentar el proceso de investigación 
- Crear una base clara para futuras extensiones hacia MIDI, audio, visualización interactiva y composición algorítmica.

## Estado actual

Estoy en etapa inicial de organización.  
La prioridad actual es rescatar y sistematizar las ideas desarrolladas durante el lapso de investigación para que no queden dispersas.

Este primer esbozo incluye:

- propuesta conceptual;
- marco matemático inicial;
- diseño preliminar de mapeos sonoros;
- estética musical del proyecto;
- ruta de trabajo para servicio social;
- primeros archivos de Sonic Pi y Python;
- bitácora;
- bibliografía base.

## Herramientas previstas

- Python
- Sonic Pi
- GitHub
- Markdown / LaTeX
- NumPy
- Matplotlib
- MIDI
- Mathematica / KnotTheory, en una etapa posterior
- Posibles herramientas de audio digital para edición y mezcla

## Estructura del repositorio

```text
sonorizacion-nudos/
├── README.md
├── MANIFEST.md
├── requirements.txt
├── docs/
│   ├── 00_estado_del_proyecto.md
│   ├── 01_manifiesto_conceptual.md
│   ├── 02_marco_teorico_nudos.md
│   ├── 03_sonificacion_y_mapeos.md
│   ├── 04_estetica_musical.md
│   ├── 05_theta_invariant.md
│   ├── 06_plan_tesis_servicio_social.md
│   ├── 07_referencias_iniciales.md
│   └── bitacora/
├── sonic_pi/
├── src/
│   ├── knots/
│   ├── sonification/
│   └── visualization/
├── notebooks/
├── data/
├── outputs/
└── tests/
```

## Primeros prototipos

- Sonificación del nudo trébol.
- Mapeo de cruces a eventos musicales.
- Conversión de coordenadas paramétricas a secuencias de notas.
- Exploración de la relación entre repetición topológica e improvisación musical.

## Dirección estética

El piano puede funcionar como voz topológica principal. Es decir, llevara el motivo de la pieza musical.
Después pueden incorporarse bajo, guitarra, percusión, sintetizadores u otras capas instrumentales en lineas de conversación con el motivo de la pieza o con el piano (donde estará la sonificación del nudo).

El jazz aparece como un lenguaje fértil porque permite trabajar con estructura, variación, conversación, tensión, resolución e improvisación. Una referencia estética importante es *A Love Supreme*, no para copiar su forma, sino por su potencia espiritual, modal, repetitiva y expansiva como fuente de inspiración o proyección creativa del proyecto.


