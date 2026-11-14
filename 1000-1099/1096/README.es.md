# 1096. El menor número de intercambios de placas de ruta de dos caras

[Timus 1096](https://acm.timus.ru/problem.aspx?space=1&num=1096) · dificultad 710 · bfs, graphs

Problema original de Stanislav Vasiliev, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de `K` autobuses (`1 ≤ K ≤ 1000`) hace la ruta `rᵢ` y lleva una
placa con `rᵢ` delante y otro número `bᵢ` detrás (números de 1 a 2000).
Un autobús nuevo debe hacer la ruta `T`, pero recibió una placa con `S1`
y `S2`. Un conductor acepta cambiar de placa con el conductor nuevo
cuando la placa de este muestra, por cualquier cara, la ruta de su
autobús. Halla el menor número de cambios tras los que el conductor
nuevo tiene una placa que muestra `T`, y los autobuses con los que
cambiar, o imprime `IMPOSSIBLE`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K`, luego `K` líneas con `rᵢ` y `bᵢ`, y al final `T`, `S1` y `S2`.

## Salida

El número de cambios `M` y `M` números de autobús en orden, o
`IMPOSSIBLE`.

## Evaluación

Se acepta cualquier secuencia más corta. El comprobador repite los
cambios y compara su número con el menor posible.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
8 5
5 4
7 4
1 5
4 1 8
```

Salida:

```
2
1
2
```

## Solución

Lo que importa es qué placa tiene el conductor nuevo: la primera o la de
algún autobús `j`. Con una placa que muestra `x` e `y`, se puede cambiar
con cualquier autobús de la ruta `x` o de la ruta `y` y obtener su placa.
Una búsqueda en anchura sobre estos estados halla el menor número de
cambios; cada autobús se alcanza una vez, así que los autobuses se
agrupan por ruta y cada grupo se gasta entero la primera vez que aparece
su ruta. La búsqueda se detiene en la primera placa que muestra `T`, y
los predecesores guardados dan los autobuses en orden. `O(K)` esperado
con tablas hash; `O(K log K)` en C++.

Por qué los cambios de placa no estropean esto: tras un cambio, el
autobús `j` tiene la placa que antes tenía el conductor nuevo. Cambiar
otra vez con `j` solo devolvería esa placa vieja, así que una secuencia
más corta nunca lo hace, y los demás autobuses no cambian.

Detalles a tener en cuenta:

- se imprimen los números de autobús, no los de ruta;
- la respuesta tiene al menos un cambio, porque `T` no está en ninguna
  cara de la primera placa;
- `S1` puede ser igual a `S2`, y muchos autobuses pueden compartir ruta.

El comprobador calcula el menor número de cambios capa a capa y repite
los cambios listados con las placas cambiando de manos.

## Notas por lenguaje

- Todos los lenguajes quitan del mapa el grupo de una ruta una vez usado
  (`pop`, `erase`, `delete`, `remove`), para que ningún autobús entre dos
  veces en la cola.

## Soluciones optimizadas

Se agrupan los autobuses por la ruta delantera en arreglos compactos. La búsqueda en anchura recorre las rutas y registra el autobús que alcanza primero cada una para reconstruir los intercambios.

El envío 11317785 en Python tardó 0.062 s y usó 960 KB. La versión sencilla tardó 0.078 s y usó 756 KB.

El envío 11317790 en Go tardó 0.031 s y usó 892 KB. La versión sencilla tardó 0.031 s y usó 1396 KB.

El envío 11317798 en Rust tardó 0.015 s y usó 256 KB. La versión sencilla tardó 0.062 s y usó 492 KB.

El envío 11317805 en Java tardó 0.109 s y usó 432 KB. La versión sencilla tardó 0.171 s y usó 5620 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321827 · Go 1.14 x64 №11322170 · Java 1.8 №11322171 · Python 3.12 x64 №11322172 · Rust 1.75 x64 №11322173.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1096_bfs.cpp](1096_bfs.cpp) | G++ 13.2 x64 | bfs | O(K log K) | AC | 0.015 s | 352 KB | 11321827 |
| [1096_bfs.go](1096_bfs.go) | Go 1.14 x64 | bfs | O(K) | AC | 0.031 s | 1396 KB | 11322170 |
| [1096_bfs.java](1096_bfs.java) | Java 1.8 | bfs | O(K) | AC | 0.171 s | 5620 KB | 11322171 |
| [1096_bfs.py](1096_bfs.py) | Python 3.12 x64 | bfs | O(K) | AC | 0.078 s | 756 KB | 11322172 |
| [1096_bfs.rs](1096_bfs.rs) | Rust 1.75 x64 | bfs | O(K) | AC | 0.062 s | 492 KB | 11322173 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1096_bfs_optimized.py](1096_bfs_optimized.py) | Python 3.12 x64 | bfs | O(K + R) | AC | 0.062 s | 960 KB | 11317785 |
| [1096_bfs_optimized.go](1096_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(K + R) | AC | 0.031 s | 892 KB | 11317790 |
| [1096_bfs_optimized.rs](1096_bfs_optimized.rs) | Rust 1.75 x64 | bfs | O(K + R) | AC | 0.015 s | 256 KB | 11317798 |
| [1096_bfs_optimized.java](1096_bfs_optimized.java) | Java 1.8 | bfs | O(K + R) | AC | 0.109 s | 432 KB | 11317805 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
