# 1643. Ataque a la Fortaleza Oscura

[Timus 1643](https://acm.timus.ru/problem.aspx?space=1&num=1643) · dificultad 425 · bfs

Problema original de Denis Dublennykh, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos ejércitos están en un mapa de n × m con distritos transitables e
intransitables. En un día un ejército pasa a cualquiera de los 8
distritos vecinos transitables; un distrito con una letra de teletransporte
puede enviarlo al instante a cualquier distrito con la misma letra. Cuando ambos
ejércitos están en un mismo distrito se unen y avanzan juntos. Antes de
eso, ninguno puede entrar en la fortaleza. Hay que hallar el menor número
de días hasta que el ejército unido llegue a la fortaleza.

## Entrada

n y m (1 ≤ n, m ≤ 100) y luego el mapa: `#` intransitable, `.`
transitable, `A`–`Z` teletransportes, `$` y `!` los ejércitos, `*` la
fortaleza, cada uno de los tres últimos exactamente una vez.

## Salida

El menor número de días o `Impossible`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 8
....AA.#
.######!
.....*##
.#######
..B$...B
```

Salida:

```
11
```

### Ejemplo 2

Entrada:

```
3 5
##*..
!#...
##..$
```

Salida:

```
Impossible
```

## Solución

Un ejército que llega antes puede esperar, así que reunirse en el
distrito c cuesta max(d₁(c), d₂(c)) días, donde d₁ y d₂ son las
distancias de los dos ejércitos con la fortaleza cerrada. Después el
ejército unido necesita d(c) días más hasta la fortaleza, y como todo
movimiento es reversible (un paso vale en ambos sentidos y un
teletransporte une su letra en las dos direcciones), d es la distancia
desde la propia fortaleza. La respuesta es el mínimo de
max(d₁, d₂) + d sobre todos los distritos salvo la fortaleza.

Cada distancia es una búsqueda en anchura en la que los teletransportes
cuestan 0: un 0-1 BFS, donde los movimientos gratuitos van primero: una
pila en Go, el frente de la cola doble en los demás. El primer distrito
procesado de una letra ya tiene la menor distancia entre los de esa letra,
así que cada letra se propaga una sola vez. `O(n · m)` por búsqueda, tres en total.

Detalles a tener en cuenta:

- un ejército no puede atravesar la fortaleza antes de la reunión
  (prueba 06), pero el ejército unido sí puede salir justo a su lado;
- el grupo de una letra debe propagarse una sola vez, o un mapa lleno de
  la misma letra cuesta tiempo cuadrático;
- el ejército unido también puede usar teletransportes (prueba 07).

Las respuestas coinciden con una implementación aceptada independiente
en 180 mapas aleatorios.

## Soluciones optimizadas

C++ y Go guardan cuadrícula y tres distancias en arreglos planos de 16 bits. Hasta 10000 celdas implican distancias menores que 10000; 65535 señala inalcanzable. Al descubrir una letra el día d, asignan d y encolan inmediatamente todas sus celdas. Así contraen su componente gratuito antes de continuar BFS; las aristas restantes cuestan un día. Cada celda se descubre una vez y bastan n·m entradas de cola. Un arreglo enlazado guarda los grupos sin objetos por celda. Dos búsquedas cierran la fortaleza; la tercera parte de ella abierta. Se minimiza max(d₁,d₂)+d₃ en encuentros alcanzables fuera de la fortaleza: la primera tropa espera y la reversibilidad da la ruta posterior. Tiempo y espacio O(n·m). Se conservan todas las bases; Java, Python y Rust reutilizan las admitidas para la cobertura rápida.

Las implementaciones base aceptadas [1643_bfs.java](1643_bfs.java), [1643_bfs.py](1643_bfs.py), [1643_bfs.rs](1643_bfs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1643_bfs.cpp](1643_bfs.cpp) | G++ 13.2 x64 | bfs | O(n · m) | AC | 0.015 s | 1088 KB | 11288481 |
| [1643_bfs.go](1643_bfs.go) | Go 1.14 x64 | bfs | O(n · m) | AC | 0.031 s | 4792 KB | 11288482 |
| [1643_bfs.java](1643_bfs.java) | Java 1.8 | bfs | O(n · m) | AC | 0.109 s | 2224 KB | 11288484 |
| [1643_bfs.py](1643_bfs.py) | Python 3.12 x64 | bfs | O(n · m) | AC | 0.125 s | 2176 KB | 11288483 |
| [1643_bfs.rs](1643_bfs.rs) | Rust 1.75 x64 | bfs | O(n · m) | AC | 0.031 s | 1140 KB | 11288485 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1643_bfs_optimized.cpp](1643_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(n·m) | AC | 0.015 s | 220 KB | 11314974 |
| [1643_bfs_optimized.go](1643_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(n·m) | AC | 0.015 s | 388 KB | 11314986 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
