# 1279. Almacén

[Timus 1279](https://acm.timus.ru/problem.aspx?space=1&num=1279) · dificultad 424 · binary_search

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un almacén de N × M secciones (N, M ≤ 100) tiene pilas de contenedores
de altura entre 1 y 1000. Llegan K ≤ 10⁷ contenedores nuevos, que se
ponen de uno en uno sobre una sección de las más bajas. Hay que hallar
la menor altura cuando todos están colocados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, M y K, y luego N filas de M alturas.

## Salida

La menor altura tras colocar los contenedores.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2 3
1 3
2 4
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
3 3 10
1 2 3
4 5 6
7 8 9
```

Salida:

```
5
```

## Solución

Añadir siempre a la sección más baja es como verter agua: al final
todas las secciones por debajo de cierto nivel h han subido a h, y los
contenedores sobrantes subieron algunas de ellas a h + 1, pero no todas.
Subir todo al nivel h requiere need(h) = Σ max(0, h − altura)
contenedores, que crece con h. Así que la respuesta es el mayor h con
need(h) ≤ K, hallado por búsqueda binaria entre la altura menor y esa
altura más K. `O(N · M · log K)`.

Detalles a tener en cuenta:

- la respuesta puede pasar de 10⁷, y need(h) hasta 10⁴ · 10⁷ necesita
  64 bits (pruebas 03, 12);
- los contenedores sobrantes no suben el mínimo salvo que lleguen a
  todas las secciones de ese nivel (prueba 05);
- simular los contenedores de uno en uno es demasiado lento con
  K = 10⁷.

Las respuestas se compararon con colocar los contenedores de uno en uno
con un montículo en 199 almacenes pequeños.

## Soluciones optimizadas

Go y Rust aprovechan el límite inicial H=1000. Cuentan pilas por altura y elevan el nivel desde 1. Antes de salir de h incorporan sus pilas al número activo; cada capa completa cuesta un contenedor por pila activa. Si el presupuesto restante no basta, h es el mínimo final. Cuando todas están activas, se añaden directamente presupuesto dividido por N·M niveles; una capa incompleta no cambia el mínimo. Tiempo O(N·M+H), espacio O(H), sin ordenar ni repetir comprobaciones. El presupuesto es de 64 bits. Se conservan las búsquedas binarias y C++, Java y Python también cubren el conjunto rápido.

Las implementaciones base aceptadas [1279_binary_search.cpp](1279_binary_search.cpp), [1279_binary_search.java](1279_binary_search.java), [1279_binary_search.py](1279_binary_search.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1279_sorting_optimized.py`. Se ordenan las alturas y se eleva el prefijo más bajo hasta la siguiente mientras alcancen los contenedores. El resto se divide por el tamaño del prefijo. Sustituye la búsqueda binaria por un recorrido ordenado: tiempo O(nm log(nm)) y espacio O(nm). El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328665 (Python 3.12 x64): **0.062 s / 1296 KB**. Comparación archivada: `1279_binary_search.py` (Python 3.12 x64) — 0.109 s / 1344 KB (#11284394).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1279_binary_search_implementation_optimized.rs`. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328966 (Rust 1.75 x64): **0.015 s / 460 KB**. Comparación archivada: `1279_binary_search.rs` (Rust 1.75 x64) — 0.031 s / 512 KB (#11284398).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Misma búsqueda binaria: sumas de precisión arbitraria en Python y de
  64 bits en los demás.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1279_binary_search.cpp](1279_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N · M · log K) | AC | 0.015 s | 280 KB | 11284386 |
| [1279_binary_search.go](1279_binary_search.go) | Go 1.14 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 1208 KB | 11284389 |
| [1279_binary_search.java](1279_binary_search.java) | Java 1.8 | binary_search | O(N · M · log K) | AC | 0.109 s | 600 KB | 11284396 |
| [1279_binary_search.py](1279_binary_search.py) | Python 3.12 x64 | binary_search | O(N · M · log K) | AC | 0.109 s | 1344 KB | 11284394 |
| [1279_binary_search.rs](1279_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 512 KB | 11284398 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1279_greedy.go](1279_greedy.go) | Go 1.14 x64 | greedy | O(N·M + H) | AC | 0.015 s | 320 KB | 11314936 |
| [1279_greedy.rs](1279_greedy.rs) | Rust 1.75 x64 | greedy | O(N·M + H) | AC | 0.031 s | 56 KB | 11314955 |
| [1279_sorting_optimized.py](1279_sorting_optimized.py) | Python 3.12 x64 | sorting | O(nm log(nm)) time; O(nm) space | AC | 0.062 s | 1296 KB | 11328665 |
| [1279_binary_search_implementation_optimized.rs](1279_binary_search_implementation_optimized.rs) | Rust 1.75 x64 | binary_search, implementation | O(N · M · log K) | AC | 0.015 s | 460 KB | 11328966 |
