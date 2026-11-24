# 1823. Gas ideal

[Timus 1823](https://acm.timus.ru/problem.aspx?space=1&num=1823) · dificultad 348 · math

Problema original atribuido a Benoît Paul Émile Clapeyron y Dmitri Mendeléiev, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La ley de los gases ideales pV = nRT relaciona la presión p, la
cantidad de sustancia n, el volumen V y la temperatura T, con
R = 8.314. Se dan tres de los cuatro valores; hallar el cuarto. El
volumen y la temperatura deben ser positivos. Imprimir "error" si los
datos se contradicen y "undefined" si el valor no queda determinado de
forma única.

## Entrada

Tres líneas "X = value" para tres magnitudes distintas X entre p, n, V
y T, cada valor un entero no negativo de hasta 1000. Los V y T dados
son positivos.

## Salida

"X = value" con error absoluto o relativo de como mucho 10⁻⁶, o
"error", o "undefined".

## Evaluación

Las pruebas del repositorio comparan tokens numéricos con |resultado-referencia| <= 1e-6·max(1,|referencia|), rechazan valores no finitos y comparan exactamente los tokens no numéricos.

## Ejemplos

### Ejemplo 1

Entrada:

```
p = 1
n = 1
V = 1
```

Salida:

```
T = 0.120279
```

## Solución

Se despeja el valor que falta de pV = nRT; los valores dados son
enteros, así que toda comprobación de cero es exacta.

- p = nRT/V y n = pV/(RT): V y T están dados y son positivos, así que
  el resultado siempre está definido, quizá 0.
- V = nRT/p: si p = 0 la ecuación queda 0 = nRT, que vale para todo V
  cuando n = 0 ("undefined") y para ninguno cuando n > 0 ("error"). Si
  p > 0 y n = 0, V saldría 0, lo que no se permite ("error").
- T = pV/(nR) funciona igual, con n en lugar de p.

Se usa R = 8314/1000 para conservar cada resultado como una fracción
exacta de enteros a/b. Se redondea a seis decimales con aritmética entera,
redondeando los empates hacia arriba, y se imprimen la parte entera y
los seis dígitos decimales separados por un punto literal. Java usa
`Locale.ROOT` para los dígitos. El error absoluto de redondeo no supera
0.0000005 y todos los valores intermedios caben en enteros con signo de
64 bits bajo los límites de entrada.

`O(1)`.

En el ejemplo T = 1·1/(1·8.314) ≈ 0.120279.

Trampas:

- una presión nula o una cantidad de gas nula están permitidas y son
  una respuesta válida cuando la incógnita es p o n;
- un volumen o una temperatura calculados iguales a cero son un error,
  no una respuesta;
- las líneas pueden venir en cualquier orden;
- la salida numérica debe ser independiente de la configuración regional:
  el test 15 muestra que el formato predeterminado de Java puede imprimir
  `0,000000` en vez de `0.000000`.

## Soluciones optimizadas

`1823_math_optimized.java`. Conserva cálculo entero escalado exacto con R=8314/1000 y seis decimales. Cuatro long con -1 para la magnitud no negativa ausente reemplazan HashMap. Para V o T desconocido distingue 0=0 (undefined) de un solo factor cero (error) antes de dividir; V,T dados son positivos. Redondea la fracción a mitad hacia arriba con escala10^6 y emite dígitos, incluidas seis posiciones fraccionarias con ceros, sin printf/locale. El numerador escalado máximo es 8.314·10^15 y cabe en long. Tiempo y estado aritmético O(1), más búferes fijos.

Frente a `1823_math.java`: tiempo 0.093 s → 0.078 s; memoria 1736 KB → 504 KB.

`1823_math_optimized.py`. Conserva ecuación de gas y todas las ramas cero/undefined/error. Mantiene R=8314/1000 y redondeo entero de mitad hacia arriba a seis decimales, sin aproximación flotante. Solo cambia entrada cruda, decodificación ASCII y vida del intérprete. O(I) trabajo/espacio de entrada y número fijo de operaciones acotadas. Vacía respuesta antes de os._exit(0). Admisión por memoria medida del runtime propio, no nuevo algoritmo físico.

Frente a `1823_math.py`: tiempo 0.078 s → 0.125 s; memoria 572 KB → 284 KB.

Go y Rust guardan p, V, n y T en cuatro posiciones fijas y despejan la incógnita de 1000pV = 8314nT con enteros. Numerador y denominador nulos dan undefined. Un denominador nulo o volumen o temperatura forzados a cero dan error. En los demás casos redondean la fracción a seis decimales con enteros de 64 bits.

Las implementaciones base aceptadas [1823_math.cpp](1823_math.cpp), [1823_math.java](1823_math.java), [1823_math.py](1823_math.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1823_math_optimized.java`: puesto de tiempo 1/18 y de memoria 1/18 en esta muestra comparable.

`1823_math_optimized.py`: puesto de tiempo 11/17 y de memoria 1/17 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1823_math.cpp](1823_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 384 KB | 11325589 |
| [1823_math.go](1823_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1116 KB | 11298046 |
| [1823_math.java](1823_math.java) \* | Java 1.8 | math | O(1) | AC | 0.093 s | 1736 KB | 11298047 |
| [1823_math.py](1823_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 572 KB | 11298048 |
| [1823_math.rs](1823_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 424 KB | 11325613 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1823_math_optimized.go](1823_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 776 KB | 11311181 |
| [1823_math_optimized.rs](1823_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 208 KB | 11310736 |
| [1823_math_optimized.java](1823_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 504 KB | 11325039 |
| [1823_math_optimized.py](1823_math_optimized.py) \* | PyPy 3.10 x64 | math | O(I) input work; exact bounded arithmetic | AC | 0.125 s | 284 KB | 11325491 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
