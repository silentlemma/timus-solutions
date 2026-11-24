# 1346. Intervalos de monotonía

[Timus 1346](https://acm.timus.ru/problem.aspx?space=1&num=1346) · dificultad 297 · greedy

Problema original de Alexander Klepinin, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función F está dada en la rejilla entera A, A + 1, …, B, con
0 ≤ A < B ≤ 100 000 y valores de −100 000 a 100 000. Hay que partir la
rejilla en el menor número de intervalos en cada uno de los cuales F no
decrece o no crece, e imprimir cuántos son.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A y B, luego los valores F(A), …, F(B), separados por espacios o saltos
de línea.

## Salida

El menor número de intervalos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
1 2 3 4 2 1 -1 3 6 7
```

Salida:

```
3
```

## Solución

Los intervalos reparten los puntos de la rejilla, así que el paso entre
el último punto de un intervalo y el primero del siguiente es libre.
Cualquier parte de un intervalo monótono vuelve a ser monótona. Por eso
nunca estorba alargar el primer intervalo todo lo posible, y lo mismo
vale para cada siguiente: el conteo voraz es el mínimo.

Un intervalo se alarga mientras siga siendo monótono. Su sentido lo
fija su primer paso que no es plano, y los pasos planos valen para
cualquier sentido. El primer paso contra ese sentido acaba el
intervalo, y el siguiente empieza en el punto siguiente. `O(B − A)`.

Detalles a tener en cuenta:

- el paso entre dos intervalos es libre: 1 3 2 4 solo necesita 2
  intervalos, 1 3 y 2 4 (prueba 02);
- los pasos planos pertenecen al intervalo vaya en el sentido que vaya,
  y una función constante es un solo intervalo (pruebas 03, 05 y 06);
- los valores pueden venir en varias líneas.

Los conteos se compararon con una programación dinámica sobre todos los
repartos en 500 funciones aleatorias de hasta 12 puntos.

## Soluciones optimizadas

`1346_greedy_optimized.cpp`. Mantiene el recorrido voraz de monotonía. Al invertir una dirección no nula abre otro intervalo y borra su dirección: el paso de frontera no pertenece a ninguno. Valores iguales no fijan dirección. Solo conserva valor anterior, dirección y conteo: O(B-A+1) tiempo, O(1) espacio auxiliar. Sustituye entrada formateada por fread de 16384 bytes y un byte centinela, conservando signos/dígitos parciales entre recargas y detectando EOF sin bucle infinito en entrada vacía. Escribe el conteo como bytes decimales. Escáner compartido probado con ambos tamaños, AddressSanitizer/UndefinedBehaviorSanitizer y 100019 valores por tamaño. Conserva la implementación didáctica.

Accepted exacto G++ 13.2 x64 #11327408: 0.015 s / 92 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/71, memoria 1/71. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. También cumple la meta propia de C++: ambas métricas entre diez primeras o 15% superior, sin asterisco. El registro optimizado documentado antes #11310334 era 0.031 s / 84 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1346_greedy_optimized.cpp`: 0.015 s / 92 KB; base didáctica conservada `1346_greedy.cpp`: 0.062 s / 588 KB.

Comparación histórica de la revisión anterior: Las versiones en C++ y Go conservan el recorrido voraz y procesan cada valor al leerlo. Solo guardan el valor anterior, la dirección del intervalo actual y el número de intervalos. El búfer de entrada tiene tamaño fijo, así que el recorrido tarda O(B − A + 1) y requiere O(1) espacio adicional. El envío aceptado de C++ tardó 0,031 s y usó 84 KB, frente a 0,062 s y 588 KB de la versión base. Go usó 1588 KB en lugar de 2512 KB, con 0,031 s en ambas versiones.

Las implementaciones base aceptadas [1346_greedy.java](1346_greedy.java), [1346_greedy.py](1346_greedy.py), [1346_greedy.rs](1346_greedy.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1346_greedy_optimized.py`. Se procesa la secuencia en flujo, guardando solo el valor anterior, la dirección y el número de intervalos. Los valores iguales no fijan dirección; un cambio inicia otro intervalo. El tiempo es lineal y el estado del algoritmo constante. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328773 (Python 3.12 x64): **0.109 s / 724 KB**. Comparación archivada: `1346_greedy.py` (Python 3.12 x64) — 0.14 s / 11140 KB (#11285126).


`1346_implementation_parsing_optimized.rs`. La salida directa se especializa a los tipos usados, evitando despacho genérico y cadenas temporales. El texto fijo usa escrituras nativas y los números se convierten exactamente con el signo requerido. Se conservan decisiones matemáticas y versiones simples.

Este código exacto tiene su propio Accepted y cumple los [criterios compartidos](../../RATING_CRITERIA.md). El tiempo y la memoria siguientes proceden de una misma ejecución; las mediciones repetidas pueden variar. Se conservan las versiones sencillas y optimizadas distintas existentes.

Accepted #11329367 (Rust 1.75 x64): **0.015 s / 56 KB**.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Las cinco soluciones hacen la misma pasada.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1346_greedy.cpp](1346_greedy.cpp) | G++ 13.2 x64 | greedy | O(B - A) | AC | 0.062 s | 588 KB | 11285122 |
| [1346_greedy.go](1346_greedy.go) | Go 1.14 x64 | greedy | O(B - A) | AC | 0.031 s | 2512 KB | 11285125 |
| [1346_greedy.java](1346_greedy.java) | Java 1.8 | greedy | O(B - A) | AC | 0.109 s | 900 KB | 11285127 |
| [1346_greedy.py](1346_greedy.py) | Python 3.12 x64 | greedy | O(B - A) | AC | 0.140 s | 11140 KB | 11285126 |
| [1346_greedy.rs](1346_greedy.rs) | Rust 1.75 x64 | greedy | O(B - A) | AC | 0.015 s | 2632 KB | 11285128 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1346_greedy_optimized.cpp](1346_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(B-A+1) time; O(1) auxiliary storage | AC | 0.015 s | 92 KB | 11327408 |
| [1346_greedy_optimized.go](1346_greedy_optimized.go) | Go 1.14 x64 | greedy | O(B - A + 1) | AC | 0.031 s | 1588 KB | 11310367 |
| [1346_greedy_optimized.py](1346_greedy_optimized.py) | Python 3.12 x64 | greedy | O(B-A+1) time; O(1) state + bounded input buffer | AC | 0.109 s | 724 KB | 11328773 |
| [1346_implementation_parsing_optimized.rs](1346_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(B-A+1) time; O(1) state + bounded input buffer | AC | 0.015 s | 56 KB | 11329367 |
