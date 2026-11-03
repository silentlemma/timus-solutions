# 1737. Mnemotecnia y palíndromos 3

[Timus 1737](https://acm.timus.ru/problem.aspx?space=1&num=1737) · dificultad 254 · strings

Problema original de Alexander Ipatov, del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Listar en orden alfabético todas las palabras de longitud n sobre las
letras a, b y c que no tienen ninguna subcadena palíndroma de dos o más
letras. Si ocuparían más de 100 000 letras en total, imprimir
`TOO LONG`.

## Entrada

n (1 ≤ n ≤ 20 000).

## Salida

Las palabras, una por línea, o `TOO LONG`.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
ab
ac
ba
bc
ca
cb
```

## Solución

Un palíndromo de dos o más letras tiene en su centro un palíndromo de
dos o tres letras, así que basta con que no haya dos letras vecinas
iguales ni dos letras iguales a una de distancia. Entonces tres letras
seguidas cualesquiera son a, b y c en algún orden, y cada letra repite
la de tres posiciones atrás: la palabra es uno de los seis órdenes de
a, b y c repetido. Así hay tres palabras para n = 1 y seis para todo n
mayor, y la respuesta es `TOO LONG` cuando 6n > 100 000, es decir, desde
n = 16 667. `O(n)`.

Trampas:

- para n = 1 los seis órdenes dan solo tres palabras distintas;
- el límite es sobre la longitud total, no sobre el número de palabras.

Las listas coinciden con la comprobación una por una de todas las
palabras sobre a, b y c para n hasta 9.

## Soluciones optimizadas

Para longitud al menos dos, las primeras dos letras distintas determinan la palabra periódica válida. Enumerar los pares alfabéticamente emite directamente las seis palabras en orden lexicográfico, sin conjunto, deduplicación ni ordenación. El caso de una letra emite tres palabras aparte. Se decide si la salida es demasiado larga antes de construirla y se escribe por bloques, sin conservar todas las palabras y su concatenación.

- `1737_strings_optimized.cpp`: 0.031 s / 112 KB; base `1737_strings.cpp`: 0.031 s / 232 KB; cambio respecto a la base: tiempo -0.0%, memoria -51.7%.
- `1737_strings_optimized.go`: 0.015 s / 964 KB; base `1737_strings.go`: 0.031 s / 1448 KB; cambio respecto a la base: tiempo -51.6%, memoria -33.4%.
- `1737_strings_optimized.java`: 0.093 s / 388 KB; base `1737_strings.java`: 0.109 s / 3016 KB; cambio respecto a la base: tiempo -14.7%, memoria -87.1%.
- `1737_strings_optimized.py`: 0.093 s / 444 KB; base `1737_strings.py`: 0.109 s / 980 KB; cambio respecto a la base: tiempo -14.7%, memoria -54.7%.
- `1737_strings_optimized.rs`: 0.015 s / 196 KB; base `1737_strings.rs`: 0.015 s / 328 KB; cambio respecto a la base: tiempo -0.0%, memoria -40.2%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1737_strings.cpp`; versión que cubre `1737_strings_optimized.cpp`; puestos tiempo/memoria 42/1, registros de otros autores 48/48.

- Go: base didáctica preferida `1737_strings.go`; versión que cubre `1737_strings.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1737_strings.java`; versión que cubre `1737_strings_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1737_strings.py`; versión que cubre `1737_strings_optimized.py`; puestos tiempo/memoria 5/7, registros de otros autores 15/15.

- Rust: base didáctica preferida `1737_strings.rs`; versión que cubre `1737_strings.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1737_strings.cpp](1737_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 232 KB | 11308913 |
| [1737_strings.go](1737_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1448 KB | 11289457 |
| [1737_strings.java](1737_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 3016 KB | 11308916 |
| [1737_strings.py](1737_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 980 KB | 11308917 |
| [1737_strings.rs](1737_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 328 KB | 11289460 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1737_strings_optimized.cpp](1737_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(output size) | AC | 0.031 s | 112 KB | 11308823 |
| [1737_strings_optimized.go](1737_strings_optimized.go) | Go 1.14 x64 | strings | O(output size) | AC | 0.015 s | 964 KB | 11308824 |
| [1737_strings_optimized.java](1737_strings_optimized.java) | Java 1.8 | strings | O(output size) | AC | 0.093 s | 388 KB | 11308825 |
| [1737_strings_optimized.py](1737_strings_optimized.py) \* | Python 3.12 x64 | strings | O(output size) | AC | 0.093 s | 444 KB | 11308821 |
| [1737_strings_optimized.rs](1737_strings_optimized.rs) | Rust 1.75 x64 | strings | O(output size) | AC | 0.015 s | 196 KB | 11308826 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
