# 03. Estado del arte y recursos de partida

Este documento reúne recursos, herramientas e ideas de referencia mencionadas durante el desarrollo conceptual del proyecto.

## 1. Herramientas computacionales

### Python

Lenguaje principal del proyecto por su claridad, disponibilidad de bibliotecas científicas y facilidad para generar datos, figuras, archivos de audio y notebooks reproducibles.

Bibliotecas sugeridas:

- NumPy: cálculo numérico.
- Matplotlib: visualización.
- music21: manipulación musical simbólica.
- midiutil: generación de archivos MIDI.
- Jupyter: documentación computacional interactiva.

### Sonic Pi

Entorno de programación musical en tiempo real. Útil para probar ideas rápidamente, escuchar patrones y construir piezas sonoras con sintaxis accesible.

### Mathematica / KnotTheory

Herramienta útil para cálculo de invariantes, representaciones PD/BR y exploración computacional de teoría de nudos. En el historial del proyecto apareció como recurso asociado al estudio del invariante theta.

### SuperCollider / Pure Data / Max/MSP

Herramientas posibles para fases posteriores si se busca un control más avanzado del sonido, síntesis, espacialización o interacción en vivo.

## 2. Recursos sobre invariante theta

Recursos mencionados en el historial del proyecto:

- Reporte original sobre invariante theta: https://wolfr.am/Theta_Report
- Artículo del invariante theta: https://doi.org/10.48550/arXiv.2509.18456
- Código del reporte original: https://github.com/AliKarimLalani/theta_invariant
- Código/página de Dror Bar-Natan sobre theta: https://drorbn.net/AcademicPensieve/Projects/Theta/
- Nota de Quanta Magazine: https://wolfr.am/Quanta_Theta_Invariant

## 3. Ideas recuperadas de materiales traducidos

### Reporte sobre invariante theta

El reporte estudia el invariante theta de nudos, desarrollado por Dror Bar-Natan y Roland van der Veen, y lo aplica a familias de nudos como torales, pretzel y twisted torus knots. Desde el punto de vista de este proyecto, su utilidad está en que produce estructuras algebraicas/computacionales ricas que pueden ser convertidas en material sonoro.

Ideas aprovechables:

- usar coeficientes como secuencia;
- mapear grados/exponentes a altura o registro;
- mapear signo a dirección melódica o color tímbrico;
- mapear magnitud a intensidad o densidad;
- mapear familias de nudos a familias sonoras.

### Artículo de sonificación con Python/Jupyter

Se discutió un flujo de trabajo donde los datos se cargan, filtran, transforman y escuchan desde un entorno reproducible basado en código. Esta idea es central para el repositorio: cada ejemplo sonoro debe poder generarse de nuevo a partir de código y parámetros documentados.

## 4. Referencias funcionales para el proyecto

- Sonificación de datos en ciencia.
- Música algorítmica.
- Teoría de nudos computacional.
- Representación visual de estructuras matemáticas.
- Diseño de interfaces para exploración matemática sonora.

## 5. Criterio de selección de recursos

Para el proyecto se priorizarán recursos que cumplan al menos una de estas funciones:

1. Ayuden a calcular o representar estructuras matemáticas.
2. Ayuden a transformar estructuras en sonido.
3. Ayuden a documentar el proceso de manera reproducible.
4. Ayuden a justificar el proyecto desde arte, ciencia o divulgación.

