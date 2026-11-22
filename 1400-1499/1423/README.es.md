# 1423. Fábula de una cadena

[Timus 1423](https://acm.timus.ru/problem.aspx?space=1&num=1423) · dificultad 170 · strings

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las cadenas S y T tienen la misma longitud N (1 ≤ N ≤ 250 000) y
constan de caracteres con códigos de 33 a 255. Un desplazamiento cíclico
lleva el último carácter de una cadena al principio. Hay que imprimir un
número X (0 ≤ X < N) tal que X desplazamientos conviertan S en T, o −1
si no existe; vale cualquier X.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego S, luego T.

## Salida

X o −1.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador exige un entero; acepta-1 exactamente si la referencia dice que no hay giro. En otro caso vale cualquier X en [0,N) que mueva los últimos X bytes de S al principio y produzca T, sin exigir mínimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
11
abracadabra
racadabraab
```

Salida:

```
9
```

En el ejemplo, 9 desplazamientos convierten «abracadabra» en
«racadabraab».

## Solución

X desplazamientos a la derecha equivalen a N − X a la izquierda, y los
desplazamientos de S a la izquierda en k son justo las subcadenas de
longitud N de S + S que empiezan en k < N. Así que se busca T en
S + S: si empieza en la posición k, la respuesta es (N − k) mod N, y si
no aparece, −1. La búsqueda es Knuth–Morris–Pratt con la función de
prefijos de T, recorriendo S + S sin su último carácter; la búsqueda de
bytes integrada de Python también es lineal aquí. `O(N)`.

Detalles a tener en cuenta:

- una S periódica tiene varias respuestas, así que las pruebas usan un
  verificador (prueba 04);
- los caracteres por encima de 127 deben leerse como bytes; algunas
  formas de lectura los decodifican o incluso toman el código 160 por un
  espacio (prueba 05, gen3);
- una búsqueda ingenua de subcadenas puede ser cuadrática con cadenas de
  una sola letra repetida (gen2).

## Soluciones optimizadas

`1423_strings_optimized.py`. Conserva búsqueda exacta de bytes en S+S. T en desplazamiento izquierdo p da giro derecho (N−p) mod N; si no existe, −1. Cualquier giro válido sirve, también con periodicidad. Lee/split binario completo, bytes.find y salida corta antes de os._exit(0). Retiene O(N) bytes. Tiempo de E/S lineal más búsqueda del runtime, sin bucle Python por carácter. Este CPython es primero en ambas métricas; 1592 KB aún superan 1372 KB de la base.

Fuente exacto: Python 3.12 x64 Accepted #11327848: 0.062 s / 1592 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 1/55; 1/55. Admisión estricta usa tiempo y memoria con 1024 KB o más: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Ambas son primeras, sin asterisco. La variante anterior conservada tiene su par propio #11325463 (Python 3.12 x64): 0.093 s / 1592 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1423_strings_optimized.py`: 0.062 s / 1592 KB; base didáctica conservada `1423_strings.py`: 0.109 s / 1372 KB.

`1423_strings_optimized.java`. Conserva KMP de bytes y el desplazamiento a la derecha. Lee ambas palabras de N bytes directamente a sus arreglos finales con búfer de 4096 bytes, sin copia de entrada completa ni char decodificados. Prefijos int y cursor circular sustituyen módulo en el recorrido doble virtual. La igualdad de bytes preserva valores 33…255. Tiempo y espacio O(N); conserva la versión legible.

Accepted de fuente exacto Java 1.8 #11326951: 0.109 s / 1920 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 2/99, memoria 1/99. Con al menos 1024 KB, se exigen ambos criterios estrictos; pasan los dos.

- `1423_strings_optimized.java`: 0.109 s / 1920 KB; base didáctica conservada `1423_strings.java`: 0.156 s / 5744 KB; cambio de tiempo -30.1%; cambio de memoria -66.6%.

`1423_strings_optimized.rs`. Conserva KMP por bytes e índice de rotación derecha. Prefijos u32 y recorrido de s seguido de s sin último byte eliminan módulo por posición sin duplicar cadena. Tokens de bytes conservan caracteres33…255. O(N) tiempo/espacio, salida directa en vez de formato Rust.

Frente a `1423_strings.rs`: tiempo 0.031 s → 0.031 s; memoria 3052 KB → 1 804 KB.

La solución optimizada en C++ guarda la función de prefijos en campos de
18 bits empaquetados en un arreglo de palabras de 32 bits, porque cada
valor es menor que N ≤ 250 000 < 2^18, y lee un campo de dos palabras
vecinas a la vez; esto cuesta unos desplazamientos por acceso, pero
ocupa unos 0.56 MB en lugar de 1 MB para valores `int`. Además recorre S
dos veces en lugar de construir S + S, y lee S y T con `scanf` en dos
búferes estáticos de 250 001 bytes en lugar de `std::string` con `cin`:
{1423_strings_optimized.cpp}.

La solución optimizada en Go guarda la función de prefijos en valores
`int32` en lugar de `int` de 8 bytes, porque cada valor es menor que
N ≤ 250 000, y lee S y T directamente en arreglos de exactamente N bytes
con `io.ReadFull`, contando con que ambas cadenas tienen longitud N, en
lugar de leer toda la entrada y partirla en campos:
{1423_strings_optimized.go}.

### Mejora medida

Cada versión optimizada tiene Accepted y cumple un criterio de clasificación
o de mejora de recursos. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1423_strings_optimized.cpp`: reducción de tiempo -106.67%; reducción
  de memoria +40.82%; base: `1423_strings.cpp`.

- `1423_strings_optimized.go`: reducción de tiempo +0.00%; reducción de
  memoria +40.39%; base: `1423_strings.go`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings.cpp](1423_strings.cpp) | G++ 13.2 x64 | strings | O(N) | AC | 0.015 s | 1940 KB | 11286160 |
| [1423_strings.go](1423_strings.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 4268 KB | 11286161 |
| [1423_strings.java](1423_strings.java) | Java 1.8 | strings | O(N) | AC | 0.156 s | 5744 KB | 11307252 |
| [1423_strings.py](1423_strings.py) | Python 3.12 x64 | strings | O(N) | AC | 0.109 s | 1372 KB | 11286163 |
| [1423_strings.rs](1423_strings.rs) | Rust 1.75 x64 | strings | O(N) | AC | 0.031 s | 3052 KB | 11286168 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1423_strings_optimized.cpp](1423_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(N) | AC | 0.031 s | 1148 KB | 11307257 |
| [1423_strings_optimized.go](1423_strings_optimized.go) | Go 1.14 x64 | strings | O(N) | AC | 0.031 s | 2544 KB | 11307255 |
| [1423_strings_optimized.java](1423_strings_optimized.java) \* | Java 1.8 | strings | O(N) | AC | 0.109 s | 1920 KB | 11326951 |
| [1423_strings_optimized.py](1423_strings_optimized.py) | Python 3.12 x64 | strings | Linear I/O plus runtime substring search; O(N) bytes | AC | 0.062 s | 1592 KB | 11327848 |
| [1423_strings_optimized.rs](1423_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(N) time; O(N) space | AC | 0.031 s | 1804 KB | 11325527 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
