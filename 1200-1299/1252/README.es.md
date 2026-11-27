# 1252. Ordenar piedras con intercambios a distancia K

[Timus 1252](https://acm.timus.ru/problem.aspx?space=1&num=1252) · dificultad 397 · number_theory

Problema original de Alexey Lakhtin, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N piedras (1 ≤ N ≤ 130 000) de pesos distintos están en fila. Dos piedras se
pueden intercambiar si entre ellas hay exactamente K piedras más. Hay que
hallar el mayor K (0 ≤ K < N) con el que la fila se puede ordenar por
peso, en orden creciente o decreciente.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N pesos, uno por línea. Cada peso es un entero entre 1 y
130 000, ambos inclusive.

## Salida

El mayor K así.

## Evaluación

`tests/tests.json` usa `tokens` exactos: un K decimal en 0..N−1. Se ignoran blancos/saltos alrededor; tokens extra u otra escritura numeral fallan. Se permite orden creciente o decreciente; una fila ya ordenada permite N−1 aunque no existan intercambios a esa distancia.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
40
50
60
10
20
30
```

Salida:

```
2
```

## Solución

Un intercambio con K piedras en medio mueve las dos piedras d = K + 1
puestos, así que una piedra se queda en su clase de posiciones módulo d,
y dentro de una clase se puede obtener cualquier orden con intercambios
de vecinas de la clase. Por tanto se puede ordenar justo cuando d divide
la distancia de cada piedra desde su sitio actual hasta su sitio en la
fila ordenada.

Así que se halla, para el orden creciente y para el decreciente, el mcd g
de esas distancias. El mayor d que divide a g es el propio g, que es
menor que N, así que K = g − 1; si la fila ya está en ese orden, g = 0 y
sirve cualquier K, así que K = N − 1. La respuesta es el mayor de los
dos. `O(N log N)` por la ordenación.

Detalles a tener en cuenta:

- el orden decreciente también cuenta (prueba 04), y los dos órdenes
  pueden dar K distintos;
- una fila ya ordenada admite el mayor K, N − 1, aunque entonces no se
  pueda hacer ningún intercambio (pruebas 03 y gen4).

La regla se comparó con una búsqueda de todos los órdenes alcanzables
para cada K en 300 filas aleatorias de hasta 7 piedras.

C++/Go sencillos retienen pesos e índices originales ordenados; Java un long[N] empaquetado: O(N) arrays, incluido posible espacio de ordenación. Python añade entrada completa, enteros/slices e índices; Rust entrada y vectores numéricos/índices, O(I+N). Nativos rápidos guardan tabla completa de 130001 posiciones, O(W) para W=130000 independientemente del intervalo ocupado, sin segunda secuencia completa. Búferes: 16384 bytes C++, 4096 Java, stdin bloqueado acotado en Rust. GCD general hasta O(N log N), inicialización/barrido O(W), entrada O(I).

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

Los tres rápidos sustituyen ordenar por tabla cero peso→posición original gracias a pesos distintos y acotados. Guardan mínimo/máximo y barren ese intervalo saltando ceros; el rango da destinos crecientes/decrecientes. C++/Rust paran cuando ambos GCD llegan a 1: GCD 1 sigue 1 con nuevos valores, así que d>1 es imposible en ambos y K=0 final. Java recorre todo el intervalo. C++ usa fread propio, Java parser 4096 y Rust bytes bloqueados. Tiempo conservador O(I+W+N log N), espacio O(W+B) con búfer acotado B.

La caché exacta admite Go 4012 KB base por ambas métricas ante referencia exacta escasa, no por top 10/top 15% ordinario. Python 13612 KB pasa ambas clasificaciones ordinarias. Bases Java 1596 KB/Rust 3652 KB pasan ambas; rápidos Java 972 KB/C++ 604 KB/Rust 712 KB solo tiempo por debajo de 1024 KB. C++ sencillo queda docente pese a fallar métricas exigidas. Rigen [criterios compartidos](../../RATING_CRITERIA.md) sin primer puesto separado ni mejora 30%. Los comentarios C++/Rust revisados requieren Accepted exacto nuevo, sin atribuirles los bytes de envíos históricos.

Solo se añadieron comentarios de parada temprana a `1252_sorting.cpp` (histórico#11310440,0.015 s/604 KB) y `1252_sorting.rs` (histórico#11310439,0.015 s/712 KB). Se conservan bases y Java rápido sin cambios.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Java ordena los pesos empaquetados con sus posiciones en un solo
  arreglo `long`, en vez de ordenar índices en objetos con un
  comparador.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1252_number_theory.cpp](1252_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.093 s | 1212 KB | 11284003 |
| [1252_number_theory.go](1252_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.125 s | 4012 KB | 11284006 |
| [1252_number_theory.java](1252_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.093 s | 1596 KB | 11284010 |
| [1252_number_theory.py](1252_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.14 s | 13612 KB | 11284007 |
| [1252_number_theory.rs](1252_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.031 s | 3652 KB | 11284011 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1252_sorting.cpp](1252_sorting.cpp) | G++ 13.2 x64 | sorting | O(W + N log N) | AC | 0.015 s | 608 KB | 11331145 |
| [1252_sorting.java](1252_sorting.java) | Java 1.8 | sorting | O(W + N log N) | AC | 0.078 s | 972 KB | 11310354 |
| [1252_sorting.rs](1252_sorting.rs) | Rust 1.75 x64 | sorting | O(W + N log N) | AC | 0.015 s | 712 KB | 11331120 |
