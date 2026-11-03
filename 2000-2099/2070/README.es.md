# 2070. Potencias de primos con un número primo de divisores

[Timus 2070](https://acm.timus.ru/problem.aspx?space=1&num=2070) · dificultad 235 · number_theory

Problema original de Alexey Danilyuk, del Concurso Regional de Programación por Equipos de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una persona considera interesante un entero si es primo, y otra si su
número de divisores positivos es primo. Un entero es satisfactorio si
ambas coinciden, en un sentido o en el otro. Contar los enteros
satisfactorios de [L; R]. Los límites son 2 segundos y 64 MB.

## Entrada

L y R, 2 ≤ L ≤ R ≤ 10¹².

## Salida

El número de enteros satisfactorios de [L; R].

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 7
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
2 2
```

Salida:

```
1
```

### Ejemplo 3

Entrada:

```
77 1010
```

Salida:

```
924
```

## Solución

Un primo tiene 2 divisores, y 2 es primo, así que ambas consideran
interesante todo primo. Un número compuesto es satisfactorio salvo que
su número de divisores sea primo. Para x = p₁^a₁ · … · pₛ^aₛ ese número
es (a₁ + 1) · … · (aₛ + 1), y un producto es primo solo si tiene un único
factor. Por tanto los números no satisfactorios son exactamente las
potencias p^k de un primo con k ≥ 2 y k + 1 primo, y la respuesta es
R − L + 1 menos su cantidad en [L; R].

Como p^k ≤ 10¹² con k ≥ 2, todo p así es a lo sumo 10⁶. Una criba hasta
10⁶ da los primos, y para cada primo p con p² ≤ R se recorren las
potencias p², p³, … hasta R, contando las que son al menos L y cuyo
exponente más uno es primo. Los primos mayores que 10⁴ solo tienen el
cuadrado, así que el recorrido es corto; el trabajo lo domina la criba,
O(N log log N) con N = 10⁶.

En el primer ejemplo 4 = 2² tiene 3 divisores, así que es el único no
satisfactorio entre 3 … 7 y la respuesta es 4.

## Soluciones optimizadas

Se separan cuadrados de primos de las demás potencias pares válidas. Una DP de conteo de primos sobre los cocientes enteros distintos cuenta hasta la raíz cuadrada requerida. Solo las potencias mayores necesitan una criba explícita, con bases primas hasta la raíz cuarta. Se cuentan exponentes como en la prueba simple y se restan conteos de prefijos para el intervalo. Las raíces se corrigen con enteros para evitar errores de frontera flotantes.

R es el extremo derecho, M=floor(sqrt(R)) y P los primos pequeños para potencias mayores. Estas potencias son números excluidos: su cantidad se resta de la longitud del intervalo.

- `2070_number_theory_dp.cpp`: 0.015 s / 172 KB; base `2070_number_theory.cpp`: 0.015 s / 284 KB; cambio respecto a la base: tiempo -0.0%, memoria -39.4%.
- `2070_number_theory_dp.go`: 0.031 s / 1116 KB; base `2070_number_theory.go`: 0.031 s / 2136 KB; cambio respecto a la base: tiempo -0.0%, memoria -47.8%.
- `2070_number_theory_dp.java`: 0.125 s / 492 KB; base `2070_number_theory.java`: 0.140 s / 2584 KB; cambio respecto a la base: tiempo -10.7%, memoria -81.0%.
- `2070_number_theory_dp.py`: 0.093 s / 940 KB; base `2070_number_theory.py`: 0.109 s / 2772 KB; cambio respecto a la base: tiempo -14.7%, memoria -66.1%.
- `2070_number_theory_dp.rs`: 0.046 s / 228 KB; base `2070_number_theory.rs`: 0.046 s / 1200 KB; cambio respecto a la base: tiempo -0.0%, memoria -81.0%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `2070_number_theory.cpp`; versión que cubre `2070_number_theory.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 76/76.

- Go: base didáctica preferida `2070_number_theory.go`; versión que cubre `2070_number_theory.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `2070_number_theory.java`; versión que cubre `2070_number_theory.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `2070_number_theory.py`; versión que cubre `2070_number_theory.py`; puestos tiempo/memoria 1/1, registros de otros autores 13/13.

- Rust: base didáctica preferida `2070_number_theory.rs`; versión que cubre `2070_number_theory.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2070_number_theory.cpp](2070_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.015 s | 284 KB | 11309222 |
| [2070_number_theory.go](2070_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.031 s | 2136 KB | 11294446 |
| [2070_number_theory.java](2070_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.140 s | 2584 KB | 11309223 |
| [2070_number_theory.py](2070_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.109 s | 2772 KB | 11309224 |
| [2070_number_theory.rs](2070_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.046 s | 1200 KB | 11309225 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2070_number_theory_dp.cpp](2070_number_theory_dp.cpp) | G++ 13.2 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.015 s | 172 KB | 11308159 |
| [2070_number_theory_dp.go](2070_number_theory_dp.go) | Go 1.14 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.031 s | 1116 KB | 11308162 |
| [2070_number_theory_dp.java](2070_number_theory_dp.java) | Java 1.8 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.125 s | 492 KB | 11308164 |
| [2070_number_theory_dp.py](2070_number_theory_dp.py) | Python 3.12 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.093 s | 940 KB | 11308156 |
| [2070_number_theory_dp.rs](2070_number_theory_dp.rs) | Rust 1.75 x64 | number_theory, dp | O(M^(3/4)+P log R) | AC | 0.046 s | 228 KB | 11308166 |
