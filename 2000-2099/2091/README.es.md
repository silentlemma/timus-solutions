# 2091. Dos asignaturas que reparten los planes de forma más pareja

[Timus 2091](https://acm.timus.ru/problem.aspx?space=1&num=2091) · dificultad 271 · bitmask, bruteforce

Problema original de Dmitry Ivankov, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tabla n × m dice cuáles de m asignaturas incluye cada uno de n
planes de estudio. Elegir dos asignaturas distintas A y B; reparten los
planes en cuatro grupos: con ambas, solo con A, solo con B y con
ninguna. Hacer el grupo mayor lo más pequeño posible e imprimir su
tamaño y las dos asignaturas. Se acepta cualquier pareja óptima. Los
límites son 1 segundo y 64 MB.

## Entrada

n y m, 4 ≤ n, m ≤ 100, y después las n filas de m ceros y unos.

## Salida

El menor tamaño posible del grupo mayor y después las dos asignaturas.

## Evaluación

El verificador comprueba óptimo y ruta/pareja válida, sin exigir salida literal.

- `2091_bitmask.cpp` (G++ 13.2 x64): 13 pruebas del repositorio.

- `2091_bitmask.go` (Go 1.14 x64): 13 pruebas del repositorio.

- `2091_bitmask.java` (Java 1.8): 13 pruebas del repositorio.

- `2091_bitmask.py` (Python 3.12 x64): 13 pruebas del repositorio.

- `2091_bitmask.rs` (Rust 1.75 x64): 13 pruebas del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 4
0 0 0 1
0 0 1 0
0 1 1 1
1 1 1 1
0 0 0 0
1 0 0 1
```

Salida:

```
2
1 3
```

## Solución

Hay menos de 5000 parejas de asignaturas, y los grupos de una pareja se
cuentan en una pasada por los planes, con número de grupo 2·[A] + [B].
Probar todas las parejas cuesta O(m² n), medio millón de pasos.

En el ejemplo las asignaturas 1 y 3 dan los grupos {4}, {6}, {2, 3} y
{1, 5}, así que el mayor tiene 2 planes.

## Soluciones optimizadas

Se conserva enumerar cada pareja y programa. Las variantes bitmask codifican los programas por curso. Con totales ca,cb e intersección t, los cuatro grupos son t,ca-t,cb-t,N-ca-cb+t. Intersección y popcount sustituyen recorrer N programas por pareja. Se prueban cursos distintos minimizando el grupo máximo; ceil(N/4) es cota inferior universal y permite salida óptima al alcanzarla. Filas de programas repetidas conservan bits separados y su multiplicidad. Para N<=100, cada curso nativo usa dos palabras64bits; Python, enteros grandes. Estado numérico O(M ceil(N/W))palabras; Python/Rust retienen además O(NM)entrada. Tiempo O(NM+M² ceil(N/W)), con máximo dos palabras nativas reales. Se acepta cualquier pareja óptima.

- `2091_bitmask.cpp`: 0.015 s / 112 KB; base `2091_bruteforce.cpp`: 0.015 s / 228 KB; cambio respecto a la base: tiempo -0.0%, memoria -50.9%.
- `2091_bitmask.go`: 0.015 s / 304 KB; base `2091_bruteforce.go`: 0.031 s / 1200 KB; cambio respecto a la base: tiempo -51.6%, memoria -74.7%.
- `2091_bitmask.java`: 0.125 s / 400 KB; base `2091_bruteforce.java`: 0.125 s / 5664 KB; cambio respecto a la base: tiempo -0.0%, memoria -92.9%.
- `2091_bitmask.py`: 0.078 s / 592 KB; base `2091_bruteforce.py`: 0.125 s / 676 KB; cambio respecto a la base: tiempo -37.6%, memoria -12.4%.
- `2091_bitmask.rs`: 0.015 s / 220 KB; base `2091_bruteforce.rs`: 0.015 s / 464 KB; cambio respecto a la base: tiempo -0.0%, memoria -52.6%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `2091_bruteforce.cpp`; fuente que cubre `2091_bitmask.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 56/56.

- Go: base didáctica preferida `2091_bruteforce.go`; fuente que cubre `2091_bitmask.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `2091_bruteforce.java`; fuente que cubre `2091_bitmask.java`; puestos tiempo/memoria 2/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `2091_bruteforce.py`; fuente que cubre `2091_bitmask.py`; puestos tiempo/memoria 1/1, registros de otros autores 12/12.

- Rust: base didáctica preferida `2091_bruteforce.rs`; fuente que cubre `2091_bitmask.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2091_bruteforce.cpp](2091_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 228 KB | 11308118 |
| [2091_bruteforce.go](2091_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m^2 n) | AC | 0.031 s | 1200 KB | 11294643 |
| [2091_bruteforce.java](2091_bruteforce.java) | Java 1.8 | bruteforce | O(m^2 n) | AC | 0.125 s | 5664 KB | 11308125 |
| [2091_bruteforce.py](2091_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m^2 n) | AC | 0.125 s | 676 KB | 11308827 |
| [2091_bruteforce.rs](2091_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 464 KB | 11308829 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2091_bitmask.cpp](2091_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.015 s | 112 KB | 11308002 |
| [2091_bitmask.go](2091_bitmask.go) | Go 1.14 x64 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.015 s | 304 KB | 11309740 |
| [2091_bitmask.java](2091_bitmask.java) \* | Java 1.8 | bitmask | O(NM+M²) time; O(M) words for N≤100 | AC | 0.125 s | 400 KB | 11308008 |
| [2091_bitmask.py](2091_bitmask.py) | Python 3.12 x64 | bitmask | O(NM+M² ceil(N/W)) time; O(NM+M ceil(N/W)) space | AC | 0.078 s | 592 KB | 11308000 |
| [2091_bitmask.rs](2091_bitmask.rs) | Rust 1.75 x64 | bitmask | O(NM+M² ceil(N/W)) time; O(NM+M ceil(N/W)) space | AC | 0.015 s | 220 KB | 11308009 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
