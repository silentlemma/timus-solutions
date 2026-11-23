# 1032. Elegir números cuya suma sea múltiplo de N

[Timus 1032](https://acm.timus.ru/problem.aspx?space=1&num=1032) · dificultad 302 · prefix_sums, math

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `N` enteros positivos (`1 ≤ N ≤ 10 000`, cada uno como mucho 15 000,
con repeticiones posibles), elige uno o más cuya suma sea divisible entre
`N`. Si no hay tal elección, imprime 0.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` números, uno por línea.

## Salida

La cantidad de números elegidos y luego esos números, uno por línea, en
cualquier orden; o 0.

## Evaluación

Se acepta cualquier elección válida. El verificador comprueba que cada
número se usa como mucho tantas veces como aparece, que se elige al menos
uno y que la suma es múltiplo de `N`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
8
6
1
```

Salida:

```
1
8
```

### Ejemplo 2

Entrada:

```
1
15000
```

Salida:

```
1
15000
```

## Solución

**Siempre existe una elección**, e incluso puede ser un bloque de números
consecutivos. Mira las `N + 1` sumas prefijas `S_0 = 0, S_1, ..., S_N`
módulo `N`. Toman como mucho `N` valores distintos, así que por el
**principio del palomar** dos coinciden, `S_i ≡ S_j (mod N)` con `i < j`;
entonces `a_{i+1} + ... + a_j = S_j - S_i` es múltiplo de `N`.

Se recorren los números manteniendo la suma prefija módulo `N` y la primera
posición en que apareció cada resto (el resto 0 en la posición 0). El primer
resto repetido da el bloque. `O(N)`.

Así que la respuesta 0 nunca hace falta.

Detalles a tener en cuenta:

- el resto 0 debe darse por «visto» en la posición 0, para encontrar un
  prefijo que ya sea múltiplo de `N`;
- en la salida van los valores, no sus posiciones;
- `N = 1`: cualquier número sirve.

## Soluciones optimizadas

`1032_prefix_sums_optimized.py`. Python conserva el primer resto prefijo repetido módulo N. Guarda posiciones iniciales y valores en arreglos unsigned-short: N<=10000, valores<=15000 y posiciones desplazadas caben en 16 bits. Cero significa no visto y registra antes el prefijo vacío. Restos iguales dan un bloque contiguo cuya suma es divisible por N. Imprime longitud y valores en bloques de hasta 512, sin construir toda la cadena del testigo. Vacía stdout antes de salir dentro de main con ambos arreglos vivos. Tiempo O(N), espacio O(N) más bloque de salida acotado. La base didáctica no cambia.

Accepted exacto Python 3.12 x64 #11327433: 0.078 s / 820 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/51, memoria 1/51. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Ambas métricas son primeras; cumple también la meta propia del lenguaje, sin asterisco. El registro optimizado documentado antes #11310314 (Python 3.12 x64) era 0.109 s / 1068 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1032_prefix_sums_optimized.py`: 0.078 s / 820 KB; base didáctica conservada `1032_prefix_sums.py`: 0.093 s / 2608 KB.

Las implementaciones base aceptadas [1032_prefix_sums.cpp](1032_prefix_sums.cpp), [1032_prefix_sums.go](1032_prefix_sums.go), [1032_prefix_sums.java](1032_prefix_sums.java), [1032_prefix_sums.rs](1032_prefix_sums.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1032_prefix_sums_optimized.java`. Java actualiza el residuo del prefijo conforme llegan los valores. En el arreglo de primeras posiciones, cero significa no visto; las posiciones reales se guardan desplazadas en uno, y el prefijo vacío se registra al comienzo. Al repetirse un residuo, imprime directamente los valores intermedios guardados con un búfer acotado. La igualdad de residuos hace que la suma del segmento sea divisible por N. Se eliminan el relleno del arreglo y el constructor de toda la salida, manteniendo O(N) tiempo y espacio.

Frente a `1032_prefix_sums.java`: tiempo 0.156 s → 0.109 s; memoria 944 KB → 592 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1032_prefix_sums_optimized.rs`. Se mantienen el algoritmo y los tipos enteros. Los tokens decimales se convierten directamente; los negativos se acumulan con su signo para representar también el mínimo entero con signo. No cambian el almacenamiento de entrada ni la complejidad del algoritmo.

Accepted #11328489 (Rust 1.75 x64): **0.031 s / 456 KB**. Comparación archivada: `1032_prefix_sums.rs` (Rust 1.75 x64) — 0.046 s / 464 KB (#11278437).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

La misma pasada en todos los lenguajes.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1032_prefix_sums.cpp](1032_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 232 KB | 11278431 |
| [1032_prefix_sums.go](1032_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 1368 KB | 11278432 |
| [1032_prefix_sums.java](1032_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.156 s | 944 KB | 11278435 |
| [1032_prefix_sums.py](1032_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.093 s | 2608 KB | 11278433 |
| [1032_prefix_sums.rs](1032_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 464 KB | 11278437 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1032_prefix_sums_optimized.py](1032_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N) time; O(N) storage + bounded output chunk | AC | 0.078 s | 820 KB | 11327433 |
| [1032_prefix_sums_optimized.java](1032_prefix_sums_optimized.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 592 KB | 11325005 |
| [1032_prefix_sums_optimized.rs](1032_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.031 s | 456 KB | 11328489 |
