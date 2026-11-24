# 1061. La ventana más barata de búferes desbloqueados

[Timus 1061](https://acm.timus.ru/problem.aspx?space=1&num=1061) · dificultad 670 · prefix_sums

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` búferes (`1 ≤ N ≤ 100000`), cada uno bloqueado (`*`) o con un
valor de 0 a 9. Elige `K` búferes consecutivos (`1 ≤ K ≤ 10000`), ninguno
bloqueado, con el menor valor total, e imprime el número `L` del primero;
con totales iguales, el menor `L`. Imprime `0` si no existe tal ventana.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, y luego los `N` estados, 80 caracteres por línea (la última
puede ser más corta).

## Salida

`L`, o `0`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
100 53
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Salida:

```
0
```

### Ejemplo 2

Entrada:

```
100 10
2165745216091853477755800393859785807207523169954341**7363*9*94664808*4777717089
09825185827659480548
```

Salida:

```
36
```

## Solución

Dos sumas prefijas sobre los búferes: el valor total y el número de
búferes bloqueados entre los `i` primeros. Una ventana `[L, L + K − 1]` es
válida cuando el número de bloqueos no cambia a lo largo de ella, y su
valor es una diferencia de las sumas de valores. Revisar las `N − K + 1`
ventanas de izquierda a derecha y cambiar la mejor solo con un valor
estrictamente menor da el menor `L` entre las más baratas. `O(N)`.

Detalles a tener en cuenta:

- `K > N`: no hay ninguna ventana, la respuesta es `0`;
- empates: se conserva la primera ventana, así que la mejor solo se
  cambia con un valor estrictamente menor;
- los estados están repartidos en líneas de 80 caracteres: se leen
  caracteres y se saltan los saltos de línea;
- los búferes bloqueados no tienen valor; solo invalidan ventanas.

## Notas por lenguaje

- **C++**, **Go**, **Java**: los estados se leen carácter a carácter tras
  los dos números.
- **Python**, **Rust**: toda la entrada se separa en palabras y se unen
  las filas.

## Soluciones optimizadas

La versión en Python divide la entrada en tramos de búferes desbloqueados. En cada tramo desplaza una ventana de K búferes, resta el valor que sale y suma el que entra. Solo actualiza la respuesta con una suma estrictamente menor, conservando la primera posición en caso de empate. Usa O(N) de tiempo y O(N) de espacio con la entrada y los tramos. El envío 11317122 tardó 0.093 s y usó 1048 KB frente a 0.125 s y 9992 KB de la base.

La versión en Go lee los estados en flujo y guarda los últimos K valores en un búfer circular de bytes. Un búfer bloqueado reinicia la ventana. Usa O(N) de tiempo y O(K) de espacio. El envío 11317123 tardó 0.015 s y usó 1088 KB frente a 0.031 s y 2704 KB de la base.

La versión en Rust lee los estados en flujo y guarda los últimos K valores en un búfer circular de bytes. Un búfer bloqueado reinicia la ventana. Usa O(N) de tiempo y O(K) de espacio. El envío 11317124 tardó 0.015 s y usó 204 KB frente a 0.015 s y 2196 KB de la base.

La versión en C++ lee los estados en flujo y guarda los últimos K valores en un búfer circular de bytes. Un búfer bloqueado reinicia la ventana. Usa O(N) de tiempo y O(K) de espacio. El envío 11317125 tardó 0.015 s y usó 184 KB frente a 0.015 s y 1356 KB de la base.

La versión en Java lee los estados en flujo y guarda los últimos K valores en un búfer circular de bytes. Un búfer bloqueado reinicia la ventana. Usa O(N) de tiempo y O(K) de espacio. El envío 11317126 tardó 0.093 s y usó 408 KB frente a 0.109 s y 1592 KB de la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322104 · Go 1.14 x64 №11322105 · Java 1.8 №11322106 · Python 3.12 x64 №11322107 · Rust 1.75 x64 №11322108.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1061_prefix_sums.cpp](1061_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 1356 KB | 11322104 |
| [1061_prefix_sums.go](1061_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 2704 KB | 11322105 |
| [1061_prefix_sums.java](1061_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 1592 KB | 11322106 |
| [1061_prefix_sums.py](1061_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.125 s | 9992 KB | 11322107 |
| [1061_prefix_sums.rs](1061_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.015 s | 2196 KB | 11322108 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1061_two_pointers.py](1061_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.093 s | 1048 KB | 11317122 |
| [1061_two_pointers.go](1061_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.015 s | 1088 KB | 11317123 |
| [1061_two_pointers.rs](1061_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.015 s | 204 KB | 11317124 |
| [1061_two_pointers.cpp](1061_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 184 KB | 11317125 |
| [1061_two_pointers.java](1061_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.093 s | 408 KB | 11317126 |
