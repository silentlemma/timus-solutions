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
  64 bits (prueba 03);
- los contenedores sobrantes no suben el mínimo salvo que lleguen a
  todas las secciones de ese nivel (prueba 05);
- simular los contenedores de uno en uno es demasiado lento con
  K = 10⁷.

Las respuestas se compararon con colocar los contenedores de uno en uno
con un montículo en 199 almacenes pequeños.

## Notas por lenguaje

- Todos los lenguajes usan la misma búsqueda binaria con sumas de 64
  bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1279_binary_search.cpp](1279_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N · M · log K) | AC | 0.015 s | 280 KB |
| [1279_binary_search.go](1279_binary_search.go) | Go 1.14 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 1208 KB |
| [1279_binary_search.java](1279_binary_search.java) | Java 1.8 | binary_search | O(N · M · log K) | AC | 0.109 s | 600 KB |
| [1279_binary_search.py](1279_binary_search.py) | Python 3.12 x64 | binary_search | O(N · M · log K) | AC | 0.109 s | 1344 KB |
| [1279_binary_search.rs](1279_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N · M · log K) | AC | 0.031 s | 512 KB |
