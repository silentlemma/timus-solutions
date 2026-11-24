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

Revisiones Accepted solo de formato: `1742_graphs.cpp` #11327489, `1742_graphs.py` #11327491, `1742_graphs.rs` #11327493. Cada fila usa esa revisión exacta y su propio par tiempo/memoria; no se atribuye una mejora de rendimiento al formato.

`1742_graphs_optimized.cpp`. Conserva el recorrido lineal del grafo funcional y grados de entrada saturados a 0/1/2. Estados de un byte distinguen vértices nuevos, en camino y terminados; vuelve a seguir flechas para cerrar el camino sin arreglo aparte. C++ lee enteros con búfer fread fijo de 4096 bytes, en lugar de entrada numérica formateada. Tiempo O(n), espacio del grafo O(n), sin nuevo algoritmo ni archivo duplicado.

Accepted exacto G++ 13.2 x64 #11326976: 0.015 s / 532 KB. Comparación guardada del 2026-11-20: tiempo 1/53, memoria 1/53; ambas metas de diez primeros cumplidas, sin asterisco. Bajo 1024 KB la admisión estricta usa solo tiempo. Ejecución optimizada anterior #11310429: 0.062 s / 576 KB. Son pares independientes; la memoria registrada nueva es menor. El C++ didáctico conservado tiene su propio Accepted actual #11327489: 0.093 s / 2324 KB, sin cambiar su algoritmo.

Las versiones compactas limitan a dos el contador de aristas entrantes. Cero identifica un inicio y un ciclo está aislado si todos sus vértices tienen contador uno. Un byte por vértice indica si está sin visitar, en el recorrido actual o terminado. Tras contar el ciclo encontrado, se siguen otra vez las mismas flechas para marcar el recorrido como terminado. Cada vértice se visita un número constante de veces y no se necesita un vector separado con el recorrido.

Rust optimizado / base didáctica conservada: Accepted #11310368 0.031 s / 2088 KB; Accepted #11327493 0.031 s / 5168 KB.

Los fuentes didácticos Accepted conservados [1742_graphs.java](1742_graphs.java), [1742_graphs.py](1742_graphs.py) cumplen diez primeros o 15% superior en las métricas exigidas de la comparación guardada. La tabla contiene sus pares actuales exactos, incluidas revisiones solo de formato. Algoritmos intactos y sin copias optimizadas idénticas; el asterisco indica la meta propia del lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1742_graphs.cpp](1742_graphs.cpp) | G++ 13.2 x64 | graphs | O(n) | AC | 0.093 s | 2324 KB | 11327489 |
| [1742_graphs.go](1742_graphs.go) | Go 1.14 x64 | graphs | O(n) | AC | 0.078 s | 8728 KB | 11289503 |
| [1742_graphs.java](1742_graphs.java) \* | Java 1.8 | graphs | O(n) | AC | 0.140 s | 2020 KB | 11289505 |
| [1742_graphs.py](1742_graphs.py) \* | Python 3.12 x64 | graphs | O(n) | AC | 0.156 s | 13532 KB | 11327491 |
| [1742_graphs.rs](1742_graphs.rs) | Rust 1.75 x64 | graphs | O(n) | AC | 0.031 s | 5168 KB | 11327493 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1742_graphs_optimized.cpp](1742_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(n) | AC | 0.015 s | 532 KB | 11326976 |
| [1742_graphs_optimized.go](1742_graphs_optimized.go) | Go 1.14 x64 | graphs | O(n) | AC | 0.046 s | 2084 KB | 11310371 |
| [1742_graphs_optimized.rs](1742_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(n) | AC | 0.031 s | 2088 KB | 11310368 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
