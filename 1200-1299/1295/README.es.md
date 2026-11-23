# 1295. Delirio

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · dificultad 151 · number_theory

Problema original de Den Raskovalov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

¿En cuántos ceros termina el número decimal 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ, para
1 ≤ n ≤ 300 000?

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

La cantidad de ceros finales.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
3
```

Salida:

```
2
```

## Solución

Para el mayor n la suma tiene más de 180 000 cifras, pero sus ceros
finales están limitados por la potencia de 2 que contiene. Sea
S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ.

- n = 1: S = 10, un cero.
- n par: 1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4), y 2ⁿ, 4ⁿ son múltiplos de 4, así
  que S es divisible por 2 pero no por 4.
- n impar, n ≥ 3: 3ⁿ ≡ 3 (mod 8), luego 1ⁿ + 3ⁿ ≡ 4 (mod 8), mientras
  que 2ⁿ y 4ⁿ son múltiplos de 8; S es divisible por 4 pero no por 8.

Así que S nunca termina en tres ceros, y S mod 100 lo decide todo: dos
ceros si vale 0, un cero si termina en 0 y ninguno en otro caso. Las
cuatro potencias módulo 100 salen de la exponenciación rápida.
`O(log n)`.

De hecho la respuesta solo depende de n mod 20: 0 cuando 4 divide a n,
2 cuando n deja resto 3 módulo 4 o 5 módulo 20, y 1 en los demás
casos. Las soluciones la calculan directamente sin apoyarse en esta
tabla.

Detalles a tener en cuenta:

- un n con resto 1 módulo 4 suele dar un cero, pero n = 5, 25, … dan
  dos (pruebas 05 y 06);
- la suma completa se puede construir con enteros grandes, pero nunca
  hace falta: solo importan sus dos últimas cifras.

Los resultados se compararon con la suma exacta en enteros grandes para
todos los n hasta 3000.

## Soluciones optimizadas

`1295_math.java`. Una fórmula de congruencias sustituye potencias modulares: n divisible por 4 da cero ceros finales; n mod 4=3 o n mod 20=5 da dos; los demás uno. Módulo 5 decide existencia, expansión impar módulo 25 el segundo, módulo 8 excluye tercero; n=1 da 10 aparte. Sin tabla de respuestas. Aritmética y espacio O(1), más lectura decimal. Algoritmo distinto llamado math; conserva potencia modular y enseñanza. Fórmula real contrastada para todo n=1..300000 con potencias independientes.

Fuente exacto: Java 1.8 Accepted #11327403: 0.078 s / 340 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 2/67; 2/67. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11305839 (Java 1.8): 0.109 s / 324 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1295_math.java`: 0.078 s / 340 KB; base didáctica conservada `1295_number_theory.java` (Java 1.8): 0.125 s / 1600 KB.

`1295_number_theory_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327024 mide 0.062 s / 660 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 1/57, memoria 30/57. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11325070, 0.125 s / 200 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

La solución optimizada en Java analiza `n` a mano desde un búfer de 4 KB
que se llena desde `System.in`, en lugar de crear un `Scanner`, así que
la JVM no carga el escáner ni sus expresiones regulares; las potencias
módulo 100 son las mismas: {1295_number_theory_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1295_number_theory_optimized.java`: reducción de tiempo +12.80%;
  reducción de memoria +79.75%; base: `1295_number_theory.java`.

`1295_number_theory_optimized.py`. Conserva el argumento módulo 100 para los ceros finales. Calcula directamente 1+pow(2,n,100)+pow(3,n,100)+pow(4,n,100), sin generador sobre cuatro bases. Las potencias modulares no construyen valores enormes. La cota demostrada de dos ceros hace que resto cero dé dos, divisibilidad por diez dé uno y lo demás cero. Tiempo O(log n) operaciones modulares acotadas y estado O(1). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1295_number_theory.py`: tiempo 0.093 s → 0.125 s; memoria 464 KB → 200 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1295_number_theory_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328536 (Go 1.14 x64): **0.031 s / 936 KB**. Comparación archivada: `1295_number_theory.go` (Go 1.14 x64) — 0.031 s / 1080 KB (#11284638).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Comparación PyPy anterior: `1295_number_theory_optimized.py`: puesto de tiempo 37/57 y de memoria 1/57 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB | 11284634 |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB | 11284638 |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB | 11284648 |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB | 11284644 |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB | 11284651 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory_optimized.java](1295_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(log n) | AC | 0.109 s | 324 KB | 11305839 |
| [1295_math.java](1295_math.java) | Java 1.8 | math | O(1) arithmetic/storage + decimal input | AC | 0.078 s | 340 KB | 11327403 |
| [1295_number_theory_optimized.py](1295_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.062 s | 660 KB | 11327024 |
| [1295_number_theory_optimized.go](1295_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 936 KB | 11328536 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
