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

- `1984_geometry_optimized.java` (Java 1.8): 16 pruebas del repositorio.

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

El radio sigue siendo 1 si N = 1, o 1 + 1/sin(pi/N). C++/Java reducen E/S manteniendo la fórmula de biblioteca. Python evalúa el seno hasta x^13 en forma Horner, con seis cocientes factoriales constantes, no una tabla de respuestas. Para 2 <= N <= 10, 0 < x<=pi/2 y el siguiente término alterno x^15/15!<7e-10; sin(pi/N)>=sin(pi/10)>0,3, así que el error del radio<10^-8. Seis decimales por salida entera añaden como máximo medio micro: sigue dentro de 10^-6 absoluto. Los diez N legales se contrastaron con seno de biblioteca independiente. Límites fijos: O(1) de tiempo y espacio, conservando N=1.

- `1984_geometry_optimized.cpp`: 0.015 s / 120 KB; base `1984_geometry.cpp`: 0.015 s / 444 KB; cambio respecto a la base: tiempo -0.0%, memoria -73.0%.
- `1984_geometry_optimized.java`: 0.125 s / 540 KB; base `1984_geometry.java`: 0.125 s / 1796 KB; cambio respecto a la base: tiempo -0.0%, memoria -69.9%.
- `1984_geometry_optimized.py`: 0.109 s / 276 KB; base `1984_geometry.py`: 0.078 s / 396 KB; cambio respecto a la base: tiempo +39.7%, memoria -30.3%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1984_geometry.cpp`; fuente que cubre `1984_geometry_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 30/30.

- Go: base didáctica preferida `1984_geometry.go`; fuente que cubre `1984_geometry.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1984_geometry.java`; fuente que cubre `1984_geometry_optimized.java`; puestos tiempo/memoria 4/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1984_geometry.py`; fuente que cubre `1984_geometry_optimized.py`; puestos tiempo/memoria 8/1, registros de otros autores 9/9.

- Rust: base didáctica preferida `1984_geometry.rs`; fuente que cubre `1984_geometry.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

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
| [1984_geometry_optimized.java](1984_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 540 KB | 11308258 |
| [1984_geometry_optimized.py](1984_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(1) | AC | 0.109 s | 276 KB | 11309752 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
