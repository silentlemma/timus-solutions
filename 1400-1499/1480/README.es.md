# 1480. Cupones

[Timus 1480](https://acm.timus.ru/problem.aspx?space=1&num=1480) · dificultad 471 · constructive

Problema original de Sergey Pupyrev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que colocar los números 1 … N² (2 ≤ N ≤ 50) en una tabla N × N de
modo que la mayor suma de dos casillas con un lado común sea lo más
pequeña posible. Se escribe esa suma y una tabla que la alcanza;
escritos en orden fila a fila, la suma sería 2N² − 1.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

La menor mayor suma posible y luego las N filas de la tabla. Se acepta
cualquier tabla válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
6
1 4
3 2
```

## Actualización de envíos aceptados

Archivos actualizados: [1480_parsing_implementation_optimized.rs](1480_parsing_implementation_optimized.rs). Las tablas de soluciones muestran los nuevos Accepted correspondientes exactamente al código fuente de estos archivos. Las mediciones y posiciones comparativas anteriores pertenecen a versiones previas y se conservan como datos históricos. La auditoría en caché confirma implementaciones que cumplen los criterios en todos los lenguajes disponibles. Se conservan las versiones didácticas por su claridad; si un mismo archivo cubre también la versión rápida, debe cumplir el criterio de rendimiento.

## Solución

Sea V=N² y t=⌊N/2⌋. Colorea la tabla como un ajedrez. En orden de
lectura coloca V,V−1,… en el color par y1,2,… en el impar. Los dos
contadores reparten1…V sin repetir; toda arista une colores distintos.
Para N impar, los índices dan sumas horizontales V o V+1, y la suma
de un número grande con el pequeño debajo es V+(N+1)/2. Para N=2t,
las horizontales no superan V+2 y la máxima vertical es V+t+1.
Las casillas (fila0,columna0) y (fila1,columna0) alcanzan V+t+1.
El máximo de esta construcción es exactamente ese valor. El tiempo
Θ(N²) es necesario para escribir la respuesta; los dos contadores
usan O(1) espacio de trabajo aparte del búfer de salida de cada lenguaje.

### Por qué no se puede mejorar

Usamos este hecho de la cuadrícula: si A pertenece a un solo color
y |A|≤t², su vecindad abierta cumple

|N(A)|−|A| ≥ ⌈√|A|⌉.

La prueba que tiene en cuenta los bordes aparece abajo. Supón que todas
las sumas fueran como máximo V+t. Las t² etiquetas mayores forman un
conjunto independiente S: dos de ellas ya sumarían más de V+t. Sus
vecinos solo pueden llevar etiquetas hasta t²+t−1; hay como máximo
t²+t−1 vecinos. Divide S por color en A0,A1. Sus vecindades tienen
colores distintos y no se solapan. El hecho anterior implica
|N(S)|−|S|≥√|A0|+√|A1|≥√|S|=t, contradicción. Por tanto V+t+1
es una cota inferior y la construcción es óptima.

### Prueba del hecho de la cuadrícula

Para un conjunto finito no vacío X de un color en la retícula infinita,
[la desigualdad isoperimétrica bipartita](https://arxiv.org/html/1710.10232#S4.SS3)
da |N(X)|−|X|≥⌈2√|X|⌉+1 (ejemplo4.7, ecuación4.22).
No se aplica directamente al borde finito: las siguientes reflexiones
y caminos transversales contabilizan los vecinos que faltan.

Primero supón que A no toca un borde horizontal ni uno vertical.
Refleja la tabla para que sean el inferior y el derecho. Escribe
s=|A|, d=|N(A)|−s. Sean a,b los puntos de A,N(A) en los ejes superior
e izquierdo, contando dos veces su esquina; α,β indican su pertenencia
a cada conjunto. Refleja en ambos ejes e identifica repeticiones:
|X|=4s−2a+α y D=|N(X)|−|X|=4d+2(a−b)+β−α.
Desplazar A abajo o a la derecha lo inyecta en N(A) evitando el eje
correspondiente, así que cada cuenta de eje es como máximo d.
La desigualdad infinita implica d≥1. Si α=1, entonces β=0, b≥a y
a≤2d; de ahí 4s−2a+1≤(2d−1)² y s≤d². Si α=0 y A toca p de los
dos ejes, b≥a+p, a≤pd, β≤1 y β=0 cuando p=0. Al sustituir se obtiene
s≤(d−1/4)², s≤d²−d/2+1/4 o s≤d²−d+1 para p=0,1,2.
Todas son como máximo d². Une puntos de A que comparten vecino;
las componentes distintas tienen vecindades disjuntas. Si todas cumplen
esta condición, sumar sᵢ≤dᵢ² también da s≤d².

Ahora B=N(A), C es el color opuesto menos B. Las regiones R=A∪B y
Q=C∪N(C) son disjuntas. Si ambas tienen caminos entre el mismo par
de bordes opuestos, d≥t. Transpón para cruzar de izquierda a derecha.
Los caminos simples disjuntos tienen un orden vertical; refleja para
que R quede arriba de Q. Cada columna contiene un punto R sobre uno Q.
En una columna alternante, cada tramo de posiciones A tiene un vecino
vertical adicional, salvo que un extremo de color A elimina uno.
Con N par, toda columna aporta exceso no negativo; en las t columnas
con extremo A abajo, exceso cero haría de R un sufijo inferior,
contradiciendo el orden de los caminos, por lo que aportan al menos1.
Con N impar, las t o t+1 columnas con extremos del otro color aportan
al menos1; en las restantes Q impide alcanzar ambos extremos y el
exceso es no negativo. Los vecinos horizontales solo aumentan B.
Sumar prueba d≥t.

Finalmente, sea |A|≤t² y una componente que cruza bordes opuestos,
pero d<t. C no es vacío y d_C≤d+ε, donde ε es la diferencia entre
los tamaños de los colores: 0 para N par y ±1 para N impar. Una
componente C no puede cruzar perpendicularmente al camino A por
separación planar. Un cruce paralelo daría d≥t. De otro modo, todas
las componentes C cumplen la cota por reflexión y se obtiene
1≤d_C y |C|≤(d+ε)². Pero para N=2t,
|C|≥t²−t+1>(t−1)²; para N=2t+1 con A del color mayoritario,
|C|≥t²+t+1>t²; con A minoritario,
|C|≥t²+t+2>(t−2)². Si t−2<1, el último caso ya contradice
1≤d_C≤t−2. Por tanto un conjunto transversal tiene d≥t y
s≤t²≤d². El hecho queda probado para todo N; las comprobaciones
finitas no sustituyen esta demostración.

## Soluciones optimizadas

C++ y Go emiten la misma construcción ajedrezada con dos contadores, pequeño creciente y grande decreciente. Un bloque de 8192 bytes sustituye el formato individual de cada entero. Go lee y escribe mediante los descriptores estándar y convierte los dígitos en un arreglo de cuatro bytes. Tiempo Θ(N²), exigido por la salida, y espacio adicional O(1). Se conservan originales; Java, Python y Rust reutilizan los admitidos. La optimalidad general se demuestra arriba mediante reflexiones con bordes y caminos transversales; la enumeración de cuadrículas pequeñas es una regresión independiente.

Las implementaciones base aceptadas [1480_constructive.java](1480_constructive.java), [1480_constructive.py](1480_constructive.py), [1480_constructive.rs](1480_constructive.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1480_parsing_implementation_optimized.rs`. Se conserva la construcción del tablero y cada número se escribe en un búfer acotado persistente, sin cadenas por celda ni respuesta completa.

Accepted #11329180 (Rust 1.75 x64): **0.015 s / 84 KB**. Comparación archivada: `1480_constructive.rs` (Rust 1.75 x64) — 0.031 s / 256 KB (#11286708).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1480_constructive.cpp](1480_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 128 KB | 11286681 |
| [1480_constructive.go](1480_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.031 s | 1108 KB | 11286689 |
| [1480_constructive.java](1480_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.125 s | 1640 KB | 11286700 |
| [1480_constructive.py](1480_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.078 s | 432 KB | 11286697 |
| [1480_constructive.rs](1480_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 256 KB | 11286708 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1480_constructive_optimized.cpp](1480_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N²) | AC | 0.015 s | 100 KB | 11315374 |
| [1480_constructive_optimized.go](1480_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N²) | AC | 0.015 s | 276 KB | 11315828 |
| [1480_parsing_implementation_optimized.rs](1480_parsing_implementation_optimized.rs) | Rust 1.75 x64 | parsing, implementation | O(n^2) time; O(1) state + bounded I/O buffers | AC | 0.031 s | 72 KB | 11330233 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
