# 1026. El k-ésimo menor elemento de una base de datos

[Timus 1026](https://acm.timus.ru/problem.aspx?space=1&num=1026) · dificultad 156 · sorting, prefix_sums

Problema original de Leonid Volkov, de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una base de datos guarda `N` enteros (`N ≤ 100 000`, cada uno de 1 a 5000,
en cualquier orden y con repeticiones). Responde `K` consultas
(`1 ≤ K ≤ 100`): para un `i` dado (`1 ≤ i ≤ N`), imprime el `i`-ésimo menor
elemento, contando las repeticiones.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` números, uno por línea; después una línea `###`; luego
`K` y las `K` consultas, una por línea.

## Salida

`K` líneas: las respuestas a las consultas en orden.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
42
7
5000
7
1
300
###
5
1
2
3
6
4
```

Salida:

```
1
7
7
5000
42
```

### Ejemplo 2

Entrada:

```
1
3000
###
1
1
```

Salida:

```
3000
```

## Solución

**Ordenación.** Se ordena la base una vez; la respuesta a la consulta `i`
es el elemento en la posición `i` (contando desde 1). `O(N log N + K)`.

**Conteo.** Los valores son pequeños, así que se cuenta cuántas veces
aparece cada valor `v ≤ 5000` y se toman sumas prefijas: `atMost[v]` es el
número de elementos no mayores que `v`. El `i`-ésimo menor elemento es el
menor `v` con `atMost[v] ≥ i`, que se encuentra con búsqueda binaria sobre
el arreglo no decreciente. `O(N + V + K log V)` con `V = 5000`.

Detalles a tener en cuenta:

- los valores repetidos ocupan varias posiciones: con 7 dos veces, las
  posiciones 2 y 3 contienen 7;
- la línea separadora `###` hay que saltarla, no leerla como número;
- lee la entrada rápido: son `10^5` líneas.

## Notas por lenguaje

- **C++**: la ordenación y también el conteo con búsqueda binaria.
- **Go**, **Python**, **Java**, **Rust**: ordenación; Python lee todos los
  tokens de una vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1026_prefix_sums.cpp](1026_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + V + K log V), V = 5000 | AC | 0.015 s | 440 KB |
| [1026_sorting.cpp](1026_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + K) | AC | 0.015 s | 816 KB |
| [1026_sorting.go](1026_sorting.go) | Go 1.14 x64 | sorting | O(N log N + K) | AC | 0.046 s | 2324 KB |
| [1026_sorting.java](1026_sorting.java) | Java 1.8 | sorting | O(N log N + K) | AC | 0.109 s | 5112 KB |
| [1026_sorting.py](1026_sorting.py) | Python 3.12 x64 | sorting | O(N log N + K) | AC | 0.109 s | 11668 KB |
| [1026_sorting.rs](1026_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + K) | AC | 0.031 s | 2128 KB |
