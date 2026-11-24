# 1640. Anillo de frío

[Timus 1640](https://acm.timus.ru/problem.aspx?space=1&num=1640) · dificultad 178 · geometry

Problema original de Dmitry Ivankov (preparado por Alexander Ipatov), del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay demonios en n puntos de la red. Sandro puede teletransportarse a
cualquier punto sin demonio y lanzar ahí un anillo de hielo de radio a
lo sumo 10000 centrado en él. El anillo debe matar al menos a un demonio
(uno sobre la circunferencia), y todos los demonios que sigan vivos deben
quedar dentro. Hay que dar un centro y un radio.

## Entrada

n (1 ≤ n ≤ 100) y luego las coordenadas de los demonios, enteros de
valor absoluto hasta 1000, medidas desde la posición actual de Sandro.
Todos los demonios están en puntos distintos y ninguno en el de Sandro.

## Salida

El centro y el radio con precisión 10⁻⁹. Se acepta cualquier respuesta
válida.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador del repositorio exige exactamente tres números finitos x,y,r, con 0<=r<=10000+1e-6. El centro debe distar al menos 1e-6 de cada demonio, todos deben quedar a distancia no mayor que r+1e-6 y alguna distancia debe diferir de r a lo sumo 1e-6. Esta es la tolerancia del repositorio; el enunciado solicita por separado precisión de 1e-9.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
1 1
1 5
3 6
5 3
8 0
9 5
5 9
```

Salida:

```
5 4 5
```

### Ejemplo 2

Entrada:

```
2
0 2
2 0
```

Salida:

```
1 1 1.41421356237309
```

## Solución

No hace falta teletransportarse. La posición de Sandro no tiene demonio,
y la circunferencia a su alrededor que pasa por el demonio más lejano lo
mata y encierra a todos los demás. Su radio es a lo sumo 1000 · √2, muy
por debajo de 10000. `O(n)`.

Detalles a tener en cuenta:

- el centro no puede ser el punto de un demonio, así que el centro del
  menor círculo envolvente no siempre vale; el punto de partida siempre;
- hay muchas respuestas válidas, así que un verificador acepta cualquier
  circunferencia que cumpla las reglas.

## Soluciones optimizadas

La solución optimizada en Java imprime la misma circunferencia, pero lee
los números a mano desde bloques de bytes de 4 KB en lugar de con
`Scanner`, cuyas expresiones regulares cuestan tiempo y memoria de
preparar: {1640_geometry_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1640_geometry_optimized.java`: reducción de tiempo +33.57%; reducción
  de memoria +54.92%; base: `1640_geometry.java`.

`1640_geometry_optimized.rs`. Conserva el círculo centrado en el origen, garantizado libre de demonios. Lee cada par entero y mantiene max(x*x+y*y) exactamente en i64; calcula una sola raíz al final en vez de hypot por punto. Las coordenadas de valor absoluto hasta 1000 acotan los cuadrados con seguridad. Emite el radio con diez decimales. Tiempo O(n), estado auxiliar O(1), sin un vector de todos los datos flotantes. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1640_geometry.rs`: tiempo 0.062 s → 0.031 s; memoria 268 KB → 96 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1640_geometry_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1640_geometry.cpp](1640_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 148 KB | 11288466 |
| [1640_geometry.go](1640_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.015 s | 1112 KB | 11288467 |
| [1640_geometry.java](1640_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 2032 KB | 11288469 |
| [1640_geometry.py](1640_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 488 KB | 11288468 |
| [1640_geometry.rs](1640_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.062 s | 268 KB | 11304017 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1640_geometry_optimized.java](1640_geometry_optimized.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 916 KB | 11307283 |
| [1640_geometry_optimized.rs](1640_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 96 KB | 11325103 |
