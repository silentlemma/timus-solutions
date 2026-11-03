# 1917. Eliminación segura de grupos por umbral

[Timus 1917](https://acm.timus.ru/problem.aspx?space=1&num=1917) · difficulty 242 · greedy

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada moneda tiene un umbral positivo. Un hechizo de fuerza s elimina
todas las monedas restantes con umbral≤s y libera energía s por la
cantidad recién eliminada. Cada hechizo debe liberar como máximo p.
Maximizar monedas eliminadas y, después, minimizar hechizos para ese máximo.
Límites: 1 segundo, 64 MB.

## Entrada

n,p con 1≤n≤1000 y 1≤p≤1 000 000 000, seguidos por n umbrales
1≤aᵢ≤1 000 000 en cualquier orden.

## Salida

Máxima cantidad eliminable y mínimo número de hechizos. Si no se puede
eliminar ninguna moneda, escribir `0 0`.

## Evaluación

Comparación exacta de los dos tokens enteros, en ese orden.

## Ejemplos

```
5 4
4 1 4 1 2
```

```
3 2
```

## Solución

Ordenar y agrupar umbrales iguales. Un grupo de c monedas con umbral t
no puede dividirse: un hechizo débil no elimina ninguna, y el primero
con fuerza≥t elimina todas simultáneamente.

Si ct>p, ese grupo no se puede eliminar ni solo. Mayor fuerza o más
monedas empeoran la energía. También bloquea todos los umbrales superiores,
pues cualquier hechizo que los elimine incluiría este grupo. El máximo
es el prefijo anterior al primer grupo así; cada grupo previo puede
eliminarse individualmente, por lo que se alcanza ese límite.

Dividir el prefijo factible de forma voraz. Mantener active monedas
en el lote actual; añadir el siguiente grupo entero si (active+c)t≤p.
Si no cabe, cerrar el lote previo no vacío y comenzar con el nuevo grupo.
Cerrar el lote final si queda alguno. La fuerza mínima de cada lote
es su umbral máximo. Comprobar ct>p antes de iniciar un lote y no contar vacíos.

### Optimalidad del lote más largo

Al añadir grupos no disminuyen ni cantidad ni umbral máximo. El primer
lote voraz es el mayor prefijo factible. Sustituir el primer lote de
cualquier partición óptima por él, borrar de los lotes posteriores las
monedas adicionales eliminadas y descartar lotes vacíos. Ningún lote
restante aumenta su cantidad ni umbral, así que sigue siendo seguro.
El número de hechizos no crece. Repetir el intercambio sobre los grupos
restantes demuestra el mínimo global.

Tiempo `O(n log n)` por ordenar, recorrido posterior lineal; memoria `O(n)`
incluida la entrada y copia ordenada.

En el ejemplo se eliminan dos unos con fuerza 1 y el dos con fuerza 2.
Los dos cuatros producirían energía 8>4. Se consiguen tres monedas en dos hechizos.

No dividir umbrales iguales ni saltar un grupo inferior inseguro.
La energía permite igualdad; contar todas las monedas destruidas a la vez.
Reiniciar solo tras contabilizar el lote previo no vacío. Un grupo inseguro
posterior no invalida el lote pendiente. Primero maximizar monedas, luego minimizar hechizos.

## Soluciones optimizadas

No cambia el voraz por grupos: los valores iguales son inseparables y no se puede saltar el primer grupo inseguro. Java ordena el arreglo primitivo in situ con heapsort iterativo, evitando clases auxiliares, copias y memoria temporal. La entrada de bytes y salida ASCII acotadas sustituyen objetos de tokens y formato. Los productos de comprobación usan enteros anchos y la memoria auxiliar de ordenación es constante.

- `1917_greedy_optimized.java`: 0.109 s / 380 KB; base `1917_greedy.java`: 0.125 s / 648 KB; cambio respecto a la base: tiempo -12.8%, memoria -41.4%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1917_greedy.cpp`; versión que cubre `1917_greedy.cpp`; puestos tiempo/memoria 1/9, registros de otros autores 42/42.

- Go: base didáctica preferida `1917_greedy.go`; versión que cubre `1917_greedy.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1917_greedy.java`; versión que cubre `1917_greedy_optimized.java`; puestos tiempo/memoria 2/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1917_greedy.py`; versión que cubre `1917_greedy.py`; puestos tiempo/memoria 1/1, registros de otros autores 6/6.

- Rust: base didáctica preferida `1917_greedy.rs`; versión que cubre `1917_greedy.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1917_greedy.cpp](1917_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.015 s | 416 KB | 11291446 |
| [1917_greedy.go](1917_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 1112 KB | 11291447 |
| [1917_greedy.java](1917_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.125 s | 648 KB | 11291452 |
| [1917_greedy.py](1917_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.078 s | 572 KB | 11291451 |
| [1917_greedy.rs](1917_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 240 KB | 11291453 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1917_greedy_optimized.java](1917_greedy_optimized.java) \* | Java 1.8 | greedy | O(N log N) | AC | 0.109 s | 380 KB | 11309400 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
