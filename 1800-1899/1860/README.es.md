# 1860. Fiborial

[Timus 1860](https://acm.timus.ru/problem.aspx?space=1&num=1860) · dificultad 469 · number_theory

Problema original de Denis Dublennykh (idea de Grigoriy Nazarov), del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sean F₀ = F₁ = 1 y Fᵢ = i·Fᵢ₋₁·Fᵢ₋₂. Hallar el número de divisores de
Fₙ módulo 10⁹ + 7.

## Entrada

n (1 ≤ n ≤ 10⁶).

## Salida

El número de divisores de Fₙ módulo 10⁹ + 7.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
4
```

## Solución

Cada paso multiplica una vez por i y repite los dos productos
anteriores, así que el factor k entra en Fₙ exactamente fib(n − k + 1)
veces, con fib(1) = fib(2) = 1: aparece una vez en F_k, una en F_{k+1},
dos en F_{k+2}, y así según la regla de Fibonacci. Por tanto
Fₙ = Π k^fib(n−k+1) para k = 1 … n.

El número de divisores es Π (e_p + 1) sobre los primos p, donde e_p es
el exponente de p en Fₙ. Un número k aporta v_p(k) por su peso
fib(n − k + 1), y v_p(k) cuenta cuántos de p, p², p³, … dividen a k,
así que e_p es la suma de los pesos de todos los múltiplos de p, de p²,
etcétera. Solo importa e_p módulo 10⁹ + 7, así que los pesos también se
guardan reducidos. Recorrer los múltiplos de cada potencia de primo
lleva unos n·ln ln n pasos; la solución en Python suma cada progresión
con un solo corte. `O(n log log n)`.

En el ejemplo F₃ = 3·F₂·F₁ = 3·2·1 = 6, que tiene los divisores 1, 2, 3
y 6.

Trampas:

- los exponentes son enormes, pero la respuesta solo los necesita
  módulo 10⁹ + 7;
- una potencia de primo que pasa de n debe parar el bucle antes de
  desbordarse;
- la solución en Python corre en PyPy.

Las respuestas coinciden con una factorización directa de Fₙ para n
hasta 14 y con una implementación aceptada independiente hasta 10⁶.

## Soluciones optimizadas

`1860_number_theory_optimized.java`. Conserva la fórmula de divisores por exponentes primos módulo10^9+7. Guarda Fibonacci en int[] en lugar de long[]: incluso sumar dos residuos antes de reducir queda bajo2^31. Consulta el peso como fib[n-multiple+1], eliminando long[] weight. Mantiene exponentes acumulados y productos en long, reduciendo tras cada potencia prima. Mismos tamiz y aportes. Tiempo O(n log log n), espacio O(n), con menos bytes por índice. Lee un token numérico; n=1 aún da un divisor.

Frente a `1860_number_theory.java`: tiempo 0.187 s → 0.125 s; memoria 18 412 KB → 8 368 KB.

C++, Go y Rust mantienen las sumas por potencias primas con un único arreglo Fibonacci uint32: el peso k es fib[n−k+1], sin duplicar pesos64. Dos residuos suman menos de2·MOD, basta restar condicionalmente. La criba de impares ocupa unos n/16 bytes y trata2 aparte. Cada primo suma hasta n pesos: uint64 queda bajo n·MOD≤10¹⁵ y se reduce al final. También cabe el producto modular. Se comprueba power>n/p antes de multiplicar. Tiempo O(n log log n), memoria O(n), unos4n bytes de pesos frente a dos arreglos8n. Se conservan bases; Java/Python reutilizan las admitidas.

Las implementaciones base aceptadas [1860_number_theory.java](1860_number_theory.java), [1860_number_theory.py](1860_number_theory.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1860_number_theory_optimized.py`. Los pesos de Fibonacci módulo se guardan en un solo arreglo compacto sin signo y se invierten in situ, evitando otra copia. Este Accepted corresponde a PyPy 3.10, no a CPython. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328686 (PyPy 3.10 x64): **0.218 s / 14116 KB**. Comparación archivada: `1860_number_theory.py` (PyPy 3.10 x64) — 0.171 s / 34140 KB (#11325600).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1860_number_theory_optimized.java`: puesto de tiempo 3/16 y de memoria 5/16 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1860_number_theory.cpp](1860_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 15492 KB | 11325590 |
| [1860_number_theory.go](1860_number_theory.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.046 s | 18860 KB | 11290853 |
| [1860_number_theory.java](1860_number_theory.java) | Java 1.8 | number_theory | O(n log log n) | AC | 0.187 s | 18412 KB | 11325560 |
| [1860_number_theory.py](1860_number_theory.py) | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.171 s | 34140 KB | 11325600 |
| [1860_number_theory.rs](1860_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.046 s | 16684 KB | 11325614 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1860_number_theory_optimized.cpp](1860_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(n log log n) | AC | 0.031 s | 3700 KB | 11315295 |
| [1860_number_theory_optimized.go](1860_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(n log log n) | AC | 0.031 s | 4800 KB | 11315297 |
| [1860_number_theory_optimized.rs](1860_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(n log log n) | AC | 0.046 s | 3888 KB | 11315298 |
| [1860_number_theory_optimized.java](1860_number_theory_optimized.java) | Java 1.8 | number_theory | O(n log log n) | AC | 0.125 s | 8368 KB | 11325040 |
| [1860_number_theory_optimized.py](1860_number_theory_optimized.py) | PyPy 3.10 x64 | number_theory | O(n log log n) | AC | 0.218 s | 14116 KB | 11328686 |
