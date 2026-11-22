# 1439. Batalla con Quien-Tú-Sabes

[Timus 1439](https://acm.timus.ru/problem.aspx?space=1&num=1439) · dificultad 428 · binary_search

Problema original de Alexander Klepinin y Stanislav Vasiliev, del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las salas del Ministerio de Magia están numeradas 1, 2, …, N
(1 ≤ N ≤ 10⁹), y la numeración nunca tiene huecos: cuando se destruye
una sala, todas las de número mayor bajan un número. Hay M ≤ 10⁵ sucesos
en orden, cada uno «D x» (se destruye la sala que ahora tiene el número
x) o «L x» (Harry mira la puerta que ahora muestra el número x). Se
destruyen como mucho 10⁴ salas. Para cada suceso «L» hay que imprimir
el número que esa sala tenía al principio de todo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, y luego los M sucesos.

## Salida

Los números originales, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
20 7
L 5
D 5
L 4
L 5
D 5
L 4
L 5
```

Salida:

```
5
4
6
4
7
```

## Solución

Se guardan los números originales de las salas destruidas en un arreglo
ordenado g. La sala que ahora tiene el número x tiene el número original
x + k, donde k cuenta las salas destruidas por debajo de ella.
Recorriendo el arreglo hacia arriba, la sala g[j] queda por debajo justo
cuando g[j] ≤ x + j, es decir, g[j] − j ≤ x; y g[j] − j nunca decrece
porque los números de g son distintos, así que las salas de abajo forman
un prefijo y su longitud k sale de una búsqueda binaria.

Para «L» se imprime x + k. Para «D» el nuevo número original x + k
encaja justo en la posición k del arreglo: todo lo anterior es menor y
todo lo posterior mayor, así que insertarlo mantiene el orden.
`O(M log D + D²)` con D salas destruidas, donde cada inserción desplaza
como mucho 10⁴ números.

Detalles a tener en cuenta:

- el mismo número de puerta destruido una y otra vez oculta cada vez una
  sala nueva (pruebas 03, 07, gen3);
- los números llegan a mil millones, más de lo que permite un arreglo
  por sala (pruebas 05, gen1).

## Soluciones optimizadas

La revisión C++ conserva la búsqueda binaria en el vector ordenado de etiquetas destruidas y los desplazamientos al insertar. Búferes fijos de 16 KB sustituyen las llamadas formateadas. Se mantiene O(M log D + D²) de tiempo y O(D) de memoria; no es un árbol de estadísticas de orden.

Accepted del fuente exacto (G++ 13.2 x64, #11326643: 0.031 s / 188 KB); base didáctica `1439_binary_search.cpp`: 0.156 s / 424 KB. La medición optimizada anterior era 0.156 s / 216 KB. En la comparación guardada del 20 de noviembre de 2026, el puesto de tiempo es 1/80 y de memoria 1/80; por debajo de 1 MiB la regla evalúa solo el puesto de tiempo.

Estas versiones conservan el arreglo ordenado de habitaciones destruidas y la búsqueda binaria del prefijo; las inserciones siguen desplazando datos, así que el tiempo permanece O(M log D + D²). Mejoran el almacenamiento y la E/S. C++ usa etiquetas de 32 bits, suficientes para N ≤ 10⁹, y reserva las 10000 eliminaciones máximas. Go y Rust usan búferes acotados; Rust también usa 32 bits y entrada del C runtime. Python descarta cada línea tras procesarla y acumula bytes de salida en vez de todos los tokens de entrada y enteros de salida. Requiere O(D + bytes de salida); las otras versiones nuevas, O(D) más búferes fijos. Las versiones sencillas anteriores se conservan.

El envío aceptado en Python 3.12 x64 tarda 0.437 s frente a 0.421 s de la base y usa 2 376 KB frente a 21004 KB.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.031 s de la base y usa 96 KB frente a 4664 KB.

Las implementaciones base aceptadas [1439_binary_search.java](1439_binary_search.java) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1439_binary_search.cpp](1439_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D^2) | AC | 0.156 s | 424 KB | 11286248 |
| [1439_binary_search.go](1439_binary_search.go) | Go 1.14 x64 | binary_search | O(M log D + D^2) | AC | 0.171 s | 5708 KB | 11286251 |
| [1439_binary_search.java](1439_binary_search.java) \* | Java 1.8 | binary_search | O(M log D + D^2) | AC | 0.171 s | 10132 KB | 11286253 |
| [1439_binary_search.py](1439_binary_search.py) | Python 3.12 x64 | binary_search | O(M log D + D^2) | AC | 0.421 s | 21004 KB | 11286252 |
| [1439_binary_search.rs](1439_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log D + D^2) | AC | 0.031 s | 4664 KB | 11286256 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1439_binary_search_optimized.cpp](1439_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D²) | AC | 0.031 s | 188 KB | 11326643 |
| [1439_binary_search_optimized.go](1439_binary_search_optimized.go) \* | Go 1.14 x64 | binary_search | O(M log D + D²) | AC | 0.031 s | 404 KB | 11314850 |
| [1439_binary_search_optimized.py](1439_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O(M log D + D²) | AC | 0.437 s | 2376 KB | 11314854 |
| [1439_binary_search_optimized.rs](1439_binary_search_optimized.rs) \* | Rust 1.75 x64 | binary_search | O(M log D + D²) | AC | 0.046 s | 96 KB | 11314853 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
