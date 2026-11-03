# 2073. Una tabla resumen de registros de concursos

[Timus 2073](https://acm.timus.ru/problem.aspx?space=1&num=2073) · dificultad 242 · implementation

Problema original de Kirill Borozdin, preparado por Kirill Borozdin y Alexey Danilyuk, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan n ≤ 100 registros de concursos: un nombre de 1 a 30 letras,
dígitos y espacios, una fecha DD.MM.YY, el número de problemas p ≤ 13 y
de envíos s ≤ 100, y después s envíos, cada uno una letra de problema y
un veredicto. Imprimir una tabla dibujada con `+`, `-` y `|`: una fila
de encabezado y una fila por concurso con el nombre rellenado hasta 30
caracteres, la fecha (8 caracteres) y 13 marcas, una por letra A … M.
Una marca es `o` si el problema se aceptó al menos una vez, `x` si se
envió pero nunca se aceptó, `.` si estaba en el concurso pero no se
envió, y un espacio si el concurso no tenía ese problema. Los límites
son 1 segundo y 64 MB.

## Entrada

n, y para cada concurso la línea del nombre, la de la fecha, la línea
"p s" y s líneas "letra veredicto". Un veredicto es uno de `Accepted`,
`Wrong Answer`, `Runtime Error`, `Time Limit Exceeded`,
`Memory Limit Exceeded`, `Compilation Error`.

## Salida

La tabla, con el formato del ejemplo, con una línea de borde antes del
encabezado, después de él y después de cada concurso.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
Codeforces Gamma Round 512
29.02.16
5 4
A Accepted
B Accepted
C Accepted
E Accepted
URKOP
17.10.15
12 11
A Accepted
B Wrong Answer
B Time Limit Exceeded
J Accepted
B Accepted
J Time Limit Exceeded
J Accepted
F Accepted
E Runtime Error
H Accepted
E Runtime Error
```

Salida:

```
+------------------------------+--------+-------------+
|Contest name                  |Date    |ABCDEFGHIJKLM|
+------------------------------+--------+-------------+
|Codeforces Gamma Round 512    |29.02.16|ooo.o        |
+------------------------------+--------+-------------+
|URKOP                         |17.10.15|oo..xo.o.o.. |
+------------------------------+--------+-------------+
```

## Solución

Cada concurso empieza con p puntos seguidos de 13 − p espacios. Un envío
pone `o` en su marca si el veredicto es `Accepted`; cualquier otro pone
`x` salvo que la marca ya sea `o`. Después se imprimen las filas con el
nombre rellenado con espacios hasta 30 caracteres. La complejidad temporal es
O(input).

Los nombres pueden tener espacios, así que la entrada se lee línea a
línea, quitando los espacios y retornos de carro finales (un nombre
nunca termina en espacio). Las marcas conservan sus espacios finales: en
el ejemplo la segunda fila termina en `.. ` antes del borde.

## Soluciones optimizadas

No cambian las notas ni el formato exacto de la tabla. Se lee y emite un concurso cada vez con búferes de líneas y filas ASCII acotados, sin retener toda la entrada ni la salida completa. Se conservan nombres, fechas y anchuras de relleno. Los límites de búfer provienen de las longitudes de campos; los numéricos se analizan aparte y no se truncan con cotas de texto.

- `2073_implementation_optimized.cpp`: 0.015 s / 112 KB; base `2073_implementation.cpp`: 0.001 s / 356 KB; cambio respecto a la base: tiempo -0.0%, memoria -68.5%.
- `2073_implementation_optimized.java`: 0.093 s / 440 KB; base `2073_implementation.java`: 0.093 s / 2224 KB; cambio respecto a la base: tiempo -0.0%, memoria -80.2%.
- `2073_implementation_optimized.py`: 0.078 s / 464 KB; base `2073_implementation.py`: 0.062 s / 1196 KB; cambio respecto a la base: tiempo +25.8%, memoria -61.2%.
- `2073_implementation_optimized.rs`: 0.015 s / 224 KB; base `2073_implementation.rs`: 0.015 s / 732 KB; cambio respecto a la base: tiempo -0.0%, memoria -69.4%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `2073_implementation.cpp`; versión que cubre `2073_implementation_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 32/32.

- Go: base didáctica preferida `2073_implementation.go`; versión que cubre `2073_implementation.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `2073_implementation.java`; versión que cubre `2073_implementation.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `2073_implementation.py`; versión que cubre `2073_implementation_optimized.py`; puestos tiempo/memoria 1/2, registros de otros autores 9/9.

- Rust: base didáctica preferida `2073_implementation.rs`; versión que cubre `2073_implementation.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2073_implementation.cpp](2073_implementation.cpp) | G++ 13.2 x64 | implementation | O(input) | AC | 0.001 s | 356 KB | 11309231 |
| [2073_implementation.go](2073_implementation.go) | Go 1.14 x64 | implementation | O(input) | AC | 0.015 s | 1832 KB | 11294474 |
| [2073_implementation.java](2073_implementation.java) | Java 1.8 | implementation | O(input) | AC | 0.093 s | 2224 KB | 11309232 |
| [2073_implementation.py](2073_implementation.py) | Python 3.12 x64 | implementation | O(input) | AC | 0.062 s | 1196 KB | 11309233 |
| [2073_implementation.rs](2073_implementation.rs) | Rust 1.75 x64 | implementation | O(input) | AC | 0.015 s | 732 KB | 11309234 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2073_implementation_optimized.cpp](2073_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(input+output) | AC | 0.015 s | 112 KB | 11308727 |
| [2073_implementation_optimized.java](2073_implementation_optimized.java) | Java 1.8 | implementation | O(input+output) | AC | 0.093 s | 440 KB | 11308732 |
| [2073_implementation_optimized.py](2073_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(input+output) | AC | 0.078 s | 464 KB | 11308735 |
| [2073_implementation_optimized.rs](2073_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(input+output) | AC | 0.015 s | 224 KB | 11308736 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
