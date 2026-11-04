# 1869. Crucero de Año Nuevo

[Timus 1869](https://acm.timus.ru/problem.aspx?space=1&num=1869) · dificultad 239 · prefix_sums, simulation

Problema original de Denis Dublennykh, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tren va de Vladivostok (estación 1) a Moscú (estación n) parando en
las estaciones 1, …, n, y luego vuelve por el mismo camino. aᵢⱼ
personas compraron billete de la estación i a la j: viajan en el tren
de ida si i < j y en el de vuelta si i > j. Cada vagón tiene 36
asientos. ¿Cuántos vagones necesita el tren para que todos tengan
asiento?

## Entrada

n (2 ≤ n ≤ 100), luego la matriz n × n de aᵢⱼ (0 ≤ aᵢⱼ ≤ 1000,
aᵢᵢ = 0).

## Salida

El menor número de vagones.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 180 180
0 0 180
360 0 0
```

Salida:

```
10
```

## Solución

El tren debe llevar el mayor número de personas a bordo a la vez, en
cualquier tramo y en cualquier sentido. Para cada sentido se suma aᵢⱼ
en la estación de menor número y se resta en la de mayor número. La suma acumulada de
estos cambios por orden de estación es la carga de cada tramo. La
respuesta es la mayor carga dividida entre 36 y redondeada hacia
arriba. `O(n²)`.

En el ejemplo viajan 360 personas en el tren de ida en ambos tramos
(los 180 de la estación 1 a la 3 junto con los 180 de la 1 a la 2 o de
la 2 a la 3), y 360 vuelven todo el camino: 10 vagones.

Trampas:

- los dos sentidos son viajes distintos, así que sus cargas no se
  suman;
- la división redondea hacia arriba: 37 personas necesitan dos vagones;
- sin ningún billete la respuesta es 0.

Las respuestas coinciden con una implementación aceptada independiente
en 150 matrices aleatorias.

## Soluciones optimizadas

Las cinco simulaciones directas suman cada billete en todos los tramos que recorre, con tiempo O(N³) y espacio O(N). Se usan como bases educativas junto con las soluciones matriciales originales. Python optimizado lee una fila por estación. Los sufijos derechos aportan a los tramos de ida y los prefijos izquierdos a los de vuelta. Cada vector se empaqueta en un entero con campos de 32 bits. Desplazar un campo y dividir por 2^32−1 calcula los sufijos y la multiplicación por un número de unos en esa base, con truncamiento, calcula los prefijos. Cada campo vale como máximo 1000N² y no hay acarreo entre campos. La respuesta es la carga máxima en ambos sentidos dividida por 36, redondeando hacia arriba. El tiempo es O(N²) y el espacio de trabajo O(N). La versión tarda menos y usa más memoria que la simulación directa.

- `1869_prefix_sums_optimized.py`: 0.062 s / 468 KB; base `1869_simulation.py`: 0.093 s / 396 KB; cambio respecto a la base: tiempo -33.3%, memoria +18.2%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1869_simulation.cpp`; fuente que cubre `1869_simulation.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 45/45.

- Go: base didáctica preferida `1869_simulation.go`; fuente que cubre `1869_simulation.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1869_simulation.java`; fuente que cubre `1869_simulation.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1869_simulation.py`; fuente que cubre `1869_prefix_sums_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 9/9.

- Rust: base didáctica preferida `1869_simulation.rs`; fuente que cubre `1869_simulation.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1869_simulation.cpp](1869_simulation.cpp) | G++ 13.2 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 108 KB | 11308691 |
| [1869_simulation.go](1869_simulation.go) | Go 1.14 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 1228 KB | 11308696 |
| [1869_simulation.java](1869_simulation.java) | Java 1.8 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 388 KB | 11308693 |
| [1869_simulation.py](1869_simulation.py) | Python 3.12 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 396 KB | 11308701 |
| [1869_simulation.rs](1869_simulation.rs) | Rust 1.75 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.046 s | 320 KB | 11308699 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums.cpp](1869_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 180 KB | 11309204 |
| [1869_prefix_sums.go](1869_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.031 s | 1244 KB | 11290934 |
| [1869_prefix_sums.java](1869_prefix_sums.java) | Java 1.8 | prefix_sums | O(n^2) | AC | 0.093 s | 444 KB | 11309206 |
| [1869_prefix_sums.py](1869_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n^2) | AC | 0.078 s | 1324 KB | 11309207 |
| [1869_prefix_sums.rs](1869_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 336 KB | 11309208 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums_optimized.py](1869_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N^2) time, O(N) working space | AC | 0.062 s | 468 KB | 11310099 |
