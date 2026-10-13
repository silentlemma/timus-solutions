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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1439_binary_search.cpp](1439_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(M log D + D^2) | AC | 0.156 s | 424 KB |
| [1439_binary_search.go](1439_binary_search.go) | Go 1.14 x64 | binary_search | O(M log D + D^2) | AC | 0.171 s | 5708 KB |
| [1439_binary_search.java](1439_binary_search.java) | Java 1.8 | binary_search | O(M log D + D^2) | AC | 0.171 s | 10132 KB |
| [1439_binary_search.py](1439_binary_search.py) | Python 3.12 x64 | binary_search | O(M log D + D^2) | AC | 0.421 s | 21004 KB |
| [1439_binary_search.rs](1439_binary_search.rs) | Rust 1.75 x64 | binary_search | O(M log D + D^2) | AC | 0.031 s | 4664 KB |
