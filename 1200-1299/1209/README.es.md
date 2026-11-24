# 1209. Las cifras de 1, 10, 100, 1000 escritos seguidos

[Timus 1209](https://acm.timus.ru/problem.aspx?space=1&num=1209) · dificultad 34 · math

Problema original de Alexey Lakhtin, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se escriben las potencias de diez una tras otra: `110100100010000…`.
Para hasta 65535 posiciones `1 ≤ K < 2³¹`, hay que imprimir la cifra de
cada posición.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las `N` posiciones.

## Salida

Las `N` cifras separadas por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
14
7
6
```

Salida:

```
0 0 1 0
```

## Solución

La `m`-ésima potencia escrita es `10^(m−1)`, que ocupa `m` cifras, así
que empieza en la posición `1 + (1 + 2 + … + (m − 1)) = 1 + m(m − 1)/2`,
y ahí está su único 1. La posición `K` tiene un 1 exactamente cuando
`K − 1 = m(m − 1)/2` para algún `m`, es decir, cuando
`8(K − 1) + 1 = (2m − 1)²` es un cuadrado perfecto. `O(1)` por posición.

Detalles a tener en cuenta:

- `8(K − 1) + 1` llega a unos `1.7·10¹⁰`, más de 32 bits;
- una raíz cuadrada en coma flotante puede fallar por uno cerca de
  cuadrados grandes, así que hay que corregirla con comprobaciones
  enteras exactas.

Las respuestas se compararon con una solución escrita aparte en todas
las posiciones de 1 a 65535, en posiciones aleatorias y en posiciones
junto a los unos.

## Soluciones optimizadas

`1209_math_optimized.py`. Conserva la prueba exacta isqrt: K se selecciona si 8*(K-1)+1 es cuadrado perfecto. Lee bloques de 4096 bytes conservando el token incompleto. Añade dígito y separador juntos a bytearray y vacía a los 4096 bytes, sin acumular consultas ni respuestas completas. Añade el salto final incluso con un bloque exactamente lleno. Enteros acotados dan O(Q) trabajo aritmético y búferes limitados, sin redondeo flotante ni tabla de respuestas. Escritura directa y os._exit(0) dentro de main.

Accepted exacto Python 3.12 x64 #11327504: 0.125 s / 748 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 7/209, memoria 23/209. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11326663 (Python 3.12 x64) era 0.156 s / 1076 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1209_math_optimized.py`: 0.125 s / 748 KB; base didáctica conservada `1209_math.py`: 0.125 s / 6556 KB.

Accepted exacto CPython 3.12 #11326663: 0.156 s / 1076 KB. Comparación guardada 2026-11-20 de compiladores actuales: tiempo 21/209, memoria 32/209. Ambas métricas exigidas pasan diez primeros o 15% superior, redondeando el corte porcentual hacia arriba. El asterisco sigue la meta separada Python de primer puesto en ambas.

El envío optimizado documentado antes #11303724 (Python 3.12 x64) registró 0.218 s / 492 KB. El actual CPython 3.12 registra menor tiempo y mayor memoria. Son medidas emparejadas de ejecuciones distintas; la comparación incluye elección de intérprete y variabilidad del juez. La base simple conservada es más rápida, 0.125 s; esta versión favorece menor memoria.

Las soluciones optimizadas (C++, Rust) analizan las posiciones a mano y
escriben cada respuesta como dos bytes, una cifra y un separador, en
lugar de reunir las respuestas en una cadena: C++ con `getchar` y
`putchar`, Rust desde un búfer de entrada de 1 KB hacia un `BufWriter`.
La comprobación es la misma. C++, 0.031 s en lugar de 0.062 s y 84 KB en
lugar de 388 KB; Rust, 188 KB en lugar de 3160 KB, con el mismo tiempo.

## Notas por lenguaje

- Python usa `math.isqrt`, que es exacta; los demás lenguajes corrigen
  la raíz en coma flotante con comparaciones enteras.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1209_math.cpp](1209_math.cpp) | G++ 13.2 x64 | math | O(1) per position | AC | 0.062 s | 388 KB | 11283621 |
| [1209_math.go](1209_math.go) | Go 1.14 x64 | math | O(1) per position | AC | 0.062 s | 2664 KB | 11283625 |
| [1209_math.java](1209_math.java) | Java 1.8 | math | O(1) per position | AC | 0.062 s | 1372 KB | 11283627 |
| [1209_math.py](1209_math.py) | Python 3.12 x64 | math | O(1) per position | AC | 0.125 s | 6556 KB | 11283626 |
| [1209_math.rs](1209_math.rs) | Rust 1.75 x64 | math | O(1) per position | AC | 0.015 s | 3160 KB | 11283628 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1209_math_optimized.cpp](1209_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) per position | AC | 0.031 s | 84 KB | 11303960 |
| [1209_math_optimized.py](1209_math_optimized.py) | Python 3.12 x64 | math | O(Q) time; bounded I/O buffers | AC | 0.125 s | 748 KB | 11327504 |
| [1209_math_optimized.rs](1209_math_optimized.rs) | Rust 1.75 x64 | math | O(1) per position | AC | 0.015 s | 188 KB | 11303961 |
