# 1741. Monstruo de la comunicación

[Timus 1741](https://acm.timus.ru/problem.aspx?space=1&num=1741) · dificultad 289 · dp

Problema original de Alex Samsonov (preparado por Marina Mukhacheva), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cliente con licencia de la versión 1 debe llegar a la versión n.
Cada actualización lleva la versión x a la versión y > x y tiene un
tamaño. Una actualización pirata vuelve pirata el cliente para
siempre; una crackeada se instala en cualquier cliente; una con
licencia solo se instala en un cliente que siga teniendo licencia.
Hallar el menor tamaño total de actualizaciones, o indicar que no se
puede llegar a la versión n.

## Entrada

n y m (2 ≤ n ≤ 10⁴, 1 ≤ m ≤ 10⁴) y luego m actualizaciones `x y d s`
(1 ≤ x < y ≤ n, 1 ≤ d ≤ 10⁶), donde s es `Pirated`, `Cracked` o
`Licensed`.

## Salida

`Online` y el menor tamaño total, o `Offline`.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
1 3 10 Licensed
1 2 2 Pirated
2 3 3 Licensed
2 3 6 Cracked
```

Salida:

```
Online
8
```

### Ejemplo 2

Entrada:

```
3 1
1 2 10 Licensed
```

Salida:

```
Offline
```

## Solución

Las actualizaciones solo suben la versión, así que las versiones se
pueden tratar en orden creciente, cada una después de todo lo que lleva
a ella. El estado es la versión junto con si el cliente sigue con
licencia o ya es pirata. Desde cada estado alcanzado, una actualización
pirata lleva al estado pirata de su destino, una crackeada conserva el
estado y una con licencia solo se permite desde el estado con licencia.
La respuesta es el menor de los dos valores de la versión n. `O(n + m)`.

En el primer ejemplo la pirata 1 → 2 de 2 y la crackeada 2 → 3 de 6
dan 8, más barato que la de licencia 1 → 3 de 10; la de licencia 2 → 3
de 3 no puede ir tras la pirata.

Trampas:

- el total puede llegar a unos 10¹⁰, más de lo que caben en 32 bits;
- una actualización crackeada deja con licencia a un cliente con
  licencia;
- no importa si la versión n termina con licencia.

Las respuestas coinciden con una implementación aceptada independiente,
una búsqueda de caminos más cortos, en 200 casos aleatorios.

## Soluciones optimizadas

Se mantiene la DP del DAG de versiones crecientes con estados de licencia limpia y pirateada. Arreglos planos reemplazan contenedores por vértice y objetos de arista. Una actualización pirata lleva el mínimo de ambos estados solo al pirata; una crackeada mantiene cada estado y una licenciada solo acepta el limpio. Se distingue el tipo una vez por actualización. Los costes usan 64 bits, con índices compactos. No se necesitan cola de prioridad ni Dijkstra.

- `1741_dp_optimized.cpp`: 0.015 s / 196 KB; base `1741_dp.cpp`: 0.031 s / 1068 KB; cambio respecto a la base: tiempo -51.6%, memoria -81.6%.
- `1741_dp_optimized.java`: 0.093 s / 748 KB; base `1741_dp.java`: 0.156 s / 5788 KB; cambio respecto a la base: tiempo -40.4%, memoria -87.1%.
- `1741_dp_optimized.py`: 0.109 s / 972 KB; base `1741_dp.py`: 0.109 s / 6872 KB; cambio respecto a la base: tiempo -0.0%, memoria -85.9%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1741_dp.cpp`; versión que cubre `1741_dp_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 56/56.

- Go: base didáctica preferida `1741_dp.go`; versión que cubre `1741_dp.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1741_dp.java`; versión que cubre `1741_dp_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1741_dp.py`; versión que cubre `1741_dp_optimized.py`; puestos tiempo/memoria 5/1, registros de otros autores 8/8.

- Rust: base didáctica preferida `1741_dp.rs`; versión que cubre `1741_dp.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1741_dp.cpp](1741_dp.cpp) | G++ 13.2 x64 | dp | O(n + m) | AC | 0.031 s | 1068 KB | 11308918 |
| [1741_dp.go](1741_dp.go) | Go 1.14 x64 | dp | O(n + m) | AC | 0.046 s | 3284 KB | 11289495 |
| [1741_dp.java](1741_dp.java) | Java 1.8 | dp | O(n + m) | AC | 0.156 s | 5788 KB | 11308919 |
| [1741_dp.py](1741_dp.py) | Python 3.12 x64 | dp | O(n + m) | AC | 0.109 s | 6872 KB | 11308920 |
| [1741_dp.rs](1741_dp.rs) | Rust 1.75 x64 | dp | O(n + m) | AC | 0.015 s | 2164 KB | 11289501 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1741_dp_optimized.cpp](1741_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N+M) | AC | 0.015 s | 196 KB | 11309342 |
| [1741_dp_optimized.java](1741_dp_optimized.java) | Java 1.8 | dp | O(N+M) | AC | 0.093 s | 748 KB | 11309343 |
| [1741_dp_optimized.py](1741_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N+M) | AC | 0.109 s | 972 KB | 11309341 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
