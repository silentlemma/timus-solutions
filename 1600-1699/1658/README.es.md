# 1658. Suma de cifras

[Timus 1658](https://acm.timus.ru/problem.aspx?space=1&num=1658) · dificultad 203 · dp

Problema original de Vladimir Yakovlev (idea de Stanislav Vasilyev), del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada una de t consultas, dada la suma s₁ de las cifras de un entero
positivo y la suma s₂ de sus cuadrados, hay que imprimir el menor entero
así, o `No solution` si no hay ninguno de a lo sumo 100 cifras.

## Entrada

t (a lo sumo 10000) y luego t pares s₁ s₂ (1 ≤ s₁, s₂ ≤ 10000).

## Salida

El menor número de cada consulta, o `No solution`.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
9 81
12 9
6 10
7 9
```

Salida:

```
9
No solution
1122
111112
```

## Solución

El menor número tiene la menor cantidad de cifras y, entre esos, es la
menor cadena. Nunca contiene un cero: un cero añade una cifra sin cambiar
ninguna suma, así que no sería el más corto. Con a lo sumo 100 cifras las
sumas no pasan de 900 y 8100, así que las consultas mayores no tienen
respuesta.

Salvo en Python, una tabla con la menor cantidad de cifras no nulas para cada par
(s₁, s₂) hasta 900 × 8100 se llena en una pasada: cada casilla es una más
que la mejor casilla a la que se llega quitando una cifra d y d². La
respuesta se construye de forma voraz: la primera cifra es la menor d
tras la cual al resto le falta exactamente una cifra menos, y así
sucesivamente. Las cifras salen ordenadas, así que cada búsqueda puede
empezar en la cifra anterior. `O(S₁ · S₂ · 9)` para la tabla y `O(100)`
por consulta.

Detalles a tener en cuenta:

- la tabla tiene 7,3 millones de casillas, así que se guarda en bytes;
- una suma de cuadrados menor que la de cifras, o mayor que nueve veces
  ella, es imposible; la tabla lo recoge sin casos especiales;
- s₁ = 900 con s₂ = 8100 son cien nueves, una cifra más ya es demasiado
  larga (prueba 02).

Las respuestas coinciden con una implementación aceptada independiente
en 80 000 consultas.

## Soluciones optimizadas

La DP de momentos de dígitos conserva solo estados compatibles con cotas y paridad, evitando una tabla rectangular de sumas imposibles. Las cotas de dígitos equilibrados y de cuadrados máximos determinan las filas comprimidas. Los valores siguen indicando el mínimo número de dígitos y se reconstruye por transiciones válidas. Python agrupa transiciones mediante desplazamientos y OR exactos, sin flotantes. La normalización elimina relleno nulo sin perder estados, y no introduce tablas de respuestas.

C cuenta estados comprimidos viables, T consultas y K la cota de longitud; el factor 9 corresponde a dígitos no nulos.

- `1658_dp_optimized.cpp`: 0.046 s / 3292 KB; base `1658_dp.cpp`: 0.125 s / 9572 KB; cambio respecto a la base: tiempo -63.2%, memoria -65.6%.
- `1658_dp_optimized.go`: 0.062 s / 4488 KB; base `1658_dp.go`: 0.203 s / 12960 KB; cambio respecto a la base: tiempo -69.5%, memoria -65.4%.
- `1658_dp_optimized.java`: 0.156 s / 9148 KB; base `1658_dp.java`: 0.265 s / 14280 KB; cambio respecto a la base: tiempo -41.1%, memoria -35.9%.
- `1658_bitmask_dp.py`: 1.031 s / 12680 KB; base `1658_dp.py`: 1.578 s / 23432 KB; cambio respecto a la base: tiempo -34.7%, memoria -45.9%.
- `1658_dp_optimized.rs`: 0.031 s / 2800 KB; base `1658_dp.rs`: 0.156 s / 9532 KB; cambio respecto a la base: tiempo -80.1%, memoria -70.6%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1658_dp.cpp`; versión que cubre `1658_dp_optimized.cpp`; puestos tiempo/memoria 5/3, registros de otros autores 87/87.

- Go: base didáctica preferida `1658_dp.go`; versión que cubre `1658_dp.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1658_dp.java`; versión que cubre `1658_dp.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1658_dp.py`; versión que cubre `1658_bitmask_dp.py`; puestos tiempo/memoria 2/1, registros de otros autores 2/2.

- Rust: base didáctica preferida `1658_dp.rs`; versión que cubre `1658_dp_optimized.rs`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1658_dp.cpp](1658_dp.cpp) | G++ 13.2 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.125 s | 9572 KB | 11308834 |
| [1658_dp.go](1658_dp.go) | Go 1.14 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.203 s | 12960 KB | 11288594 |
| [1658_dp.java](1658_dp.java) | Java 1.8 | dp | O(S₁ · S₂ · 9) | AC | 0.265 s | 14280 KB | 11308836 |
| [1658_dp.py](1658_dp.py) | Python 3.12 x64 | dp | O(K · S₁ · S₂ · 9) | AC | 1.578 s | 23432 KB | 11288595 |
| [1658_dp.rs](1658_dp.rs) | Rust 1.75 x64 | dp | O(S₁ · S₂ · 9) | AC | 0.156 s | 9532 KB | 11308837 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1658_dp_optimized.cpp](1658_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(9C+TK) | AC | 0.046 s | 3292 KB | 11308098 |
| [1658_dp_optimized.go](1658_dp_optimized.go) | Go 1.14 x64 | dp | O(9C+TK) | AC | 0.062 s | 4488 KB | 11308100 |
| [1658_dp_optimized.java](1658_dp_optimized.java) | Java 1.8 | dp | O(9C+TK) | AC | 0.156 s | 9148 KB | 11308105 |
| [1658_bitmask_dp.py](1658_bitmask_dp.py) \* | Python 3.12 x64 | bitmask, dp | O(9C+TK) | AC | 1.031 s | 12680 KB | 11308153 |
| [1658_dp_optimized.rs](1658_dp_optimized.rs) | Rust 1.75 x64 | dp | O(9C+TK) | AC | 0.031 s | 2800 KB | 11308108 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
