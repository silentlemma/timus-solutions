# 1748. El número más complejo

[Timus 1748](https://acm.timus.ru/problem.aspx?space=1&num=1748) · dificultad 268 · number_theory

Problema original de Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La complejidad de un número es su número de divisores. Para cada n
dado, hallar el número más complejo de 1 a n, el menor si hay empate, y
su complejidad.

## Entrada

t (1 ≤ t ≤ 100) y luego t números n (1 ≤ n ≤ 10¹⁸).

## Salida

Para cada n, el número y su número de divisores.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1
10
100
1000
10000
```

Salida:

```
1 1
6 4
60 12
840 32
7560 64
```

## Solución

El número de divisores de p₁^a₁ · p₂^a₂ · … es (a₁ + 1)(a₂ + 1)…, que
solo depende de los exponentes. Poner los exponentes mayores en los
primos menores da el menor número con esos exponentes, así que la
respuesta siempre es de la forma 2^a · 3^b · 5^c · … con a ≥ b ≥ c ≥ …
en primos consecutivos. Hasta 10¹⁸ hay solo unas decenas de miles de
números así, y los primos necesarios terminan antes de 53, pues
2 · 3 · … · 53 ya pasa de 10¹⁸.

Se listan todos con una búsqueda sobre los exponentes, se ordenan y se
recorren hacia arriba guardando el mejor hasta el momento: un número
sustituye al mejor solo con estrictamente más divisores, lo que deja el
menor en los empates. Cada consulta es entonces una búsqueda binaria
del último número de la lista que no pasa de n.
`O(K log K + t log K)` para los K = 32 749 números listados.

Para n = 100 la respuesta es 60 = 2² · 3 · 5 con 3 · 2 · 2 = 12
divisores.

Trampas:

- multiplicar cerca de 10¹⁸ puede desbordar 64 bits; comprobar el
  límite dividiendo antes de multiplicar;
- en un empate gana el número menor: 2 y 3 tienen dos divisores.

Las respuestas coinciden con una criba de números de divisores en 100
consultas aleatorias hasta 20 000, y con una implementación aceptada
independiente en 30 pruebas aleatorias hasta 10¹⁸ y alrededor de los
números récord.

## Soluciones optimizadas

Se enumeran exponentes primos no crecientes hasta la mayor cota consultada. Se mantiene la frontera no dominada por valor, con cantidades de divisores estrictamente crecientes. Si el predecesor tiene al menos tantos divisores, el candidato es inútil; si no, se eliminan registros posteriores con cantidad no mayor. Se conservan todos los óptimos y el menor valor en empates. Las consultas buscan en la frontera compacta, sin ordenar todos los candidatos ni duplicar prefijos óptimos.

C cuenta candidatos de exponentes, R el tamaño máximo de frontera y T las consultas; insertar puede desplazar R registros.

- `1748_number_theory_optimized.cpp`: 0.015 s / 168 KB; base `1748_number_theory.cpp`: 0.015 s / 1904 KB; cambio respecto a la base: tiempo -0.0%, memoria -91.2%.
- `1748_number_theory_optimized.go`: 0.031 s / 1136 KB; base `1748_number_theory.go`: 0.031 s / 5404 KB; cambio respecto a la base: tiempo -0.0%, memoria -79.0%.
- `1748_number_theory_optimized.java`: 0.109 s / 488 KB; base `1748_number_theory.java`: 0.187 s / 8084 KB; cambio respecto a la base: tiempo -41.7%, memoria -94.0%.
- `1748_number_theory_optimized.py`: 0.093 s / 536 KB; base `1748_number_theory.py`: 0.187 s / 6476 KB; cambio respecto a la base: tiempo -50.3%, memoria -91.7%.
- `1748_number_theory_optimized.rs`: 0.031 s / 224 KB; base `1748_number_theory.rs`: 0.031 s / 1368 KB; cambio respecto a la base: tiempo -0.0%, memoria -83.6%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1748_number_theory.cpp`; versión que cubre `1748_number_theory_optimized.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 71/71.

- Go: base didáctica preferida `1748_number_theory.go`; versión que cubre `1748_number_theory.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1748_number_theory.java`; versión que cubre `1748_number_theory_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1748_number_theory.py`; versión que cubre `1748_number_theory_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 8/8.

- Rust: base didáctica preferida `1748_number_theory.rs`; versión que cubre `1748_number_theory.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1748_number_theory.cpp](1748_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log K + t log K) | AC | 0.015 s | 1904 KB | 11308921 |
| [1748_number_theory.go](1748_number_theory.go) | Go 1.14 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 5404 KB | 11289533 |
| [1748_number_theory.java](1748_number_theory.java) | Java 1.8 | number_theory | O(K log K + t log K) | AC | 0.187 s | 8084 KB | 11289536 |
| [1748_number_theory.py](1748_number_theory.py) | Python 3.12 x64 | number_theory | O(K log K + t log K) | AC | 0.187 s | 6476 KB | 11308922 |
| [1748_number_theory.rs](1748_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 1368 KB | 11289537 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1748_number_theory_optimized.cpp](1748_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(CR+T log R) | AC | 0.015 s | 168 KB | 11309275 |
| [1748_number_theory_optimized.go](1748_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(CR+T log R) | AC | 0.031 s | 1136 KB | 11309278 |
| [1748_number_theory_optimized.java](1748_number_theory_optimized.java) | Java 1.8 | number_theory | O(CR+T log R) | AC | 0.109 s | 488 KB | 11309276 |
| [1748_number_theory_optimized.py](1748_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(CR+T log R) | AC | 0.093 s | 536 KB | 11309274 |
| [1748_number_theory_optimized.rs](1748_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(CR+T log R) | AC | 0.031 s | 224 KB | 11309279 |
