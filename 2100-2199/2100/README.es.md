# 2100. Contar los invitados y evitar el trece

[Timus 2100](https://acm.timus.ru/problem.aspx?space=1&num=2100) · dificultad 29 · implementation

Problema original de Alexey Danilyuk, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pareja invita a n amigos; una respuesta `name+one` significa que el
amigo viene con su pareja. Todos se sientan a una mesa con los novios, y
si se sentaran exactamente 13, se añade un maniquí. Cada asiento cuesta
100 dólares. Imprimir el coste de la cena. Los límites son 1 segundo y
64 MB.

## Entrada

1 ≤ n ≤ 20 y después las n respuestas, cada una un nombre de a lo sumo 20 letras
latinas, quizá con `+one`.

## Salida

El coste en dólares.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
Ted+one
Robin
Barney
```

Salida:

```
600
```

### Ejemplo 2

Entrada:

```
6
Alice+one
Bob+one
carl
Debora+one
Enrique+one
FRED+one
```

Salida:

```
1400
```

## Solución

Se empieza por los dos anfitriones, se suma 2 por cada respuesta que
termina en `+one` y 1 por las demás, se convierte 13 en 14 y se
multiplica por 100.

En el segundo ejemplo se sentarían 2 + 5 · 2 + 1 = 13 personas, así que
se les une un maniquí: 1400.

## Soluciones optimizadas

La solución optimizada en C++ lee las respuestas con `scanf` en un búfer
de 25 bytes en lugar de `iostream` y cuenta las que contienen `+`,
porque solo lo tiene una respuesta que termina en `+one`: 128 KB en
lugar de 396 KB, con el mismo tiempo.

La solución optimizada en Java lee la entrada en bloques de 1 KB y, como
la de C++, cuenta byte a byte los signos `+` de las respuestas en lugar
de usar `Scanner` y cadenas: 0.093 s en lugar de 0.140 s y 364 KB en
lugar de 1572 KB.

Leer las invitaciones byte por byte y contar un acompañante al encontrar el signo más. El envío aceptado 11301849 tardó 0.031 s y usó 924 KB. La versión sencilla tardó 0.031 s y usó 1076 KB.

Leer las invitaciones desde un búfer de bytes y contar los acompañantes según el sufijo de cada línea. El envío aceptado 11324260 tardó 0.125 s y usó 264 KB. La versión sencilla tardó 0.078 s y usó 420 KB. El tiempo registrado es mayor que el de la versión sencilla.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2100_parsing_optimized.rs`. Las invitaciones se leen como flujo acotado y solo se guarda el sufijo de cuatro bytes para detectar +one. No se conserva la entrada completa ni cadenas de invitación; no cambia el recuento. Los dígitos completos se convierten dentro del bloque, manteniendo local el cursor hasta un límite. La acumulación negativa admite el mínimo con signo y evita una rama o llamada por dígito, conservando EOF y signos opcionales.

Accepted #11329207 (Rust 1.75 x64): **0.015 s / 56 KB**. Comparación archivada: `2100_implementation.rs` (Rust 1.75 x64) — 0.046 s / 236 KB (#11294714).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2100_implementation.cpp](2100_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 396 KB | 11303533 |
| [2100_implementation.go](2100_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB | 11294707 |
| [2100_implementation.java](2100_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1572 KB | 11303534 |
| [2100_implementation.py](2100_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 420 KB | 11294708 |
| [2100_implementation.rs](2100_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 236 KB | 11294714 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2100_implementation_optimized.cpp](2100_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303968 |
| [2100_implementation_optimized.java](2100_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 364 KB | 11303969 |
| [2100_implementation_optimized.go](2100_implementation_optimized.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 924 KB | 11301849 |
| [2100_implementation_optimized.py](2100_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) | AC | 0.125 s | 264 KB | 11324260 |
| [2100_parsing_optimized.rs](2100_parsing_optimized.rs) | Rust 1.75 x64 | parsing | O(n) | AC | 0.015 s | 56 KB | 11329207 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
