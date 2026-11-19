# 1111. Ordenar cuadrados por su distancia a un punto

[Timus 1111](https://acm.timus.ru/problem.aspx?space=1&num=1111) · dificultad 383 · geometry

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n` cuadrados rellenos (`1 ≤ n ≤ 50`), cada uno dado por dos
vértices opuestos con coordenadas enteras en `(−9999, 9999)`; los
cuadrados pueden estar girados en cualquier ángulo, y un cuadrado puede
reducirse a un punto. La distancia de un punto `P` a un cuadrado es la
longitud del segmento más corto de `P` a un punto del cuadrado, así que
es 0 cuando `P` está dentro. Imprime los números de los cuadrados
ordenados por distancia, primero el menor número en caso de empate.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`n`, luego `n` líneas `x1 y1 x2 y2` con dos vértices opuestos, y luego la
línea `x y` de `P`.

## Salida

Los números de los cuadrados (desde 1) en orden, separados por espacios.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0 1 1
0 3 1 4
0 0
```

Salida:

```
1 2
```

## Solución

Se mira cada cuadrado desde su centro `C`, con `D = (x2 − x1, y2 − y1)`
la diagonal. Sus lados van en la dirección de `D` girada `±45°`, es decir
de `D ± D⊥`, donde `D⊥` es `D` girada `90°`. Con el desplazamiento
doblado `q = 2P − (x1 + x2, y1 + y2)`, todo entero, las proyecciones de
`q` en las dos direcciones de los lados son `s1 = |q · (D + D⊥)|` y
`s2 = |q · (D − D⊥)|`, y `P` está dentro exactamente cuando ambas valen
como mucho `h = |D|²`. Fuera, los excesos `a = max(0, s1 − h)` y
`b = max(0, s2 − h)` dan la distancia al cuadrado `(a² + b²) / (8h)`, y un
cuadrado reducido a un punto da `|q|² / 4`.

Así cada distancia al cuadrado es una fracción exacta de enteros, y dos
se comparan multiplicando en cruz, usando el índice original en los
empates. Se lee `P` y se calcula toda expresión que lo contiene con
enteros de precisión arbitraria; solo las coordenadas acotadas de los
vértices y los denominadores usan enteros de ancho fijo. Hay
`O(n log n)` comparaciones. Si `L` es la máxima longitud decimal de una
coordenada de `P` (al menos 1), con multiplicación escolar la cota es
`O(n L² + n log n L)` de tiempo y `O(n L)` de memoria de trabajo.
El tamaño de los denominadores está acotado.

Detalles a tener en cuenta:

- los empates son frecuentes, por cuadrados simétricos y por `P` dentro
  de varios, así que la comparación debe ser exacta: en coma flotante dos
  distancias iguales pueden quedar en cualquier orden;
- la cota de los vértices no limita `P`. En la prueba `09` las dos
  distancias son iguales, pero el numerador del cuadrado es `2^64`:
  ampliar solo la comparación final llega demasiado tarde. Ni siquiera
  128 bits cubren todo `P` válido; la lectura, las proyecciones, los
  cuadrados y las comparaciones requieren precisión arbitraria;
- los vértices dados son opuestos, no contiguos, y cualquiera de las dos
  diagonales en cualquier sentido describe el mismo cuadrado.

Las respuestas se comprobaron con un cálculo exacto aparte con
fracciones: se construyen los cuatro vértices, la pertenencia se prueba
con productos cruzados y la distancia es la menor a los cuatro lados
como segmentos. Cientos de conjuntos aleatorios, muchos con empates,
coincidieron.

## Soluciones optimizadas

`1111_geometry_optimized.java`. Conserva el orden racional exacto, restando antes el |P|² común a cada distancia cuadrada. Los numeradores reducidos son lineales en las coordenadas ilimitadas: usa proyecciones laterales y correcciones acotadas en vez de cuadrar BigInteger grandes por cuadrado. Un cuadrado degenerado es un punto; dentro, la distancia reducida es -|P|² y las coordenadas quedan acotadas. Las correcciones suman como máximo dos cuadrados de números inferiores a 8·10^8 y caben en long. Compara escalas exactamente y ordena índices primitivos por mezcla estable para respetar los ID empatados. Con L bits de consulta, la conversión decimal tiene cota conservadora O(L²); construcción y comparaciones con denominadores acotados cuestan O(nL log(n+1)), guardando O(nL) bits y O(n) índices. Bytes fijos sustituyen Scanner y el constructor de salida completa.

Frente a `1111_geometry.java`: tiempo 0.125 s → 0.109 s; memoria 3 916 KB → 664 KB.

C++, Go y Rust conservan fracciones exactas de distancias al cuadrado y ordenan por multiplicación cruzada, con el índice de entrada como desempate. Reutilizan los búferes de los productos de comparación. C++ y Rust también leen las coordenadas de consulta sin límite de longitud en grupos de nueve cifras, equivalentes a sus bloques en base 10⁹. Go representa enteros de precisión arbitraria con signo mediante bloques de 30 bits, lee las coordenadas directamente de bytes y ordena índices por mezcla. Reutiliza los búferes aritméticos y de comparación. Rust analiza tokens de bytes, guarda coordenadas e índices en vectores fijos y escribe el resultado con un único búfer fijo. Rust lee y escribe mediante la biblioteca de ejecución de C.

El envío aceptado en Go 1.14 x64 tarda 0.031 s frente a 0.015 s de la base y usa 800 KB frente a 1276 KB.

Las implementaciones base aceptadas [1111_geometry.java](1111_geometry.java), [1111_geometry.py](1111_geometry.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1111_geometry_optimized.java`: puesto de tiempo 6/23 y de memoria 1/23 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1111_geometry.cpp](1111_geometry.cpp) | G++ 13.2 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 428 KB | 11325584 |
| [1111_geometry.go](1111_geometry.go) | Go 1.14 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 1276 KB | 11325574 |
| [1111_geometry.java](1111_geometry.java) \* | Java 1.8 | geometry | O(n L² + n log n L) | AC | 0.125 s | 3916 KB | 11325557 |
| [1111_geometry.py](1111_geometry.py) \* | Python 3.12 x64 | geometry | O(n L² + n log n L) | AC | 0.078 s | 624 KB | 11298025 |
| [1111_geometry.rs](1111_geometry.rs) | Rust 1.75 x64 | geometry | O(n L² + n log n L) | AC | 0.031 s | 228 KB | 11325609 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1111_geometry_optimized.cpp](1111_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 208 KB | 11310910 |
| [1111_geometry_optimized.go](1111_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(n L² + n log n L) | AC | 0.031 s | 800 KB | 11311126 |
| [1111_geometry_optimized.rs](1111_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n L² + n log n L) | AC | 0.015 s | 80 KB | 11311247 |
| [1111_geometry_optimized.java](1111_geometry_optimized.java) \* | Java 1.8 | geometry | O(L²+n·L·log(n+1)) | AC | 0.109 s | 664 KB | 11325037 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
