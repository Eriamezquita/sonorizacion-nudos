# Sonificación y mapeos

## 1. Sonificación

La sonificación consiste en representar datos, relaciones o estructuras mediante sonido. En este proyecto no se busca una conversión arbitraria de números a notas, sino un sistema de mapeos con sentido matemático y musical.

## 2. Variables matemáticas posibles

- número de cruces;
- tipo de cruce;
- orientación;
- secuencia de sobrecruces y bajocruces;
- curvatura local;
- torsión;
- longitud de arco;
- coordenadas paramétricas;
- familia del nudo;
- invariante asociado;
- grado o coeficientes de un polinomio;
- estructura de una representación PD o BR.

## 3. Parámetros musicales posibles

- altura;
- duración;
- ritmo;
- amplitud;
- timbre;
- articulación;
- densidad;
- registro;
- silencio;
- repetición;
- variación;
- instrumento;
- espacialización.

## 4. Mapeo inicial

| Matemática | Sonido |
|---|---|
| Cruce positivo | nota ascendente o acento brillante |
| Cruce negativo | nota descendente o acento oscuro |
| Paso por arriba | registro agudo |
| Paso por abajo | registro grave |
| Número de cruces | cantidad de eventos por ciclo |
| Longitud de arco | duración total o fraseo |
| Curvatura | intensidad o vibrato |
| Familia del nudo | escala, modo o paleta tímbrica |
| Invariante | motivo estable que permanece durante variaciones |

## 5. Criterios de diseño

Un buen mapeo debe cumplir tres condiciones:

1. **Coherencia matemática**: debe respetar algún rasgo real del nudo.
2. **Claridad perceptiva**: debe producir diferencias audibles.
3. **Valor musical**: debe permitir organización, variación o composición.

## 6. Problema fundamental

No toda información matemática debe convertirse en sonido.  
La sonificación requiere seleccionar qué estructura se quiere hacer audible.

## 7. Mapeo como hipótesis

Cada mapeo debe tratarse como una hipótesis de investigación:

> Si esta propiedad matemática se transforma en este parámetro sonoro, ¿el oyente puede percibir una diferencia estructural?

## 8. Primer flujo técnico

```text
nudo → datos matemáticos → lista de eventos → mapeo → Sonic Pi / MIDI → audio
```

## 9. Primer prototipo

El primer prototipo debe concentrarse en el nudo trébol:

- generar una secuencia de tres cruces;
- asignar signo a cada cruce;
- mapear cada cruce a nota y duración;
- repetir el patrón con variaciones;
- escuchar si aparece identidad musical.
