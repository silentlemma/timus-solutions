# 1117. Recorrer un árbol binario numerado en orden de un número a otro

[Timus 1117](https://acm.timus.ru/problem.aspx?space=1&num=1117) · dificultad 281 · math

Problema original de Alexander Somov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los nodos de un árbol binario perfecto están numerados `1, 2, 3, …` en
orden simétrico: cada nodo interno tiene un número entre los de sus dos
hijos, y todos los de un subárbol quedan del mismo lado. Un mensaje va del
número `i` al número `j` pasando por cada número intermedio, un paso cada
vez; un paso entre `k` y `k ± 1` cuesta tantos días como nodos del árbol
haya estrictamente entre ellos en el camino del árbol (0 para un padre y
su hijo). Halla el total de días para `1 ≤ i, j ≤ 2^31 − 1`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`i j` en una línea.

## Salida

El número de días.

## Evaluación

Comparar un token entero exacto, ignorando espacios de formato. El nuevo código Python exacto pasó 12 pruebas del repositorio con PyPy 3.10. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 5
```

Salida:

```
2
```

## Solución

En un árbol perfecto numerado en orden simétrico, la altura del nodo `x`
sobre las hojas es el número de bits cero finales `tz(x)`: las hojas son
los impares, sus padres los `2 mod 4`, y así sucesivamente. De dos números
consecutivos uno es impar, una hoja, y el par `e` es su antepasado a
altura `tz(e)`, así que el paso cuesta `tz(e) − 1` días. Cada número par
estrictamente entre `i` y `j` se usa en dos pasos, y un extremo par en uno.

Con `c(e) = tz(e) − 1 = tz(e/2)`, la suma de `c` sobre los pares hasta `n`
es `Σ_{y ≤ n/2} tz(y) = m − popcount(m)` con `m = ⌊n/2⌋` (cada `y` aporta
sus ceros finales, y `Σ_{t≥1} ⌊m/2^t⌋ = m − popcount(m)`). Así, para
`i < j` la respuesta es `2·(G(j) − G(i − 1)) − c(i) − c(j)`, donde `G` es
esa suma y `c` de un impar vale 0. `O(1)`.

Detalles a tener en cuenta:

- la mayor respuesta, para `1` y `2^31 − 1`, es `2147483586`, solo 61 por
  debajo del límite de 32 bits con signo; las soluciones usan 64 bits por
  seguridad;
- el orden de `i` y `j` no importa;
- no se da el tamaño del árbol, pero no importa: los números en orden
  simétrico y las alturas son los mismos en cualquier árbol perfecto lo
  bastante grande para contener ambos números.

Las respuestas se comprobaron con un recorrido del árbol real (el padre
de `x` es `x ± 2^tz(x)`) que suma las longitudes de camino paso a paso,
para 300 pares aleatorios menores que 3000, y las pruebas grandes con un
bucle directo sobre cada paso.

## Soluciones optimizadas

`1117_math_optimized.rs`. Mantiene fórmula de distancia mediante ceros finales y popcount. Lee dos extremos escalares y usa min/max en vez de vector de dos elementos y ordenación. Emite entero directamente sin formato. Igualdad da cero, correcciones de extremos y aritmética se mantienen. O(1) tiempo y espacio bajo los límites del enunciado.

Frente a `1117_math.rs`: tiempo 0.015 s → 0.015 s; memoria 224 KB → 60 KB.

Se mantiene la identidad de coste prefijo. Con h=floor(x/2), partir de 2*(h-popcount(h)); si x es par, restar trailingZeros(x)-1. El conteo de bits y el bit activo menos significativo sustituyen el recorrido de bits sin alterar el entero exacto. La respuesta sigue siendo la diferencia absoluta de prefijos. Las etiquetas caben en el rango fijo del problema. Python usa los flujos existentes; el ahorro y el mayor tiempo se muestran por separado.

- `1117_math_optimized.java`: 0.093 s / 352 KB; base `1117_math.java`: 0.109 s / 1616 KB; cambio respecto a la base: tiempo -14.7%, memoria -78.2%.
- `1117_math_optimized.py`: 0.109 s / 264 KB; base `1117_math.py`: 0.078 s / 436 KB; cambio respecto a la base: tiempo +39.7%, memoria -39.4%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1117_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1117_math.cpp](1117_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11279242 |
| [1117_math.go](1117_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1052 KB | 11279244 |
| [1117_math.java](1117_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1616 KB | 11279246 |
| [1117_math.py](1117_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB | 11279245 |
| [1117_math.rs](1117_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB | 11279248 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1117_math_optimized.java](1117_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 352 KB | 11309311 |
| [1117_math_optimized.py](1117_math_optimized.py) | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 264 KB | 11309685 |
| [1117_math_optimized.rs](1117_math_optimized.rs) | Rust 1.75 x64 | math | O(1), fixed-width bit operations | AC | 0.015 s | 60 KB | 11325497 |
