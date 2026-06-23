# 04. Mapeos sonoros

Este documento define estrategias iniciales para convertir propiedades matemáticas en sonido. Todo mapeo debe documentarse porque constituye una decisión interpretativa del proyecto.

## 1. Principio general

Un mapeo sonoro tiene la forma:

```text
objeto matemático → propiedad extraída → normalización → parámetro sonoro → evento musical
```

Ejemplo:

```text
cruce positivo → signo +1 → dirección ascendente → intervalo +2 semitonos
cruce negativo → signo -1 → dirección descendente → intervalo -2 semitonos
```

## 2. Mapeos básicos

| Propiedad matemática | Parámetro sonoro posible | Justificación |
|---|---|---|
| Número de cruces | Duración total o densidad | Mayor complejidad puede producir más eventos |
| Signo del cruce | Dirección melódica | Positivo/negativo se percibe como ascenso/descenso |
| Magnitud de coeficiente | Amplitud o número de repeticiones | Mayor magnitud puede escucharse como mayor presencia |
| Exponente de polinomio | Altura o registro | Los grados ordenan una secuencia discreta |
| Palabra de trenza | Secuencia rítmica/melódica | La palabra ya es una sucesión temporal |
| Componente del nudo/enlace | Capa instrumental | Cada componente puede tener una voz propia |
| Familia de nudos | Timbre o escala | Cada familia puede tener identidad sonora |
| Writhe | Centro tonal o desplazamiento | Resume polaridad global del diagrama |
| Simetría | Repetición, inversión o canon | La simetría puede escucharse como retorno formal |

## 3. Estrategia A: cruces como eventos

Cada cruce se convierte en un evento sonoro.

- Cruce positivo: intervalo ascendente.
- Cruce negativo: intervalo descendente.
- Orden de lectura del diagrama: orden temporal.
- Tipo de cruce: timbre o articulación.
- Número total de cruces: duración total o número de pulsos.

Ventaja: es una estrategia simple y explicable.

Limitación: depende de la elección del diagrama y del orden de lectura.

## 4. Estrategia B: palabra de trenza como partitura

Una palabra de trenza se interpreta como una partitura discreta.

Ejemplo conceptual:

```text
[+1, +1, +1] → motivo ascendente repetido tres veces
[+1, -2, +1] → motivo A, motivo B invertido, motivo A
```

Reglas posibles:

- índice del generador → altura base;
- signo del generador → dirección melódica;
- repetición del generador → repetición rítmica;
- longitud de la palabra → duración de la frase.

## 5. Estrategia C: coeficientes de polinomios o invariantes

Si un invariante produce una lista de coeficientes, se puede usar como secuencia sonora.

Ejemplo:

```text
coeficientes = [-1, 3, 0, -2, 5]
```

Mapeo posible:

- índice del coeficiente → tiempo;
- signo → modo/timbre/dirección;
- magnitud → volumen/duración/densidad;
- cero → silencio;
- valor extremo → acento.

Esta estrategia será útil para polinomios de Alexander/Jones y, más adelante, para el invariante theta.

## 6. Estrategia D: ciclos y permutaciones

Las permutaciones pueden mapearse a entradas de voces, cánones o polirritmos.

Ejemplo conceptual:

```text
(1 9 5)(2 10 6)
```

Posibles interpretaciones:

- cada ciclo es una voz;
- la longitud del ciclo controla duración;
- los elementos del ciclo controlan alturas;
- ciclos simultáneos producen textura polifónica.

## 7. Estrategia E: geometría a sonido

Para estructuras geométricas como curvas o trayectorias:

- coordenada x → tiempo o paneo;
- coordenada y → altura;
- distancia entre puntos → duración;
- curvatura → timbre o vibrato;
- densidad local → textura.

Esta estrategia se relaciona con la idea discutida de usar la curva de Hilbert como ejemplo de mapeo geometría → música.

## 8. Criterios de evaluación de un mapeo

Un mapeo será útil si cumple estos criterios:

1. **Claridad:** se puede explicar de forma breve.
2. **Reproducibilidad:** el mismo objeto produce el mismo sonido.
3. **Sensibilidad:** objetos distintos producen diferencias audibles.
4. **Fidelidad:** el sonido conserva información relevante.
5. **Escalabilidad:** puede aplicarse a más de un nudo.
6. **Valor perceptivo:** se puede escuchar sin que sea caótico o arbitrario.

## 9. Primera decisión práctica

El primer prototipo usará el nudo trébol representado de manera simplificada por una secuencia de cruces/generadores. La salida será un archivo WAV generado en Python y una versión equivalente en Sonic Pi.

