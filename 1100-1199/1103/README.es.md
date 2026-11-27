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

Compara ángulos sin flotantes. Para P, dot=(A-P)·(B-P) y
cross=cross(P,A,B)>0; su cociente es cot(ángulo APB). En (0,180 grados)
la cotangente decrece estrictamente. El orden es angular creciente y,
por tanto, cotangente decreciente: P precede Q exactamente si
dot_P*cross_Q > dot_Q*cross_P. Se conserva esa desigualdad correcta;
invertir todo el orden también deja la misma mediana.

C++ selecciona mediana con std::nth_element sin ordenar todos los
puntos. La tabla da cota conservadora O(N log N) peor caso para GCC 13.2
fijado: al agotar profundidad logarítmica de particiones usa selección
por montón. No se justifica O(N) peor caso incondicional. Todos guardan
O(N) puntos/claves, más entrada retenida y espacio de selección/ordenación
cuando corresponda.

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

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1103_geometry_optimized.java`. Conserva la arista soporte de la envolvente y el círculo del ángulo mediano. Guarda coordenadas, productos escalares/cruzados positivos e índices en arreglos primitivos. Sustituye productos BigInteger del comparador por comparación exacta con signo: primero signos y luego mitades alta/baja sin signo de productos64 por64; forma la mitad alta con bloques32. Coordenadas hasta10^8 mantienen valores bajo2^63, valores absolutos seguros y productos completos en128 bits. No usa ángulos flotantes ni epsilon. La mezcla iterativa de índices cuesta O(N log N) y O(N) espacio, con el mismo criterio mediano; las promesas de no colinealidad ni cocircularidad aseguran la partición.

Frente a `1103_geometry.java`: tiempo 0.140 s → 0.078 s; memoria 7336 KB → 688 KB.

Go optimizado mantiene arista soporte y ángulos crecientes. Con cruces
positivos compara signos de dot (cero no negativo) y magnitudes exactas
con palabras alta/baja de math/bits.Mul64, invirtiendo para dos productos
negativos. Puntos/claves comparten arreglo. La mediana determinista de
tres no garantiza reducción por factor fijo, necesaria para sumar
trabajo lineal de partición. El límite 2*bit_length(N-2) particiones
acota ese trabajo a O(N log N) peor caso; ordenar el resto también
cuesta como máximo O(N log N). Espacio O(N), sin suponer pivotes aleatorios
ni reducción geométrica.

La caché confirma base C++ solo por puesto temporal bajo 1 MiB y
Python por ambas métricas de referencia pequeña del compilador exacto.
Java/Rust simples no cumplen; Java optimizado separado sí por puesto
temporal, Rust optimizado bajo 1 MiB por referencia temporal. Go
optimizado aún falla tiempo y conserva marcador. Rigen los
[criterios compartidos](../../RATING_CRITERIA.md), conservando bases
sin copias idénticas ni meta separada de primer puesto.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1103_geometry_implementation_optimized.rs`. Se usa un único vector de puntos: los dos puntos elegidos de la envolvente pasan al inicio y se selecciona in situ la mediana angular del resto. Las comparaciones exactas i128 evitan copias de puntos y claves. Se leen tokens con un búfer nativo acotado; los cortos se guardan dentro del objeto y solo los largos reservan espacio extra. La conversión decimal conserva las cotas con signo sin guardar toda la entrada de comandos. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328975 (Rust 1.75 x64): **0.015 s / 236 KB**. Comparación archivada: `1103_geometry.rs` (Rust 1.75 x64) — 0.015 s / 1160 KB (#11279171).

La revisión actual de 1103_geometry_implementation_optimized.rs solo
nombra la capacidad intacta de token inline de 32 bytes. Se conservan algoritmo geométrico, base y comentarios sustantivos.

## Notas por lenguaje

C++/Rust didácticos comparan productos en 128 bits y seleccionan con
nth_element/select_nth_unstable_by. Go/Java didácticos ordenan con
productos de precisión arbitraria; Python también usa enteros exactos
sin límite. Go/Java optimizados separados comparan magnitudes exactas
de dos palabras. Son notas de las versiones nombradas, no de todas.

Las notas del 18 de noviembre de 2026 son una instantánea histórica.
Hoy se excluyen tiempos rivales bajo 0.015 s antes de elegir cohorte;
nuestros tiempos menores solo se elevan para comparar. Se conservan
pares Accepted originales y se usa la política común actual.

`1103_geometry_optimized.java`: puesto de tiempo 1/16 y de memoria 1/16 en esta muestra comparable.

La admisión actual usa los [criterios compartidos](../../RATING_CRITERIA.md):
puestos top diez/top 15% o referencia pequeña del compilador exacto
cuando corresponde; bajo 1 MiB solo tiempo. Mejorar 30% o una meta
aparte de primer puesto no da admisión. Se conservan bases significativas
sin asteriscos de objetivos de optimización.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1103_geometry.cpp](1103_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) worst case (GCC 13.2) | AC | 0.015 s | 444 KB | 11279167 |
| [1103_geometry.go](1103_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2628 KB | 11279168 |
| [1103_geometry.java](1103_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.14 s | 7336 KB | 11279170 |
| [1103_geometry.py](1103_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 1548 KB | 11279169 |
| [1103_geometry.rs](1103_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1160 KB | 11279171 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1103_geometry_optimized.go](1103_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N log N) worst case | AC | 0.015 s | 980 KB | 11328264 |
| [1103_geometry_optimized.java](1103_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.078 s | 688 KB | 11325008 |
| [1103_geometry_implementation_optimized.rs](1103_geometry_implementation_optimized.rs) | Rust 1.75 x64 | geometry, implementation | O(n) expected time; O(n) space | AC | 0.015 s | 224 KB | 11331130 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
