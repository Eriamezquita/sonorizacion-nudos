# 02. Marco teórico inicial

## 1. Sonificación de datos

La sonificación de datos consiste en representar información mediante sonido. A diferencia de una visualización, que transforma datos en formas, colores o posiciones espaciales, una sonificación transforma datos en parámetros acústicos perceptibles: altura, intensidad, duración, timbre, espacialización, textura o ritmo.

En este proyecto, la sonificación no se entiende como una conversión automática, sino como un proceso de diseño formal:

```text
variable matemática → regla de mapeo → parámetro acústico → evento sonoro
```

La calidad del mapeo depende de que la relación sea:

- explícita;
- reproducible;
- interpretable;
- suficientemente fiel a la estructura matemática;
- perceptualmente clara.

## 2. Parámetros acústicos básicos

Los parámetros principales que se usarán son:

- **Frecuencia:** determina la altura percibida del sonido.
- **Amplitud:** determina la intensidad o volumen.
- **Duración:** determina cuánto tiempo permanece un evento sonoro.
- **Timbre:** distingue la cualidad del sonido, incluso si dos sonidos tienen la misma frecuencia e intensidad.
- **Ritmo:** organiza duraciones y acentos en el tiempo.
- **Registro:** ubica los sonidos en zonas graves, medias o agudas.
- **Textura:** describe cuántas capas sonoras ocurren simultáneamente y cómo interactúan.

## 3. Teoría de nudos

La teoría de nudos estudia curvas cerradas embebidas en el espacio tridimensional. Dos nudos se consideran equivalentes si uno puede deformarse continuamente en el otro sin cortar ni pegar la curva.

Para trabajar computacionalmente con nudos, se utilizan representaciones discretas. Algunas de las más útiles para este proyecto son:

### Diagrama de nudo

Proyección plana de un nudo tridimensional con información de sobrecruce y subcruce. Cada cruce contiene información combinatoria que puede convertirse en secuencia sonora.

### Número de cruces

Cantidad mínima de cruces necesaria para representar un nudo. Puede servir como parámetro global para duración, densidad sonora o complejidad.

### Orientación

Dirección asignada a la curva. Puede permitir distinguir movimientos ascendentes/descendentes, dirección melódica o circulación espacial.

### Writhe

Suma de signos de los cruces en un diagrama orientado. Puede mapearse a modo, polaridad, centro tonal o desplazamiento de registro.

### Palabra de trenza

Algunos nudos pueden representarse como cierres de trenzas. Una palabra de trenza se compone de generadores y sus inversos. Esta representación es especialmente útil para sonificación porque ya posee una estructura secuencial.

Ejemplo conceptual:

```text
σ1 σ1 σ1  →  motivo A, motivo A, motivo A
σ1^-1     →  motivo A invertido o descendente
```

### Representación PD

La representación PD describe un diagrama de nudo mediante información combinatoria de cruces. Es útil para conectar el proyecto con herramientas computacionales de teoría de nudos.

## 4. Invariantes de nudos

Un invariante es una cantidad, polinomio o estructura asociada a un nudo que permanece igual bajo deformaciones equivalentes. En sonificación, los invariantes son útiles porque proporcionan información matemática estable.

Posibles invariantes para etapas progresivas:

- número de cruces;
- número de componentes;
- writhe del diagrama;
- polinomio de Alexander;
- polinomio de Jones;
- invariante theta.

## 5. Invariante theta como fase avanzada

El invariante theta es una estructura computable reciente de interés en teoría de nudos. En el historial del proyecto se discutió la posibilidad de usar sus coeficientes como material sonoro:

```text
coeficientes del invariante theta → alturas / acordes / densidad / timbre / intensidad
```

Una estrategia razonable es no comenzar directamente con theta, sino construir primero el flujo completo con nudos básicos y mapeos simples. Después se pueden sustituir las secuencias iniciales por coeficientes o estructuras derivadas del invariante theta.

## 6. Música algorítmica

La música algorítmica utiliza reglas, procedimientos o código para generar material musical. Este proyecto se ubica en un punto intermedio entre música algorítmica y sonificación científica: el sonido se produce por reglas computacionales, pero dichas reglas están justificadas por estructuras matemáticas.

## 7. Problema filosófico de la traducción

Matemáticas y música son lenguajes estructurados, pero no hay una gramática universal para traducir uno en otro. Por ello, cada mapeo debe declararse como una decisión de diseño y justificarse.

El proyecto debe evitar afirmaciones como:

> “El nudo suena así de manera natural.”

Y preferir formulaciones como:

> “Bajo este sistema de mapeo, esta propiedad del nudo se representa mediante este parámetro acústico.”

