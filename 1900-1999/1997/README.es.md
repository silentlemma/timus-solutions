# 1997. Emparejar visitas evitando un intervalo de duraciones

[Timus 1997](https://acm.timus.ru/problem.aspx?space=1&num=1997) · dificultad 549 · matching

Problema original de Denis Dublennykh, preparado por Oleg Dolgorukov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un registro contiene todas las entradas y salidas de visitantes; el
local está vacío antes y después del registro. Cada visita debe durar
como máximo `b` unidades o como mínimo `a`. El intervalo abierto entre
ambos límites está prohibido. Determinar si todos los eventos admiten
esa explicación y, de ser así, dar cualquier asignación completa de
salidas a entradas.

Hay `2≤n≤1000` eventos, `1≤b,a≤10^9`, `b+1<a`. Los tiempos son distintos
y crecientes, entre 1 y `10^9`. La dirección 0 significa entrada y 1
salida. Tiempo 1 segundo y memoria 64 MB.

## Entrada

Primero `a b`, después `n`, y luego `n` líneas con tiempo y dirección.

## Salida

Escribir `Liar` si no existe una asignación completa. En otro caso
escribir `No reason` y una pareja de tiempos de entrada y salida por
visitante. Se acepta cualquier emparejamiento correcto en cualquier
orden.

## Evaluación

Un comprobador verifica que las parejas usan cada llegada y salida una
vez y que todas las duraciones están permitidas; `Liar` solo se acepta
si no existe asignación. Se acepta cualquier asignación válida en
cualquier orden.

## Ejemplos

```
6 3
4
1 0
2 0
5 1
10 1
```

```
No reason
1 10
2 5
```

```
6 3
4
1 0
2 0
6 1
10 1
```

```
Liar
```

En el primero las visitas `(1,10)` y `(2,5)` duran 9 y 3 unidades,
cumpliendo los límites largo y corto. En el segundo la salida a tiempo 6
produciría duración 5 o 4 con cualquiera de las entradas, ambas
prohibidas. Una salida posterior no puede reparar ese evento.

## Solución

Construimos un grafo bipartito: un vértice izquierdo por entrada y uno
derecho por salida. Una entrada `e` se conecta con una salida `x`
exactamente si `x>e` y se cumple `x−e≤b` o `x−e≥a`. La igualdad en ambos
límites está permitida. Cada arista representa una visita posible.

Una explicación válida equivale a un emparejamiento perfecto. La
explicación usa cada entrada y salida una vez y por tanto define dicho
emparejamiento. Recíprocamente, sus aristas producen visitas positivas
permitidas que utilizan todos los eventos. Si las cantidades de entradas
y salidas difieren, no hay solución.

### Caminos aumentantes por capas

Aplicamos Hopcroft–Karp. Guardamos la pareja de cada vértice,
inicialmente libre. BFS empieza en todos los vértices izquierdos libres,
recorre opciones derechas y vuelve por la pareja actual de un vértice
ocupado. Guarda distancias izquierdas y la longitud mínima hasta un
extremo derecho libre.

DFS sigue solo capas consecutivas y termina únicamente en un vértice
derecho libre a esa distancia mínima. Al regresar por un camino exitoso,
sustituye parejas en ambos lados y aumenta el tamaño en uno. Un cursor
por vértice izquierdo evita revisar otra vez opciones fallidas dentro de
la fase. Un vértice fallido se elimina de las capas actuales. Repetimos
fases BFS hasta que no exista camino aumentante.

Cambiar las aristas de un camino alternante conserva el emparejamiento y
aumenta su cardinalidad. Si al terminar existiera uno mayor, la
diferencia simétrica contendría un camino alternante con extremos
libres, contradiciendo el último BFS. El resultado es máximo; explica el
registro si su tamaño coincide con el número de entradas. Se imprimen
los tiempos de los eventos emparejados.

Una fase cuesta `O(E+V)`: BFS recorre el grafo y los cursores DFS
examinan cada arista como máximo una vez. Al agotar caminos mínimos
aumenta su longitud. Después de `O(sqrt V)` fases los caminos son
largos; al ser disjuntos en vértices, quedan como máximo `O(sqrt V)`
aumentos. Se obtiene la cota estándar `O(E sqrt V)`.

### Un criterio local no basta

Con `a=10,b=2`, entradas 1 y 10 y salidas 11 y 14 admiten
`(10,11),(1,14)`. Asignar primero la salida 11 a la entrada elegible más
antigua deja duración prohibida 4. El emparejamiento permite revisar
decisiones anteriores.

### Complejidad

Como máximo 500 vértices por lado y 250000 aristas. Construir el grafo
cuesta `O(n²)`; emparejar, `O(E sqrt V)`. Total `O(n² sqrt n)` tiempo y
`O(n²)` memoria en los cinco lenguajes. Cada llamada recursiva avanza
una capa izquierda, con profundidad máxima 500. Las diferencias caben en
32 bits con signo; Rust también usa tiempos de 64 bits.

La entrada da `a` antes de `b`; dirección 0 es entrada. Las duraciones
iguales a `b` y `a` son válidas; el intervalo abierto y las salidas
anteriores están prohibidos. Que cada vértice tenga una arista no basta:
varias entradas pueden necesitar la misma salida. Reiniciar cursores por
fase y actualizar ambas parejas al aumentar.

La versión didáctica en C++ construye el mismo grafo de duraciones y busca un camino aumentante por entrada. DFS toma una salida permitida si está libre o intenta reasignar su pareja actual a otra salida. Cada búsqueda visita cada salida como máximo una vez. Si no hay camino, las entradas procesadas ya no se pueden emparejar todas y el registro completo es imposible. Las parejas finales reconstruyen las visitas. Con V entradas y E aristas, tiempo O(V² + VE) y espacio O(V + E).

## Soluciones optimizadas

Go conserva Hopcroft–Karp sin listas de adyacencia densas. Entradas y salidas ya ordenadas; para entrada e, índices permitidos forman e<x≤e+b y x≥e+a. Tres punteros monótonos hallan todos los límites linealmente. BFS y cursores DFS recorren primer intervalo, saltan hueco prohibido y recorren segundo. Son exactamente las aristas explícitas: misma prueba de caminos aumentantes mínimos. Hasta500 visitantes permiten uint16 para índices e int16 para parejas y distancias con−1. Cola reutilizada, sin listas de registros/resultado ni fmt; sumas de umbrales≤2×10^9 caben en int32. V visitantes y E aristas implícitas: O(E sqrt V) para matching, O(n) preparación y O(V+n) espacio en lugar de O(E+V). Cantidades desiguales fallan y duraciones son positivas y permitidas. Se conservan grafos sencillos; otros cuatro lenguajes reutilizan bases admitidas.

Las implementaciones base aceptadas [1997_matching.cpp](1997_matching.cpp), [1997_matching.java](1997_matching.java), [1997_matching.py](1997_matching.py), [1997_matching.rs](1997_matching.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1997_matching.cpp](1997_matching.cpp) | G++ 13.2 x64 | matching | O(n^2 sqrt n) | AC | 0.015 s | 772 KB | 11292418 |
| [1997_matching.go](1997_matching.go) | Go 1.14 x64 | matching | O(n^2 sqrt n) | AC | 0.015 s | 4116 KB | 11292419 |
| [1997_matching.java](1997_matching.java) | Java 1.8 | matching | O(n^2 sqrt n) | AC | 0.109 s | 1116 KB | 11328331 |
| [1997_matching.py](1997_matching.py) \* | Python 3.12 x64 | matching | O(n^2 sqrt n) | AC | 0.109 s | 4532 KB | 11292420 |
| [1997_matching.rs](1997_matching.rs) \* | Rust 1.75 x64 | matching | O(n^2 sqrt n) | AC | 0.015 s | 1656 KB | 11292422 |
| [1997_dfs_matching.cpp](1997_dfs_matching.cpp) | G++ 13.2 x64 | dfs, matching | O(V² + VE) | AC | 0.015 s | 764 KB | 11315933 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1997_matching_optimized.go](1997_matching_optimized.go) \* | Go 1.14 x64 | matching | O(E sqrt V) | AC | 0.015 s | 928 KB | 11315782 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
