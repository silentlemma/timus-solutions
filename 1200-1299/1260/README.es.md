# 1260. El fotógrafo quisquilloso

[Timus 1260](https://acm.timus.ru/problem.aspx?space=1&num=1260) · dificultad 112 · dp

Problema original de Alexander Ipatov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N estudiantes de 1, 2, …, N años (1 ≤ N ≤ 55) se sientan en fila. Quien
tiene 1 año se sienta en el extremo izquierdo, y las edades de dos
vecinos cualesquiera difieren como mucho en 2. ¿Cuántas filas así hay?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El número de filas.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
4
```

## Solución

Sea a(k) el número de filas para las edades 1..k. Se mira quién se
sienta en segundo lugar:

- la edad 2: el resto es una fila de 2..k que empieza en 2, el mismo
  problema desplazado en uno, a(k − 1) formas;
- la edad 3 y luego la 2: después debe ir el 4, y el resto es una fila
  de 4..k que empieza en 4, a(k − 3) formas;
- la edad 3, pero el 2 más tarde: los vecinos del 2 solo pueden ser 1, 3
  y 4, y 1 y 3 ya están juntos, así que el 2 va en el extremo derecho
  junto al 4. Esto obliga al zigzag 1, 3, 5, … subiendo por las edades
  impares y bajando por las pares hasta 4, 2: exactamente una fila.

Así, a(k) = a(k − 1) + a(k − 3) + 1, con a(1) = a(2) = 1 y a(3) = 2.
Aplicar la regla hacia atrás da a(0) = 0 y a(−1) = −1, lo que permite
empezar el bucle en k = 1 sin casos especiales. a(55) = 1 388 937 263
aún cabe en 32 bits, pero C++, Go, Java y Rust usan enteros de 64 bits,
y Python, sus enteros de precisión arbitraria. `O(N)`.

Detalles a tener en cuenta:

- el tercer caso es fácil de olvidar: para N = 5 es la fila
  1, 3, 5, 4, 2 (prueba 05);
- con N = 1 y N = 2 hay una sola fila (pruebas 02, 03).

La recurrencia se comparó con listar todas las permutaciones para N
hasta 10.

## Soluciones optimizadas

`1260_dp_optimized.java`. Java conserva la misma recurrencia y tres contadores long: desde (-1,0,1), cada paso los sustituye por (old,current,current+older+1). Para N de 1 a 55 realiza como máximo 54 pasos: tiempo O(N) y espacio auxiliar O(1). Búferes fijos de entrada y salida de 1024 bytes y un auxiliar de 20 dígitos sustituyen la lectura carácter a carácter y el formato numérico general. Cada N permitido se comparó con una recurrencia independiente en un arreglo; la enumeración de permutaciones pequeñas comprueba además la interpretación del conteo.

Accepted exacto Java 1.8 #11327453: 0.093 s / 340 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 9/96, memoria 4/96. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11304342 era 0.109 s / 320 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1260_dp_optimized.java`: 0.093 s / 340 KB; base didáctica conservada `1260_dp.java`: 0.093 s / 1568 KB.

`1260_dp_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327021 mide 0.078 s / 564 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 6/44, memoria 26/44. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11324915, 0.125 s / 200 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

`1260_dp_optimized.py`. Mantiene a(k)=a(k-1)+a(k-3)+1 y el estado inicial (-1,0,1). Conserva tres acumuladores sin otra tabla, avanzando simultáneamente los valores previos. Tiempo O(N), tres enteros acotados. Para N<=55 las cuentas caben en64 bits con signo; basta a(N)<2^N. Lee un token de bytes y ejecuta la recurrencia sin llamada envolvente. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1260_dp.py`: tiempo 0.109 s → 0.125 s; memoria 404 KB → 200 KB.

`1260_dp_optimized.rs`. Mantiene a(k)=a(k-1)+a(k-3)+1 y el estado inicial (-1,0,1). Conserva tres acumuladores sin otra tabla, avanzando simultáneamente los valores previos. Tiempo O(N), tres enteros acotados. Para N<=55 las cuentas caben en64 bits con signo; basta a(N)<2^N. Mantiene acumuladores i64 y salida numérica directa, sin entrada decodificada ni formato Rust. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1260_dp.rs`: tiempo 0.015 s → 0.031 s; memoria 232 KB → 56 KB.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Comparación PyPy anterior: `1260_dp_optimized.py`: puesto de tiempo 37/44 y de memoria 1/44 en esta muestra comparable.

`1260_dp_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1260_dp.cpp](1260_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11284122 |
| [1260_dp.go](1260_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.046 s | 1076 KB | 11284124 |
| [1260_dp.java](1260_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 1568 KB | 11284130 |
| [1260_dp.py](1260_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.109 s | 404 KB | 11284128 |
| [1260_dp.rs](1260_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 232 KB | 11284131 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1260_dp_optimized.java](1260_dp_optimized.java) \* | Java 1.8 | dp | O(N) time; O(1) auxiliary space | AC | 0.093 s | 340 KB | 11327453 |
| [1260_dp_optimized.py](1260_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N) | AC | 0.078 s | 564 KB | 11327021 |
| [1260_dp_optimized.rs](1260_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 56 KB | 11325091 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
