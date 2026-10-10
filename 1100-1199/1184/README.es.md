# 1184. Los trozos iguales más largos en que se pueden cortar los cables

[Timus 1184](https://acm.timus.ru/problem.aspx?space=1&num=1184) · dificultad 244 · binary_search

Problema original de Vladimir Pinaev y Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N ≤ 10000` cables de 1 m a 100 km, dados al centímetro. Hay que
hallar la mayor longitud, en centímetros enteros, tal que los cables se
puedan cortar en al menos `K ≤ 10000` trozos de esa longitud.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, y luego las longitudes en metros con exactamente dos decimales.

## Salida

La longitud en metros con dos decimales, `0.00` si ni 1 cm sirve.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 11
8.02
7.43
4.57
5.39
```

Salida:

```
2.00
```

## Solución

Se trabaja en centímetros: las longitudes tienen exactamente dos
decimales, así que al quitar el punto quedan enteros exactos. Un cable de
longitud `c` da `⌊c/L⌋` trozos de longitud `L`, y esa cuenta solo baja al
crecer `L`. Así que se busca por bisección el mayor `L` con
`Σ ⌊c/L⌋ ≥ K`, entre 0 y el cable más largo; si ni `L = 1` basta, la
respuesta se queda en 0. `O(N log C)`.

Detalles a tener en cuenta:

- leer las longitudes como números en coma flotante puede convertir
  `8.02` en `801.99…` centímetros; analizarlas como texto lo evita;
- `K` puede superar la longitud total en centímetros, y entonces hay que
  imprimir `0.00`, no fallar;
- la salida necesita dos decimales, así que `2` se imprime como `2.00`.

Las respuestas se compararon con una solución escrita aparte en 300
existencias aleatorias y en todas las pruebas.

## Notas por lenguaje

- Python, Go, Java y Rust quitan el punto decimal de cada longitud; C++
  lee la parte entera y la fraccionaria como dos enteros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1184_binary_search.cpp](1184_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.031 s | 280 KB |
| [1184_binary_search.go](1184_binary_search.go) | Go 1.14 x64 | binary_search | O(N log C) | AC | 0.031 s | 1688 KB |
| [1184_binary_search.java](1184_binary_search.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.125 s | 6284 KB |
| [1184_binary_search.py](1184_binary_search.py) | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 1580 KB |
| [1184_binary_search.rs](1184_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 420 KB |
