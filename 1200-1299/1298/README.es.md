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

Se valida el testigo: exactamente N² casillas distintas dentro del
tablero y cada transición un salto de caballo. Diferentes recorridos
correctos son válidos; no se comparan sus textos ni se presupone el mismo
desempate. Ambos programas nuevos pasaron ocho entradas del repositorio
en Java 8 y CPython 3.12, cubriendo todos los valores permitidos N=1..8.
Se volvieron a leer y validar independientemente las 16 salidas y códigos
de salida. Para `IMPOSSIBLE`, otra búsqueda ordinaria enumeró todos los
inicios y rutas para N≤4, con 30102 llamadas recursivas, sin simetrías,
orden por grado ni poda de aislados. Ambos tienen Accepted de sus bytes exactos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
IMPOSSIBLE
```

### Ejemplo 2

Entrada:

```
5
```

Salida:

```
a1
c2
e1
d3
e5
c4
d2
e4
c5
a4
b2
d1
e3
d5
b4
a2
c1
e2
c3
b1
a3
b5
d4
b3
a5
```

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

## Soluciones optimizadas

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

Python usa máscaras enteras y `bit_count`, sin generar repetidamente
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

Accepted de los bytes exactos: Python 0,062 frente a 0,171 s, 63,7% más
rápido, pero 636 frente a 544 KB, 16,9% más memoria. Java 396 frente a
7116 KB, 94,4% menos memoria; 0,125 frente a 0,156 s, 19,9% menos tiempo.
Cada uno cumple por una métrica; las cinco fuentes sencillas se conservan.

## Notas por lenguaje

Las cinco versiones anteriores conservan la búsqueda clara por coordenadas
y sus recorridos aceptados. Las dos de máscaras pueden imprimir otro orden
válido. La tabla indica el runtime real: el nuevo Python fue aceptado en
CPython 3.12, no PyPy.

Ambas versiones nuevas están admitidas, pero aún no son primeras en alguna
métrica: ambas filas llevan asterisco. La base C++ ya cumple el 15% superior
o primeros diez puestos en ambas métricas. Go y Rust no tienen envíos de
otros autores elegibles en la muestra filtrada: es cobertura formal, no
superioridad demostrada. Cada comparación usa su propia base sencilla del
mismo lenguaje, sin copias optimizadas artificiales.

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
| [1298_backtracking_optimized.py](1298_backtracking_optimized.py) \* | Python 3.12 x64 | backtracking | O(V²·8^V) | AC | 0.062 s | 636 KB | 11308531 |
| [1298_backtracking_optimized.java](1298_backtracking_optimized.java) \* | Java 1.8 | backtracking | O(V²·8^V) | AC | 0.125 s | 396 KB | 11308542 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
