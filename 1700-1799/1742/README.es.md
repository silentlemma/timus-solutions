# 1742. Formación de equipos

[Timus 1742](https://acm.timus.ru/problem.aspx?space=1&num=1742) · dificultad 312 · graphs

Problema original de Artyom Ripatti, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n programadores nombra al colega que considera el más
fuerte, quizá a sí mismo. Los grupos se forman de uno en uno: se elige
cualquier programador sin grupo y se va añadiendo al colega nombrado por
el último añadido mientras ese colega esté libre. Hallar el menor y el
mayor número de grupos que puede salir.

## Entrada

n (1 ≤ n ≤ 10⁵) y luego el número nombrado por cada programador.

## Salida

El menor y el mayor número de grupos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2
3
4
2
```

Salida:

```
1 2
```

## Solución

Los nombres forman un grafo donde de cada programador sale una flecha:
árboles que desembocan en ciclos. Un grupo es un recorrido por las
flechas.

- Menor: un programador al que nadie nombra solo puede estar en un
  grupo que empiece por él, y lo mismo un ciclo al que nadie de fuera
  apunta; empezando por ellos, cada recorrido sigue hasta topar con un
  grupo, así que cada uno da exactamente un grupo y no hace falta nada
  más.
- Mayor: un recorrido que entra en un ciclo lo da entero, así que cada
  ciclo es a lo sumo un grupo. Tomando primero los ciclos y luego a los
  demás desde los ciclos hacia fuera, cada otro programador puede formar
  un grupo solo.

Así las respuestas son (programadores a los que nadie nombra) + (ciclos
a los que nadie apunta) y (programadores fuera de los ciclos) +
(ciclos). Seguir las flechas desde cada programador nuevo marcando el
recorrido encuentra cada ciclo una vez. `O(n)`.

En el ejemplo, 2 → 3 → 4 → 2 es un ciclo y 1 apunta a él: empezando por
1 se lleva a todos, mientras que empezando en el ciclo 1 queda solo.

Trampas:

- un programador que se nombra a sí mismo es un ciclo de uno;
- un ciclo con un árbol colgando no necesita grupo propio para el
  mínimo;
- los recorridos deben hacerse con un bucle y no con recursión, porque
  una cadena puede medir 10⁵.

Las respuestas coinciden con una búsqueda sobre todos los órdenes de
elección en 300 grafos aleatorios de hasta 8 programadores, y con una
implementación aceptada independiente en las pruebas grandes.

## Soluciones optimizadas

Las versiones compactas limitan a dos el contador de aristas entrantes. Cero identifica un inicio y un ciclo está aislado si todos sus vértices tienen contador uno. Un byte por vértice indica si está sin visitar, en el recorrido actual o terminado. Tras contar el ciclo encontrado, se siguen otra vez las mismas flechas para marcar el recorrido como terminado. Cada vértice se visita un número constante de veces y no se necesita un vector separado con el recorrido.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 2 088 KB frente a 5148 KB.

Las implementaciones base aceptadas [1742_graphs.java](1742_graphs.java), [1742_graphs.py](1742_graphs.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1742_graphs.cpp](1742_graphs.cpp) | G++ 13.2 x64 | graphs | O(n) | AC | 0.078 s | 2344 KB | 11289502 |
| [1742_graphs.go](1742_graphs.go) | Go 1.14 x64 | graphs | O(n) | AC | 0.078 s | 8728 KB | 11289503 |
| [1742_graphs.java](1742_graphs.java) \* | Java 1.8 | graphs | O(n) | AC | 0.140 s | 2020 KB | 11289505 |
| [1742_graphs.py](1742_graphs.py) \* | Python 3.12 x64 | graphs | O(n) | AC | 0.187 s | 13504 KB | 11289504 |
| [1742_graphs.rs](1742_graphs.rs) | Rust 1.75 x64 | graphs | O(n) | AC | 0.015 s | 5148 KB | 11289506 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1742_graphs_optimized.cpp](1742_graphs_optimized.cpp) \* | G++ 13.2 x64 | graphs | O(n) | AC | 0.062 s | 576 KB | 11310429 |
| [1742_graphs_optimized.go](1742_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(n) | AC | 0.046 s | 2084 KB | 11310371 |
| [1742_graphs_optimized.rs](1742_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O(n) | AC | 0.031 s | 2088 KB | 11310368 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
