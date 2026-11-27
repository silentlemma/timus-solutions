# 1298. Visitar todas las casillas con saltos de caballo

[Timus 1298](https://acm.timus.ru/problem.aspx?space=1&num=1298) · dificultad 234 · backtracking

Problema original del folclore (preparado por Den Raskovalov), de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un tablero N × N (1 ≤ N ≤ 8) hay que encontrar un recorrido del
caballo: un camino de saltos de caballo que pasa por cada casilla
exactamente una vez. Se imprimen las casillas en orden, con una letra
para la columna y un número para la fila, o `IMPOSSIBLE` si no hay
recorrido.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

N² casillas, una por línea, o `IMPOSSIBLE`.

## Evaluación

Se valida el testigo, no el texto de un recorrido concreto: exactamente
N² casillas distintas dentro del tablero, una por línea, y cada
desplazamiento consecutivo es un salto de caballo. Ocho fuentes se
ejecutan para todo N=1..8: 64 salidas reales y códigos verificados. Para IMPOSSIBLE, una búsqueda independiente simple enumera todos
los inicios y caminos de N=2,3,4 sin simetría, orden por grado ni
poda de aislados. Se comprueban directamente el caso único y
recorridos N=5..8.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
IMPOSSIBLE
```

### Ejemplo 2

Entrada:

```
6
```

Salida:

```
a1
b3
a5
c6
e5
f3
e1
c2
a3
b1
d2
f1
e3
f5
d4
e6
f4
e2
c1
a2
b4
a6
c5
d3
f2
d1
b2
c4
d6
b5
c3
e4
f6
d5
b6
a4
```

## Actualización de envíos aceptados

Archivos actualizados: [1298_backtracking_parsing_optimized.go](1298_backtracking_parsing_optimized.go). Las tablas de soluciones muestran los nuevos Accepted correspondientes exactamente al código fuente de estos archivos. Las mediciones y posiciones comparativas anteriores pertenecen a versiones previas y se conservan como datos históricos. La auditoría en caché confirma implementaciones que cumplen los criterios en todos los lenguajes disponibles. Se conservan las versiones didácticas por su claridad; si un mismo archivo cubre también la versión rápida, debe cumplir el criterio de rendimiento.

## Solución

Cada casilla es un vértice y cada salto de caballo una arista; sea
`V=N²`. Las versiones sencillas hacen búsqueda en profundidad con retroceso
desde cada inicio. Marcan y añaden la casilla actual, prueban todos los
vecinos libres y deshacen marca y paso si falla la rama. Una ruta de V
vértices es un recorrido. Solo si fallan todas las ramas desde todos los
inicios se declara imposible: la completitud no depende del orden.

La regla de Warnsdorff prueba primero vecinos con menos continuaciones
libres. Solo ordena, sin omitir ramas. Suele hallar testigos pronto,
pero no garantiza tiempo polinómico. Una cota peor gruesa es
`O(V·8^V)` tiempo y `O(V)` espacio: grado máximo ocho y profundidad V.
El dominio permitido es pequeño (`V≤64`) y se verifica entero abajo.

N=1 tiene el recorrido a1. La búsqueda exhaustiva ordinaria demuestra
la imposibilidad para N=2,3,4. Para N=5,6,7,8 la salida real proporciona
un recorrido completo. No tiene que ser cerrado ni empezar en una casilla
concreta. El comportamiento observado de la heurística no prueba una cota.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1298_backtracking_optimized.java`. Conserva retroceso completo ordenado por Warnsdorff y representantes de simetría. Actualiza grados al retirar el vértice actual; máscara de aislados permite la misma poda en tiempo constante. Cada rama fallida restaura los grados modificados y la máscara guardada. Conserva orden estable y excepción del último vértice, sin límite de búsqueda. Cota gruesa O(V²·8^V), O(V) palabras acotadas con V=N²≤64; sin recorridos precalculados.

Java 1.8 exacto #11327756 mide `0.078 s / 376 KB`, con puestos
guardados del 20 de noviembre de 2026: tiempo 1/26, memoria 2/26.
Bajo 1024 KB solo se exige tiempo, así que cumple. La fila actual
no tiene asterisco ni existe una meta separada de primero en ambas.
El anterior #11308542 (`0.125 s / 396 KB`) es un par histórico
distinto; se conservan las bases didácticas.

- `1298_backtracking_optimized.java`: 0.078 s / 376 KB; base didáctica conservada `1298_backtracking.java`: 0.156 s / 7116 KB.

Los dos `_optimized` conservan el mismo retroceso completo ordenado
por Warnsdorff, con máscaras para vecinos y casillas no visitadas.
Numeran `(columna,fila)` como `columna*N+fila`. Los candidatos son
`adjacency[v] & remaining`; el grado siguiente es la cuenta de bits de
`adjacency[w] & remaining`. Solo hay que ordenar hasta ocho movimientos.

Dos reducciones correctas acortan la búsqueda. Reflexiones en ambos ejes
y transposición conservan los saltos. Se refleja el inicio a sus distancias
a los bordes más cercanos y se transpone para columna≤fila. Cada órbita
tiene representante en `0≤columna≤fila<ceil(N/2)`: basta probarlos.
Además, si quedan más de un vértice y hay uno aislado en el subgrafo
inducido restante, ninguna continuación puede unirlo con otro vértice
restante y cubrirlos todos. Se exceptúa el caso de un solo vértice.

Descripción y mediciones históricas de la revisión anterior: Python usa máscaras enteras y `bit_count`, sin generar repetidamente
tuplas de coordenadas ni listas de vecinos libres. Java usa long y arrays
primitivos de candidatos/grados por profundidad, sin ArrayList, arrays
de coordenadas por movimiento, comparadores ni Scanner. Para N=8 hacen
falta los 64 bits: Java usa explícitamente `-1L` como máscara completa,
pues desplazar un long 64 posiciones equivale a desplazar cero. El bit 63
con signo no invalida la cuenta ni la extracción del bit inferior.

Estas reducciones conservan completitud, sin garantía polinómica. Una
cota gruesa con todos los escaneos de vértices aislados es `O(V²·8^V)`.
Con V≤64, máscaras y espacios por profundidad ocupan `O(V)` palabras u
objetos de tamaño acotado y profundidad V; para tableros mayores habría
que contar el tamaño variable de los enteros. No se guardan recorridos
ni respuestas precalculadas en las fuentes.

Descripción y mediciones históricas de la revisión anterior: Accepted de los bytes exactos: Python 0,062 frente a 0,171 s, 63,7% más
rápido, pero 636 frente a 544 KB, 16,9% más memoria. Java 396 frente a
7116 KB, 94,4% menos memoria; 0,125 frente a 0,156 s, 19,9% menos tiempo.
Cada uno cumple por una métrica; las cinco fuentes sencillas se conservan.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1298_backtracking_parsing_optimized.go`. Se rechazan los tableros2x2,3x3y4x4antes del retroceso. Una DP independiente de subconjuntos y extremos prueba que no tienen camino hamiltoniano de caballo; se conservan búsqueda exacta y empates para los demás tamaños. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios.

El Go histórico #11329146 fue `0.015 s / 804 KB`. El fuente exacto
seleccionado #11330229 mide `0.015 s / 780 KB`, como en la tabla;
base #11284709 sigue con `0.015 s / 4468 KB`.

## Notas por lenguaje

Rigen los [criterios compartidos](../../RATING_CRITERIA.md): diez primeros o
15% superior para métricas necesarias, sustituidos por referencia
con 1–10 rivales válidos del mismo compilador. Bajo 1024 KB solo
se exige tiempo. Se excluyen rivales menores de `0.015 s`; solo
nuestro tiempo comparado se eleva a ese mínimo. Empates comparten
puesto y corte porcentual redondea arriba. No hay primer puesto
separado, corte ID/fecha ni admisión solo por mejorar30%. Ninguna
fila actual tiene asterisco.

La auditoría congelada ligada a fuentes admite C++ sencillo por
ranking ordinario temporal y Java rápido con tiempo1/26. CPython
rápido #11308531 (`0.062 s / 636 KB`) cumple el límite `0.093 s`
de nueve rivales. Go tiene dos rivales: seleccionado #11330229
(`0.015 s / 780 KB`) cumple `0.062 s`; Go base4468KB supera su
límite de memoria1127.00KB. Rust tiene un rival y cumple `0.031 s`.
La afirmación anterior sin rivales Go/Rust queda obsoleta. Java y
Python sencillos se conservan para enseñanza aunque no cumplan
sus comparaciones. Algoritmos, comentarios y celdas Accepted se preservan.

Las búsquedas sencillas por coordenadas siguen completas; máscaras
pueden imprimir otro recorrido válido. La tabla selecciona CPython
3.12 para Python rápido, sin copias artificiales idénticas.

El lint estricto exige nombres para movimientos Go8, límite imposible4
y capacidad decimal24. El archivo actual solo extrae esas constantes;
sustituir sus valores recupera exactamente los bytes Accepted previos. #11330229 y sus medidas describen esa versión.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1298_backtracking.cpp](1298_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(V·8^V) | AC | 0.015 s | 216 KB | 11284706 |
| [1298_backtracking.go](1298_backtracking.go) | Go 1.14 x64 | backtracking | O(V·8^V) | AC | 0.015 s | 4468 KB | 11284709 |
| [1298_backtracking.java](1298_backtracking.java) | Java 1.8 | backtracking | O(V·8^V) | AC | 0.156 s | 7116 KB | 11284720 |
| [1298_backtracking.py](1298_backtracking.py) | Python 3.12 x64 | backtracking | O(V·8^V) | AC | 0.171 s | 544 KB | 11284718 |
| [1298_backtracking.rs](1298_backtracking.rs) | Rust 1.75 x64 | backtracking | O(V·8^V) | AC | 0.015 s | 244 KB | 11284723 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1298_backtracking_optimized.py](1298_backtracking_optimized.py) | Python 3.12 x64 | backtracking | O(V²·8^V) | AC | 0.062 s | 636 KB | 11308531 |
| [1298_backtracking_optimized.java](1298_backtracking_optimized.java) | Java 1.8 | backtracking | O(V²·8^V) time; O(V) bounded words | AC | 0.078 s | 376 KB | 11327756 |
| [1298_backtracking_parsing_optimized.go](1298_backtracking_parsing_optimized.go) | Go 1.14 x64 | backtracking, parsing | O(V·8^V) | AC | 0.015 s | 804 KB | 11331017 |
