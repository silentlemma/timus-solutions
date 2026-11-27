# 1157. Las menos baldosas que forman N rectángulos, cuando K baldosas menos formaban M

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · dificultad 200 · number_theory

Problema original del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un niño coloca todas sus baldosas cuadradas en forma de rectángulo. Dados
`M`, `N` y `K` (`1 ≤ M, N ≤ 50`, `1 ≤ K ≤ 9999`), halla el menor número de
baldosas `L` tal que con `L` baldosas se formen exactamente `N`
rectángulos distintos y con `L − K` baldosas exactamente `M`. Imprime `0`
si no hay tal `L` hasta 10000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Enteros M, N y K, con 1<=M,N<=50 y 1<=K<=9999.

## Salida

El menor `L`, o `0`.

## Evaluación

Comparación por tokens del único entero, ignorando espacios según
tests.json. La referencia es la criba C++ sencilla.

Se factorizaron independientemente todos los números de baldosas
`1..10000`, calculando divisores mediante exponentes primos para obtener
la tabla de formas de referencia; su máximo es 32. El candidato Python
real se comprobó con 125 consultas, incluido el ejemplo, cantidades sin
solución y `K = 9999`, buscando la primera coincidencia en esa tabla
independiente. Los cinco candidatos reales pasaron además 13 entradas
del repositorio cada uno en Docker. No es una prueba exhaustiva de todas
las ternas de entrada. Después los cinco obtuvieron su propio Accepted.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 1
```

Salida:

```
16
```

## Solución

Cada rectángulo de `x` baldosas corresponde a una pareja no ordenada
de divisores `a × b = x`, `a ≤ b`; girarlo no crea otra forma. Sea `d[x]`
el número de divisores. Emparejando cada divisor con su cociente obtenemos
`shapes[x] = (d[x] + 1) // 2`: en un cuadrado el divisor central se empareja
consigo mismo.

La criba sencilla incrementa `d[x]` en cada múltiplo de cada divisor
`1..B`, con `B = 10000`, contando cada divisor una vez. Recorremos `L`
en orden desde `K + 1` hasta `B` y comprobamos ambos números de formas.
La primera coincidencia es mínima; si no existe, imprimimos `0`.
Empezar en `K + 1` garantiza `L − K ≥ 1`. Esto demuestra el recuento y
la selección de la respuesta. Tiempo `O(B log B)`, espacio auxiliar `O(B)`.
Se conservan sin cambios las cinco fuentes Accepted originales. Python
materializa otra lista de formas; las bases nativas calculan la cantidad
de formas a partir de la tabla de divisores cuando la necesitan.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

Contamos directamente parejas no ordenadas de divisores. Para cada
lado menor `a = 1..floor(sqrt(B))`, incrementamos `a², a² + a, …, B`.
Son exactamente los productos `a × b` con `b ≥ a`. Cada rectángulo tiene
un único lado menor, de modo que se visita una vez; el cuadrado también
se cuenta una vez. La misma búsqueda creciente obtiene la misma respuesta.

Basta un byte por contador: para cualquier `x ≤ B` hay como máximo
`floor(sqrt(x)) ≤ 100` lados menores posibles. Ni siquiera el `byte`
con signo de Java puede desbordarse. La tabla ocupa `10001` bytes, sin
contar cabecera, E/S ni entorno de ejecución. Tiempo `O(B log B)` y
espacio `O(B)`, con menos incrementos y almacenamiento compacto. Java
también sustituye `Scanner` por `StreamTokenizer`; Rust analiza tres
números sin recopilar un vector numérico. Son implementaciones distintas
del mismo enfoque de criba de parejas, de ahí el sufijo `_optimized`.

Esta sección de parejas corresponde a C++, Java, Python y Rust
optimizados. Go optimizado conserva la criba completa de divisores
de su base, contadores int y conversión a formas. Cambia lector de
tokens y búfer de salida reutilizable, no tabla byte ni enumeración
de parejas. Ambas cribas cuestan O(B log B) y O(B) palabras o bytes;
los lectores de entrada completa añaden I bytes retenidos.

Frente a la base del mismo lenguaje, la memoria de C++ baja de 216 a
120 KB (44,4%), Python de 712 a 428 KB (39,9%), Java de 1620 a 420 KB
(74,1%). C++ y Python mantienen el tiempo registrado; Java también mejora
0,125 → 0,078 s (37,6%). Rust mejora su tiempo registrado: 0,046 → 0,015 s
(67,4%); la memoria solo baja un 25,3%, 300 → 224 KB. Estas mediciones pertenecen a las revisiones Accepted anteriores.

El experimento Go anterior de parejas (0,015 s / 1076 KB) no se
publicó como ese fuente. Sí existe el Go optimizado actual: criba
completa y E/S rápida, Accepted #11328509, 0,031 s / 1040 KB. Se
conserva la base. Un solo tic no prueba una aceleración repetible.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1157_number_theory_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328509 (Go 1.14 x64): **0.031 s / 1040 KB**. Comparación archivada: `1157_number_theory.go` (Go 1.14 x64) — 0.031 s / 1172 KB (#11281331).

La revisión Go optimizada actual acerca el comentario al límite
y nombra el ancho intacto de 64 bits de strconv. Se
conservan algoritmo y todos los fuentes sencillos.

## Notas por lenguaje

La admisión actual usa los [criterios compartidos](../../RATING_CRITERIA.md),
no primer puesto ni mejora del 30% obsoletos. La caché ligada a
fuentes confirma tiempo bajo 1 MiB para ambos C++, ambos Python,
ambos Rust y Java optimizado. Rust amplía explícitamente a todos
los compiladores, con un rival Rust 1.58 elegible; no es muestra
vacía ni referencia pequeña de versión exacta. El recibo anterior
de Go optimizado cumple ambas métricas pequeñas con dos rivales
Go 1.14. Las bases Java/Go se conservan para enseñar aunque fallen
sus métricas. Las filas actuales no tienen estrellas; las conclusiones
corresponden a la evidencia guardada.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1157_number_theory.cpp](1157_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 216 KB | 11281313 |
| [1157_number_theory.go](1157_number_theory.go) | Go 1.14 x64 | number_theory | O(B log B) | AC | 0.031 s | 1172 KB | 11281331 |
| [1157_number_theory.java](1157_number_theory.java) | Java 1.8 | number_theory | O(B log B) | AC | 0.125 s | 1620 KB | 11281380 |
| [1157_number_theory.py](1157_number_theory.py) | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 712 KB | 11281359 |
| [1157_number_theory.rs](1157_number_theory.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.046 s | 300 KB | 11281448 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1157_number_theory_optimized.cpp](1157_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(B log B) | AC | 0.015 s | 120 KB | 11308304 |
| [1157_number_theory_optimized.java](1157_number_theory_optimized.java) | Java 1.8 | number_theory | O(B log B) | AC | 0.078 s | 420 KB | 11308317 |
| [1157_number_theory_optimized.py](1157_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(B log B) | AC | 0.078 s | 428 KB | 11308301 |
| [1157_number_theory_optimized.rs](1157_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(B log B) | AC | 0.015 s | 224 KB | 11308320 |
| [1157_number_theory_optimized.go](1157_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(B log B) | AC | 0.015 s | 1024 KB | 11331013 |
