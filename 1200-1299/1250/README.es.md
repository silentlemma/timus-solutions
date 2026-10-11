# 1250. Islas dentro del mar sagrado

[Timus 1250](https://acm.timus.ru/problem.aspx?space=1&num=1250) · dificultad 724 · graphs

Problema original de Stanislav Skorb (preparado por Ivan Dashkevich), del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa de W × H (W, H ≤ 500) muestra mar `.` y tierra `#`. Las casillas
de mar forman un mismo mar si se tocan por un lado o una esquina; las de
tierra forman una misma isla si se tocan solo por un lado. El mar que
contiene la casilla (X, Y), contada desde la esquina superior izquierda,
es sagrado, y toda la tierra dentro de él también lo es, incluidas las
islas de los mares que hay dentro de sus islas, y así sucesivamente. Hay
que contar las islas sagradas que no tocan el borde del mapa.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W, H, X e Y separados por uno o más espacios, y luego H líneas de W
caracteres.

## Salida

El número de esas islas.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 7 1 1
........#
.#######.
.#.....#.
.#.#.#.#.
.#.....#.
.#######.
#........
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
9 7 3 3
........#
.#######.
.#.....#.
.#.#.#.#.
.#.....#.
.#######.
#........
```

Salida:

```
2
```

## Solución

Se rodea el mapa con un anillo de casillas exteriores. Un mar unido por
esquinas no se puede atravesar con un camino que solo pasa por lados:
donde parece estrecho, dos de sus casillas se tocan por una esquina y
cierran el hueco. Así que la tierra dentro del mar sagrado es justo la
que no alcanza una inundación por lados desde el anillo exterior que
evita el mar sagrado.

El programa halla el mar sagrado con una inundación en las ocho
direcciones desde (X, Y), inunda desde el anillo exterior todas las
casillas que no están en él y cuenta las islas entre las casillas no
alcanzadas, con una inundación por lados por isla. Una isla que toca el
borde siempre se alcanza desde el anillo, así que nunca cuenta. Cada
inundación usa una pila explícita para evitar una recursión profunda en
mapas grandes. `O(W·H)`.

Detalles a tener en cuenta:

- las islas anidadas en lagos de islas sagradas también cuentan: en el
  primer ejemplo, el anillo y las dos islas de dentro (la prueba 06 tiene
  un lago);
- la tierra que solo se toca por una esquina forma islas distintas
  (prueba 08);
- la primera línea puede llevar varios espacios entre los números, así
  que el mapa se lee como los siguientes W·H caracteres `.` y `#`, haya lo
  que haya entre ellos.

Los recuentos se compararon con una segunda solución que construye el
árbol de mares e islas, en 1500 mapas pequeños aleatorios.

## Notas por lenguaje

- Python inunda con arreglos de bytes de casillas «aún libres», que la
  inundación va borrando.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1250_graphs.cpp](1250_graphs.cpp) | G++ 13.2 x64 | graphs | O(W·H) | AC | 0.015 s | 2428 KB |
| [1250_graphs.go](1250_graphs.go) | Go 1.14 x64 | graphs | O(W·H) | AC | 0.031 s | 7352 KB |
| [1250_graphs.java](1250_graphs.java) | Java 1.8 | graphs | O(W·H) | AC | 0.125 s | 3172 KB |
| [1250_graphs.py](1250_graphs.py) | Python 3.12 x64 | graphs | O(W·H) | AC | 0.468 s | 14428 KB |
| [1250_graphs.rs](1250_graphs.rs) | Rust 1.75 x64 | graphs | O(W·H) | AC | 0.015 s | 4108 KB |
