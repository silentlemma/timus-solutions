# 1355. La calva, otra vez

[Timus 1355](https://acm.timus.ru/problem.aspx?space=1&num=1355) · dificultad 212 · number_theory

Problema original de Aleksandr Bikbaev, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las tabernas se numeran con enteros positivos, y desde la taberna n solo
se puede ir a una taberna cuyo número sea múltiplo de n. Un paseo
empieza en la taberna a y debe acabar en la taberna b, con una jarra de
cerveza en cada taberna del camino, a y b incluidas. Para cada uno de
T ≤ 20 pares con 1 ≤ a, b ≤ 10⁹, hay que imprimir el mayor número de
jarras, o 0 si no se puede llegar a b.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

T, luego T líneas con a y b.

## Salida

T líneas con las respuestas.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
30 89
2 16
3 243
1 1
2 2
```

Salida:

```
0
4
5
1
1
```

## Solución

Cada número del paseo divide al siguiente, así que solo se llega a b si
a divide a b. Entonces cada paso multiplica el número por un factor
mayor que 1, y el producto de todos los factores es q = b / a. Para
visitar tantas tabernas como sea posible, cada factor debe ser un primo,
de modo que el número de pasos es Ω(q), la cantidad de factores primos
de q contados con repetición. La respuesta es 1 + Ω(q), contando la
propia taberna a.

La división por tanteo hasta √q ≤ 31 623 da Ω(q). `O(T · √(b / a))`.

Detalles a tener en cuenta:

- con a = b se bebe una jarra, no cero (ejemplo);
- si b es menor que a o no es múltiplo suyo, la respuesta es 0
  (prueba 04);
- T puede ser 0, y entonces no se imprimen respuestas (prueba 02);
- q = 2²⁹ da más pasos que nadie, 30 jarras (prueba 03).

## Soluciones optimizadas

La versión didáctica conserva la división por prueba. La versión rápida en Python calcula el MCD del cociente con el producto fijo de todos los primos hasta 1000. El MCD identifica los divisores primos pequeños, que se eliminan del cociente con toda su multiplicidad. Los factores restantes superan 1000 y el cociente no supera 10^9, así que quedan como máximo dos. El segundo producto fijo contiene los primos entre 1001 y 31623. Un resto compuesto tiene un divisor en ese intervalo y un resto primo mayor que 10^6 es coprimo con el producto. Se cuentan dos factores o uno, respectivamente. Los productos se generan con una criba y se guardan como constantes hexadecimales.

- `1355_number_theory_math.py`: 0.062 s / 584 KB; base `1355_number_theory.py`: 0.109 s / 392 KB; cambio respecto a la base: tiempo -43.1%, memoria +49.0%.

## Notas por lenguaje

Las instantáneas se guardaron el 2 y el 4 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1355_number_theory.cpp`; fuente que cubre `1355_number_theory.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 61/61.

- Go: base didáctica preferida `1355_number_theory.go`; fuente que cubre `1355_number_theory.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1355_number_theory.java`; fuente que cubre `1355_number_theory.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1355_number_theory.py`; fuente que cubre `1355_number_theory_math.py`; puestos tiempo/memoria 1/4, registros de otros autores 13/13.

- Rust: base didáctica preferida `1355_number_theory.rs`; fuente que cubre `1355_number_theory.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1355_number_theory.cpp](1355_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 132 KB | 11285268 |
| [1355_number_theory.go](1355_number_theory.go) | Go 1.14 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 1100 KB | 11285270 |
| [1355_number_theory.java](1355_number_theory.java) | Java 1.8 | number_theory | O(T·√(b/a)) | AC | 0.078 s | 448 KB | 11285272 |
| [1355_number_theory.py](1355_number_theory.py) | Python 3.12 x64 | number_theory | O(T·√(b/a)) | AC | 0.109 s | 392 KB | 11285271 |
| [1355_number_theory.rs](1355_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 212 KB | 11285273 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1355_number_theory_math.py](1355_number_theory_math.py) \* | Python 3.12 x64 | number_theory, math | O(T*(P+log Q)) bounded arithmetic, P=1000 | AC | 0.062 s | 584 KB | 11310243 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
