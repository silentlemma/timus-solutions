# 1683. Nevera

[Timus 1683](https://acm.timus.ru/problem.aspx?space=1&num=1683) · dificultad 137 · greedy

Problema original de Stanislav Vasilyev, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tira de papel de 1 cm de ancho y n cm de largo se dobla hasta un
cuadrado de 1 × 1 cm con n capas. Cada doblez mide un número entero de
centímetros desde el extremo izquierdo y dobla esa parte hacia la
derecha, de modo que el extremo izquierdo se desplaza esa longitud.
Hallar el menor número de dobleces y las longitudes medidas.

## Entrada

n (1 ≤ n ≤ 10⁹).

## Salida

El número de dobleces y luego las longitudes medidas en orden. Se
acepta cualquier secuencia más corta.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador del repositorio exige la cuenta óptima de referencia y exactamente tantas longitudes enteras. Cada x cumple1<=x<=current-x y reduce current en x; al final la longitud es uno. Acepta cualquier secuencia mínima válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
```

Salida:

```
4
5 3 2 1
```

## Solución

Doblar x cm de una tira de longitud L solo es posible si la solapa cabe
sobre el resto, x ≤ L − x, y entonces queda una tira de
L − x ≥ ⌈L / 2⌉. Así que ningún doblez reduce la tira a menos de la
mitad redondeada hacia arriba, y doblar ⌊L / 2⌋ cada vez lo consigue
exactamente: el número de dobleces es el menor m con 2ᵐ ≥ n.
`O(log n)`.

Trampas:

- n = 1 no necesita dobleces: se imprime 0 y una lista vacía;
- el 5 3 2 1 del ejemplo es una de muchas respuestas, así que un
  verificador compara la cantidad y reproduce los dobleces.

El verificador reproduce cada doblez y compara la cantidad con la del
voraz.

## Soluciones optimizadas

`1683_greedy_optimized.java`. Conserva medias plegadas óptimas. Para 1≤N≤10^9, ceil(log2 N)=32−numberOfLeadingZeros(N−1); N=1 da cero. Longitudes int y hasta treinta valores caben en respuesta completa de 384 bytes. Codifica cifras in situ, escribe una vez y vacía antes de System.exit(0), sin construir strings ni salida long general. O(log N) plegados, espacio auxiliar acotado. Par actual 0.078 s/452 KB separado del viejo 0.093 s/452 KB; un tick no prueba mejora del 30%. Bases y evidencia de runtime Python intactas.

Accepted exacto Java 1.8 #11327867: 0.078 s / 452 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/62, memoria 5/62. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11304448 era 0.093 s / 452 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1683_greedy_optimized.java`: 0.078 s / 452 KB; base didáctica conservada `1683_greedy.java`: 0.125 s / 1664 KB.

`1683_greedy_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327033 mide 0.062 s / 620 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 1/21, memoria 21/21. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11324922, 0.125 s / 208 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

`1683_greedy_optimized.py`. Conserva doblar floor(length/2) desde la izquierda, dejando ceil(length/2). Ningún pliegue legal reduce más deprisa: el mínimo es ceil(log2 n), cero para n=1. Hace O(log n) pasos enteros acotados con n<=10^9. Calcula la cuenta con (n-1).bit_length() antes de generar longitudes. Aún guarda y une las cadenas de todos los pliegues: espacio de salida O(log n). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1683_greedy.py`: tiempo 0.125 s → 0.125 s; memoria 372 KB → 208 KB.

`1683_greedy_optimized.rs`. Conserva doblar floor(length/2) desde la izquierda, dejando ceil(length/2). Ningún pliegue legal reduce más deprisa: el mínimo es ceil(log2 n), cero para n=1. Hace O(log n) pasos enteros acotados con n<=10^9. Una pasada cuenta y otra repite los mismos pasos al emitir longitudes, sin Vec<String> ni salida unida: estado auxiliar O(1), dos pasadas O(log n). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1683_greedy.rs`: tiempo 0.015 s → 0.062 s; memoria 244 KB → 52 KB.

La solución optimizada en C++ guarda los dobleces en un arreglo fijo de
30 números en la pila en lugar de un `std::vector` que crece. Como
n ≤ 10⁹ < 2³⁰, como mucho 30 dobleces por la mitad dejan la tira en
1 cm, así que el arreglo siempre basta y el propio programa no reserva
memoria dinámica: {1683_greedy_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1683_greedy_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +47.92%; base: `1683_greedy.cpp`.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1683_greedy_parsing_optimized.go`. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios.

Accepted #11328881 (Go 1.14 x64): **0.015 s / 916 KB**. Comparación archivada: `1683_greedy.go` (Go 1.14 x64) — 0.031 s / 1096 KB (#11288848).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Comparación PyPy anterior: `1683_greedy_optimized.py`: puesto de tiempo 18/21 y de memoria 1/21 en esta muestra comparable.

`1683_greedy_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy.cpp](1683_greedy.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 192 KB | 11288846 |
| [1683_greedy.go](1683_greedy.go) | Go 1.14 x64 | greedy | O(log n) | AC | 0.031 s | 1096 KB | 11288848 |
| [1683_greedy.java](1683_greedy.java) | Java 1.8 | greedy | O(log n) | AC | 0.125 s | 1664 KB | 11288850 |
| [1683_greedy.py](1683_greedy.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.125 s | 372 KB | 11288849 |
| [1683_greedy.rs](1683_greedy.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.015 s | 244 KB | 11288851 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy_optimized.cpp](1683_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 100 KB | 11304447 |
| [1683_greedy_optimized.java](1683_greedy_optimized.java) | Java 1.8 | greedy | O(log N) time; bounded 384-byte answer | AC | 0.078 s | 452 KB | 11327867 |
| [1683_greedy_optimized.py](1683_greedy_optimized.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.062 s | 620 KB | 11327033 |
| [1683_greedy_optimized.rs](1683_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.062 s | 52 KB | 11325142 |
| [1683_greedy_parsing_optimized.go](1683_greedy_parsing_optimized.go) | Go 1.14 x64 | greedy, parsing | O(log n) | AC | 0.015 s | 916 KB | 11328881 |
