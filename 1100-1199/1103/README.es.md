# 1103. Una circunferencia por tres lápices que divide al resto por la mitad

[Timus 1103](https://acm.timus.ru/problem.aspx?space=1&num=1103) · dificultad 504 · geometry

Problema original de Katya Ovechkina, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` lápices en puntos enteros (`N` impar, `3 ≤ N ≤ 5000`, coordenadas
de valor absoluto como mucho `10^8`). No hay tres en una recta ni cuatro
en una circunferencia. Elige tres lápices de modo que la circunferencia
que pasa por ellos deje dentro exactamente `(N − 3) / 2` de los demás
lápices y el mismo número fuera. Si no existe tal circunferencia, imprime
`No solution`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `x y`.

## Salida

Las coordenadas de los tres lápices, un lápiz por línea.

## Evaluación

Se acepta cualquier circunferencia válida. El comprobador verifica que
los tres puntos son lápices distintos y cuenta los lápices de dentro y de
fuera con un determinante entero exacto.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
0 0
1 0
2 -1
2 1
1 1
0 2
-3 -1
```

Salida:

```
-3 -1
2 -1
1 1
```

## Solución

Siempre hay solución. Toma `A`, el lápiz más bajo (el de más a la
izquierda entre los más bajos), y `B`, su vecino en la envolvente
convexa, elegido de modo que todos los demás lápices queden a la
izquierda de la recta `AB`. Entonces toda circunferencia por `A` y `B`
corta ese semiplano de la misma forma: un lápiz `P` está dentro de la
circunferencia por `A`, `B` y `C` exactamente cuando ve el segmento `AB`
bajo un ángulo mayor que `C`. Todos los ángulos `APB` son menores de 180°
y, como no hay cuatro lápices en una circunferencia, todos distintos.
Ordena los otros `N − 2` lápices por ese ángulo y toma el del medio como
`C`: `(N − 3) / 2` lápices ven `AB` bajo un ángulo mayor y quedan dentro,
y otros tantos bajo uno menor y quedan fuera. `O(N log N)`.

Los ángulos se comparan sin coma flotante. La cotangente del ángulo es
`dot / cross`, donde `dot = (A − P)·(B − P)` y `cross` es el doble del área
orientada de `P`, `A`, `B`, positivo para todo `P`. A mayor ángulo,
menor cotangente, así que `P` va antes que `Q` cuando
`dot_P · cross_Q > dot_Q · cross_P`.

Detalles a tener en cuenta:

- las coordenadas llegan a `10^8`, así que `dot` y `cross` están acotados
  en valor absoluto por `8 · 10^16` y `4 · 10^16`, y sus productos por `3.2 · 10^33`, mucho más de 64 bits;
- comparar ángulos con `atan2` es arriesgado: dos lápices lejanos pueden
  ver `AB` bajo ángulos que difieren menos que el error de redondeo;
- `B` tiene que ser vecino de `A` en la envolvente; con un segundo punto
  cualquiera, los lápices a ambos lados de `AB` no se ordenan por un solo
  ángulo.

Las respuestas se comprobaron con un determinante exacto de punto en
circunferencia en todas las pruebas, incluidos conjuntos aleatorios de
miles de lápices en todo el rango de coordenadas.

## Soluciones optimizadas

Go conserva la arista AB de la envolvente convexa y ordena los demás puntos por ángulo creciente, así que la cotangente mayor va primero. Los productos cruzados son positivos. Se comparan primero los signos de los productos escalares y se trata el cero como no negativo. Si coinciden los signos, math/bits.Mul64 da las palabras alta y baja de las magnitudes exactas. Se compara primero la palabra alta y se invierte el orden si ambos signos son negativos. Las coordenadas y los productos comparten un arreglo. Cada partición usa la mediana de tres muestras. Si el intervalo se reduce geométricamente, el trabajo es O(N). Tras como máximo 2·bit_length(N−2) particiones se ordena el intervalo restante. El peor tiempo es O(N log N) y el espacio es O(N). Los otros cuatro lenguajes reutilizan sus versiones base admitidas.

Las implementaciones base aceptadas [1103_geometry.cpp](1103_geometry.cpp), [1103_geometry.java](1103_geometry.java), [1103_geometry.py](1103_geometry.py), [1103_geometry.rs](1103_geometry.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

C++/Rust usan productos nativos128 y selección; Go original y Java ordenan con enteros grandes. Go nuevo usa productos exactos de dos bloques128 y selección protegida; Python conserva enteros exactos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1103_geometry.cpp](1103_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 444 KB | 11279167 |
| [1103_geometry.go](1103_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2628 KB | 11279168 |
| [1103_geometry.java](1103_geometry.java) \* | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 7336 KB | 11279170 |
| [1103_geometry.py](1103_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 1548 KB | 11279169 |
| [1103_geometry.rs](1103_geometry.rs) \* | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1160 KB | 11279171 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1103_geometry_optimized.go](1103_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N log N) worst case | AC | 0.031 s | 960 KB | 11315430 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
