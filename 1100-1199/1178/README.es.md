# 1178. Emparejar ciudades con carreteras rectas que no se crucen

[Timus 1178](https://acm.timus.ru/problem.aspx?space=1&num=1178) · dificultad 151 · geometry

Problema original de Pavel Atnashev, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay un número par `N ≤ 10000` de ciudades en puntos enteros con
coordenadas de hasta `10⁹` en valor absoluto, sin tres en una misma
recta. Hay que unirlas por parejas con carreteras rectas, cada ciudad en
exactamente una carretera, sin que dos carreteras se crucen.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas, cada una con las dos coordenadas de una ciudad.

## Salida

`N/2` líneas, cada una con los números de las dos ciudades que une una
carretera.

## Evaluación

Se acepta cualquier plan que empareje cada ciudad exactamente una vez y en
el que dos carreteras nunca se toquen; el comprobador compara las
carreteras cuyos rangos de `x` se solapan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 2
1 1
3 4
4 4
```

Salida:

```
1 3
2 4
```

## Solución

Se ordenan las ciudades por `x` y se une la primera con la segunda, la
tercera con la cuarta, y así sucesivamente. Cada carretera queda en su
propia franja vertical entre las `x` de sus extremos, y las franjas de
carreteras distintas se solapan como mucho en una recta de borde. En esa
recta cada carretera solo tiene un extremo, y esos extremos son ciudades
distintas, así que ahí no se tocan. Una carretera puede ser vertical si
sus dos ciudades comparten `x`, pero entonces no hay otra ciudad en esa
recta, pues no hay tres ciudades alineadas. Así que dos carreteras nunca
se tocan. `O(N log N)`.

Detalles a tener en cuenta:

- los empates en `x` no necesitan cuidado especial, aunque las soluciones
  los ordenan por `y` para que la salida sea reproducible;
- las coordenadas llegan a `10⁹` y caben en enteros de 32 bits;
  la solución solo las compara.

Cada plan impreso pasó el comprobador en todas las pruebas, incluidas diez
mil ciudades sobre cónicas con muchos valores de `x` compartidos.

## Soluciones optimizadas

La solución optimizada en Java analiza los números a mano desde un búfer
de 4 KB en lugar de juntar todas las líneas en una cadena para un
`StringTokenizer`, y ordena un arreglo simple de `long` en lugar de
números `Integer` con un comparador. Cada clave es `x + 10⁹`, como mucho
2·10⁹ y por tanto 31 bits, desplazado encima del índice de ciudad de
14 bits (menor que 10000 < 2¹⁴). En la clave solo está `x`: como no hay
tres ciudades en una recta, como mucho dos comparten una `x`, y una
pasada posterior intercambia ese par vecino cuando sus `y` están en mal
orden: {1178_geometry_optimized.java}.

La solución optimizada en Python aprovecha que cada ciudad va en su
propia línea y lee las líneas una a una en lugar de partir toda la
entrada. Empaqueta cada ciudad en un solo entero, `x + 10⁹` e `y + 10⁹`
de 31 bits cada uno encima del número de ciudad de 14 bits, así que un
`sort` simple ordena las ciudades por `(x, y)` sin función clave ni
tuplas, y escribe los pares sobre la marcha en lugar de reunir una lista
de líneas: {1178_geometry_optimized.py}.

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB en lugar de leer toda la entrada en un `String` y un vector con
todos los números. Ordena tuplas `(x, y, número)` de `i32`, suficientes
para coordenadas de hasta `10⁹` en valor absoluto, con `sort_unstable`,
que no necesita búfer adicional, y escribe a través de un `BufWriter`:
{1178_geometry_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1178_geometry_optimized.java`: reducción de tiempo +33.57%; reducción
  de memoria +85.16%; base: `1178_geometry.java`.

- `1178_geometry_optimized.py`: reducción de tiempo +0.00%; reducción de
  memoria +66.30%; base: `1178_geometry.py`.

- `1178_geometry_optimized.rs`: reducción de tiempo -106.67%; reducción
  de memoria +61.78%; base: `1178_geometry.rs`.

## Notas por lenguaje

- Todos los lenguajes ordenan las ciudades por `x` y, a igual `x`, por
  `y`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1178_geometry.cpp](1178_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 388 KB | 11283266 |
| [1178_geometry.go](1178_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1676 KB | 11283270 |
| [1178_geometry.java](1178_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 6872 KB | 11283277 |
| [1178_geometry.py](1178_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 3276 KB | 11283275 |
| [1178_geometry.rs](1178_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 764 KB | 11283279 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1178_geometry_optimized.java](1178_geometry_optimized.java) | Java 1.8 | geometry | O(N log N) | AC | 0.093 s | 1020 KB | 11305836 |
| [1178_geometry_optimized.py](1178_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 1104 KB | 11305838 |
| [1178_geometry_optimized.rs](1178_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 292 KB | 11305833 |
