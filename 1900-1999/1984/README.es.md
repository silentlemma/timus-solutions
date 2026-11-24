# 1984. Una circunferencia que toca todos los discos unitarios

[Timus 1984](https://acm.timus.ru/problem.aspx?space=1&num=1984) · dificultad 214 · geometry

Problema popular, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar `n` discos de radio 1 dentro de una circunferencia, con
interiores disjuntos, de modo que cada disco sea tangente interiormente
a la frontera exterior. Hallar el mínimo radio exterior. La entrada es
un entero con `1≤n≤10`. Límites: 0,5 segundos y 64 MB.

## Entrada

Un entero `n`.

## Salida

Un número real: el radio mínimo.

## Evaluación

Se compara el valor numérico con la tolerancia indicada y las cotas de redondeo demostradas abajo.

- `1984_geometry_optimized.cpp` (G++ 13.2 x64): 16 pruebas del repositorio.

- `1984_geometry_optimized.py` (PyPy 3.10 x64): 16 pruebas del repositorio; 10 comparaciones adicionales de fuente exacta.

## Ejemplos

Entrada:

```
2
```

Salida:

```
2
```

## Solución

Con un disco, la respuesta es 1. Para `n≥2`, sean `R` el radio exterior
y `r=R−1>0`. La tangencia interior obliga a que todos los centros estén
en la circunferencia concéntrica de radio `r`. Dos centros cualesquiera
deben estar separados al menos por 2.

Ordenar los centros por ángulo polar. Los `n` intervalos angulares
cíclicos suman `2π`, así que alguno tiene tamaño `α≤2π/n≤π`. La
distancia de esa pareja es `2r sin(α/2)≤2r sin(π/n)`. Como debe ser al
menos 2, resulta `R≥1+1/sin(π/n)`.

La cota se alcanza colocando los centros en los vértices de un polígono
regular de `n` lados sobre una circunferencia de radio `1/sin(π/n)`. Los
centros vecinos distan exactamente 2 y las demás parejas no están más
cerca. Cada disco unitario llega al radio exterior `R=r+1`, cumpliendo
todas las tangencias. Por tanto, para `n≥2` el mínimo es `1+1/sin(π/n)`.

En el ejemplo `n=2`, los centros son opuestos en una circunferencia de
radio 1. Los discos unitarios se tocan y caben en una circunferencia de
radio 2, por lo que la respuesta es 2.

La fórmula requiere un número constante de operaciones: tiempo y memoria
`O(1)`. La doble precisión y diez cifras decimales bastan para la
tolerancia en todo el rango permitido.

Trampas:

- Cada disco debe tocar la frontera exterior; el empaquetamiento sin esa
  condición es otro problema.
- Los centros están a distancia `R−1`, no `R`.
- Resolver primero el caso de un disco para evitar dividir entre `sin(π)`.
- Usar `π/n` en radianes.
- Los interiores no pueden solaparse, pero los discos sí pueden tocarse.

## Soluciones optimizadas

`1984_geometry_optimized.java`. Conserva radio 1 para N=1 y 1+1/sin(π/N) con el mismo Math.sin. Analiza el entero acotado y emite la representación double reversible, sin inicializar Formatter/Locale. No cambia geometría ni sustituye seno por aproximación. Trabajo/estado numérico O(1); conserva la fórmula sencilla.

Accepted de fuente exacto Java 1.8 #11326960: 0.078 s / 460 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 1/53, memoria 2/53. Al usar menos de 1024 KB, la admisión estricta usa solo tiempo.

- `1984_geometry_optimized.java`: 0.078 s / 460 KB; base didáctica conservada `1984_geometry.java`: 0.125 s / 1796 KB; cambio de tiempo -37.6%; cambio de memoria -74.4%.

El radio sigue siendo 1 si N = 1, o 1 + 1/sin(pi/N). C++/Java reducen E/S manteniendo la fórmula de biblioteca. Python evalúa el seno hasta x^13 en forma Horner, con seis cocientes factoriales constantes, no una tabla de respuestas. Para 2 <= N <= 10, 0 < x<=pi/2 y el siguiente término alterno x^15/15!<7e-10; sin(pi/N)>=sin(pi/10)>0,3, así que el error del radio<10^-8. Seis decimales por salida entera añaden como máximo medio micro: sigue dentro de 10^-6 absoluto. Los diez N legales se contrastaron con seno de biblioteca independiente. Límites fijos: O(1) de tiempo y espacio, conservando N=1.

- `1984_geometry_optimized.cpp`: 0.015 s / 120 KB; base `1984_geometry.cpp`: 0.015 s / 444 KB; cambio respecto a la base: tiempo -0.0%, memoria -73.0%.

- `1984_geometry_optimized.py`: 0.109 s / 276 KB; base `1984_geometry.py`: 0.078 s / 396 KB; cambio respecto a la base: tiempo +39.7%, memoria -30.3%.

`1984_geometry_optimized.rs`. Conserva la fórmula del radio para colocar los círculos: un círculo requiere radio 1; en otro caso, 1+1/sin(PI/N). Calcula en f64 e imprime diez decimales directamente con estado numérico constante. Tiempo y espacio auxiliar O(1). Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1984_geometry.rs`: tiempo 0.015 s → 0.031 s; memoria 256 KB → 88 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1984_geometry_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1984_geometry.cpp](1984_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 444 KB | 11292346 |
| [1984_geometry.go](1984_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1100 KB | 11292347 |
| [1984_geometry.java](1984_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1796 KB | 11309215 |
| [1984_geometry.py](1984_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 396 KB | 11292348 |
| [1984_geometry.rs](1984_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 256 KB | 11292350 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1984_geometry_optimized.cpp](1984_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 120 KB | 11308253 |
| [1984_geometry_optimized.java](1984_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.078 s | 460 KB | 11326960 |
| [1984_geometry_optimized.py](1984_geometry_optimized.py) | PyPy 3.10 x64 | geometry | O(1) | AC | 0.109 s | 276 KB | 11309752 |
| [1984_geometry_optimized.rs](1984_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 88 KB | 11325118 |
