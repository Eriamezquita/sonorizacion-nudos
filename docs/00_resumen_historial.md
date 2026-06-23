# 00. Resumen útil recuperado del historial del proyecto

Este documento concentra las ideas útiles discutidas para convertir el trabajo del Laboratorio de Sonorización y Visualización de las Matemáticas en un repositorio de investigación y creación computacional.

## Núcleo del proyecto

El proyecto busca **hacer sonar estructuras matemáticas**, comenzando con nudos matemáticos. La intención no es solamente convertir datos a sonido de manera decorativa, sino construir una traducción formal, documentada y reproducible entre propiedades matemáticas y parámetros acústicos.

La pregunta guía puede formularse así:

> ¿Cómo diseñar una correspondencia clara entre una estructura matemática y una estructura sonora, de modo que el sonido conserve información matemática y a la vez tenga valor perceptivo, expresivo y artístico?

## Motivación conceptual

Durante las conversaciones se sostuvo una intuición central: la música y las matemáticas son lenguajes altamente estructurados, pero no existe una traducción universal directa entre ambos. Por eso, el proyecto debe construir **reglas de mapeo explícitas**, no asumir que una red neuronal o una conversión automática resuelve el problema de fondo.

La sonificación debe entenderse como una mediación entre:

- formalismo matemático;
- programación;
- percepción auditiva;
- teoría musical;
- visualización;
- documentación científica.

## Ejes acumulados

### 1. Eje matemático

- Teoría de nudos.
- Representaciones de nudos: diagramas, cruces, palabras de trenza, representaciones PD/BR.
- Nudos básicos: trébol, figura ocho, nudos torales, pretzel y twisted torus knots.
- Invariantes: número de cruces, orientación, writhe, polinomios de Alexander/Jones y, en una fase avanzada, el invariante theta.
- Posibilidad de usar estructuras discretas como ciclos, permutaciones, palabras, signos y coeficientes como material sonoro.

### 2. Eje computacional

- Python como lenguaje principal.
- Jupyter Notebook para experimentación, explicación y reproducibilidad.
- Bibliotecas posibles: NumPy, Matplotlib, music21, midiutil.
- Sonic Pi para prototipos sonoros en tiempo real.
- Posibilidad posterior de usar SuperCollider, Pure Data, Max/MSP o Ableton si el proyecto crece hacia composición sonora más avanzada.

### 3. Eje sonoro/musical

- Mapeo de variables matemáticas a frecuencia, duración, amplitud y timbre.
- Uso de escalas, motivos, ritmo, repetición, recursividad y estructura formal.
- Interés en una sonificación que no sea arbitraria: cada decisión musical debe estar justificada por una propiedad matemática.
- Posibilidad de producir un álbum o colección de piezas sonoras en YouTube/SoundCloud/Spotify.

### 4. Eje visual

- Visualización de nudos y estructuras asociadas.
- Figuras que acompañen cada sonificación.
- Posibilidad de combinar imagen, sonido y explicación matemática en una plataforma digital.

### 5. Eje de documentación

- Repositorio digital con código, ejemplos, audio, figuras, bitácora y reporte final.
- Documentación clara en español.
- Plantilla de informe final.
- Organización suficiente para que el trabajo sea útil como servicio social, investigación inicial, divulgación y posible base de tesis.

## Ideas específicas que deben conservarse

1. **Primer prototipo concreto:** sonorizar el nudo trébol.
2. **Ruta mínima:** nudo → representación → secuencia → mapeo → audio → visualización → explicación.
3. **Uso de palabra de trenza:** por ejemplo, representar el trébol como cierre de una palabra de trenza y mapear los generadores a motivos sonoros.
4. **Uso de cruces:** los cruces pueden controlar altura, duración, intensidad o articulación.
5. **Uso de signos/orientación:** los signos positivos/negativos pueden controlar dirección melódica, modo, paneo o timbre.
6. **Uso de invariantes:** coeficientes de polinomios o del invariante theta pueden convertirse en material musical.
7. **Uso de ciclos y permutaciones:** las estructuras de permutación pueden convertirse en cánones, polirritmos, entradas escalonadas o motivos repetitivos.
8. **Uso de curvas geométricas:** la curva de Hilbert apareció como ejemplo de mapeo geometría → música.
9. **No depender solamente de IA:** una red neuronal puede ser útil, pero el fundamento del proyecto debe estar en reglas de traducción/mapeo explicables.
10. **Repositorio como entrega:** el trabajo debe quedar como código organizado, material sonoro y documentación reproducible.

## Producto esperado al final

- Repositorio GitHub con código y documentación.
- Ejemplos sonoros generados desde estructuras matemáticas.
- Figuras/visualizaciones asociadas.
- Informe final.
- Posible plataforma de difusión digital.
- Posible álbum de sonificaciones.

