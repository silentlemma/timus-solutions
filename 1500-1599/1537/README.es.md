# 1537. Ents

[Timus 1537](https://acm.timus.ru/problem.aspx?space=1&num=1537) · dificultad 283 · dp

Problema original de Sergey Pupyrev, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El primer ent aprende dos palabras. Cada ent que ha aprendido w
palabras se las enseña a un ent viejo y a uno joven que aún no hablan;
después los elfos enseñan al viejo una palabra más, con lo que termina
con w + 1, y al joven w más, con lo que termina con 2w. Esto sigue sin
fin. Hay que contar los ents que saben exactamente K palabras, módulo P
(K ≤ 10⁷, P ≤ 10⁹).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K y P.

## Salida

El número de ents que saben exactamente K palabras, módulo P.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 10
```

Salida:

```
2
```

## Solución

Sea f(w) el número de ents que saben w palabras. Cada ent salvo el
primero tuvo un único maestro, como alumno viejo (w − 1 palabras) o
joven (w / 2 palabras, solo para w par), así que f(2) = 1 y
f(w) = f(w − 1) + f(w / 2) para w par, f(w) = f(w − 1) para w impar. Un
w impar no añade nada, de modo que g(m) = f(2m) = f(2m + 1) cumple
g(1) = 1 y g(m) = g(m − 1) + g(⌊m / 2⌋), y la respuesta es g(⌊K / 2⌋),
o 0 para K = 1. Si B(n) cuenta las particiones de n en potencias de dos,
entonces g(m) = B(2m) / 2 para m ≥ 1. Estos recuentos crecen demasiado
para guardarlos exactos, así que la recurrencia se evalúa módulo P.

Basta una pasada por m hasta K / 2 = 5·10⁶; solo se vuelven a consultar
los valores hasta K / 4, así que solo se guardan esos (un arreglo de
2,5·10⁶ números). La suma de dos restos es como máximo
2(P − 1) ≤ 1.999.999.998 y cabe en un entero de 32 bits con signo;
las soluciones compiladas usan sumas de 64 bits. Tiempo `O(K)` y espacio `O(K)`.

Detalles a tener en cuenta:

- K = 1: nadie sabe una sola palabra (prueba 02);
- P = 1 hace que toda respuesta sea 0 (prueba 04);
- hay que reducir cada suma módulo P: los recuentos exactos superan los
  enteros de tamaño fijo, aunque la suma de dos restos cabe en 32 bits
  (pruebas 06, 07);
- g(m) es la mitad de B(2m): para K = 4 la respuesta es 2, pero B(4) = 4
  (prueba 01);
- Python se ejecuta con PyPy: K = 10⁷ tarda unos 0,8 s con CPython y
  unos 0,17 s con PyPy.

## Soluciones optimizadas

`1537_dp_optimized.go`. Conserva g(m)=g(m-1)+g(floor(m/2)) módulo P. A diferencia del Python retenido que suma algebraicamente el tramo final, Go y Rust visitan todo m hasta T=floor(K/2). Un anillo de floor(floor(T/2)/2)+1 residuos de 32 bits sustituye el prefijo completo. g(j) se lee por última vez en 2j+1 y la celda se reutiliza después. Reduce aproximadamente a la mitad la memoria del DP, manteniendo tiempo O(K) y espacio asintótico O(K). P<=10^9 permite residuos de 32 bits; suma en 64 bits. Conserva K<2 y P=1.

Frente a `1537_dp.go`: tiempo 0.109 s → 0.093 s; memoria 11700 KB → 6 320 KB.

`1537_dp_optimized.rs`. Conserva g(m)=g(m-1)+g(floor(m/2)) módulo P. A diferencia del Python retenido que suma algebraicamente el tramo final, Go y Rust visitan todo m hasta T=floor(K/2). Un anillo de floor(floor(T/2)/2)+1 residuos de 32 bits sustituye el prefijo completo. g(j) se lee por última vez en 2j+1 y la celda se reutiliza después. Reduce aproximadamente a la mitad la memoria del DP, manteniendo tiempo O(K) y espacio asintótico O(K). P<=10^9 permite residuos de 32 bits; suma en 64 bits. Conserva K<2 y P=1.

Frente a `1537_dp.rs`: tiempo 0.046 s → 0.015 s; memoria 9836 KB → 4 792 KB.

Se usa la misma recurrencia, sumando algebraicamente el intervalo final en vez de calcular cada estado restante. Basta calcular un prefijo anterior y conservar una parte inicial aún menor. Los residuos empaquetados de 32 bits reemplazan celdas de 64 bits, permitidos por la cota del módulo. Las fórmulas de extremos pares e impares mantienen los casos base. La versión aceptada usa CPython y se compara con el intérprete real de la versión simple conservada.

```text
T = floor(K/2), H = floor(T/2), D = floor(H/2)
g(0) = 0, g(1) = 1
S = sum(g(j), D < j <= H)
For H >= 1:
  g(2H) = 2S + [H is even] * g(D)
  g(2H+1) = g(2H) + g(H)
answer = g(T) mod P
```

- `1537_dp_optimized.py`: 0.656 s / 5276 KB; base `1537_dp.py`: 0.203 s / 20812 KB; cambio respecto a la base: tiempo +223.2%, memoria -74.6%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1537_dp_optimized.go`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

`1537_dp_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1537_dp.cpp](1537_dp.cpp) | G++ 13.2 x64 | dp | O(K) | AC | 0.046 s | 9684 KB | 11287481 |
| [1537_dp.go](1537_dp.go) | Go 1.14 x64 | dp | O(K) | AC | 0.109 s | 11700 KB | 11287482 |
| [1537_dp.java](1537_dp.java) | Java 1.8 | dp | O(K) | AC | 0.140 s | 11368 KB | 11287485 |
| [1537_dp.py](1537_dp.py) | PyPy 3.10 x64 | dp | O(K) | AC | 0.203 s | 20812 KB | 11287484 |
| [1537_dp.rs](1537_dp.rs) | Rust 1.75 x64 | dp | O(K) | AC | 0.046 s | 9836 KB | 11287488 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1537_dp_optimized.py](1537_dp_optimized.py) \* | Python 3.12 x64 | dp | O(K) | AC | 0.656 s | 5276 KB | 11309315 |
| [1537_dp_optimized.go](1537_dp_optimized.go) \* | Go 1.14 x64 | dp | O(K) | AC | 0.093 s | 6320 KB | 11325049 |
| [1537_dp_optimized.rs](1537_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(K) | AC | 0.015 s | 4792 KB | 11325101 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
