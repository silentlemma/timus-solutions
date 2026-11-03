# 1208. El mayor número de equipos legendarios sin miembros en común

[Timus 1208](https://acm.timus.ru/problem.aspx?space=1&num=1208) · dificultad 210 · bitmask, dp

Problema original de Leonid Volkov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elija el mayor subconjunto de `1 ≤ K ≤ 18` equipos sin ningún miembro
compartido entre dos equipos elegidos. Cada equipo contiene tres nombres
distintos, de hasta 20 letras latinas minúsculas; un nombre puede aparecer
en varios equipos. Tiempo: 0,5 segundos. Memoria: 64 MB.

## Entrada

`K` y luego los tres nombres de cada equipo, de hasta 20 letras
minúsculas.

## Salida

El mayor número de equipos que pueden participar.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
gerostratos scorpio shamgshamg
zaitsev silverberg cousteau
zaitsev petersen shamgshamg
clipper petersen shamgshamg
clipper bakirelli vasiliadi
silverberg atn dolly
knuth dijkstra bellman
```

Salida:

```
4
```

## Solución

Dos equipos entran en conflicto si sus conjuntos de miembros se
intersecan. Para cada equipo `i` guardamos la máscara `clash[i]`, incluido
él mismo. En el conjunto restante `S`, tomamos el equipo de bit menor `i`.
Toda elección válida lo excluye, o lo incluye y elimina sus conflictos:

`best(S) = max(best(S sin i), 1 + best(S sin clash[i]))`.

Ambos casos cubren todas las posibilidades; el conjunto vacío vale cero.
Las máscaras nuevas son menores porque borran `i`, por lo que las bases
nativas llenan una tabla en orden creciente. Python evalúa la misma
recurrencia de forma perezosa con `lru_cache`, sin visitar necesariamente
todas las máscaras. Con nombres de longitud acotada, tiempo
`O(2^K + K²)` y hasta `O(2^K)` espacio de tabla o memoria caché.
Se conservan sin cambios las cinco bases Accepted. Un nombre común
en columnas distintas también causa conflicto; dos copias del mismo
equipo no pueden seleccionarse juntas.

## Soluciones optimizadas

**C++, Go, Java, Rust.** El nuevo algoritmo recorre un árbol de inclusión/exclusión sin
guardar la respuesta de cada máscara. Su estado contiene la máscara
restante y la cantidad elegida; todos los restantes son compatibles
con lo elegido. Guardamos la mejor cuenta factible hallada.
`selected + popcount(mask)` es una cota superior aun ignorando conflictos
internos; si no supera la mejor cuenta, se poda con seguridad.

En otro caso elegimos el equipo con más conflictos dentro de la máscara,
incluido él mismo. Si el máximo no supera uno, no hay parejas en conflicto:
tomarlos todos alcanza la cota. Si no, primero lo incluimos y quitamos
sus conflictos, y después lo excluimos solo a él. Ambas ramas cubren
todas las extensiones factibles. Incluir primero puede mejorar la cota
antes de excluir; el grado máximo es una heurística, no una condición
de corrección. Cada rama elimina un equipo: profundidad a lo sumo `K ≤ 18`.

Tiempo máximo `O(K 2^K + K²)`, porque elegir el siguiente equipo examina
hasta `K` bits por nodo. El espacio de búsqueda es `O(K)` para máscaras
y pila, además de los nombres; no hay tabla exponencial. Las máscaras
caben en 32 bits. Cambia el algoritmo de búsqueda, de ahí el nombre
`backtracking_bitmask`, sin crear copias con `_optimized`. Las cuatro
versiones publicadas se admiten por memoria. Java registra mayor tiempo,
0,125 s frente a 0,109 s, pero ahorra 83,3% de memoria; un solo tic no
prueba de forma fiable un cambio de CPU.

**Python/PyPy.** Se conserva la solución clara con memoización de máscaras completas. La nueva divide hasta 18 equipos en mitades de hasta 9. Para cada subconjunto izquierdo, omitir el equipo menor o elegirlo y quitar conflictos calcula su óptimo. A la derecha se enumeran exclusión/inclusión, quitando conflictos derechos y equipos izquierdos incompatibles; al terminar se consulta la tabla izquierda. Toda selección válida corresponde a una rama derecha y su mejor subconjunto izquierdo compatible. Los nombres se comparan exactamente, sin hashes probabilísticos. TiempoO(K²+2^ceil(K/2)), espacioO(2^floor(K/2)+K).

- `1208_backtracking_bitmask.cpp`: 0.015 s / 176 KB; base `1208_bitmask.cpp`: 0.015 s / 976 KB; cambio respecto a la base: tiempo -0.0%, memoria -82.0%.
- `1208_backtracking_bitmask.go`: 0.031 s / 1104 KB; base `1208_bitmask.go`: 0.062 s / 3204 KB; cambio respecto a la base: tiempo -50.0%, memoria -65.5%.
- `1208_backtracking_bitmask.java`: 0.125 s / 448 KB; base `1208_bitmask.java`: 0.109 s / 2688 KB; cambio respecto a la base: tiempo +14.7%, memoria -83.3%.
- `1208_backtracking_bitmask.rs`: 0.015 s / 224 KB; base `1208_bitmask.rs`: 0.046 s / 684 KB; cambio respecto a la base: tiempo -67.4%, memoria -67.3%.
- `1208_bitmask_dp.py`: 0.125 s / 296 KB; base `1208_bitmask.py`: 0.078 s / 456 KB; cambio respecto a la base: tiempo +60.3%, memoria -35.1%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1208_bitmask.cpp`; fuente que cubre `1208_backtracking_bitmask.cpp`; puestos tiempo/memoria 1/27, registros de otros autores 109/109.

- Go: base didáctica preferida `1208_bitmask.go`; fuente que cubre `1208_backtracking_bitmask.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1208_bitmask.java`; fuente que cubre `1208_backtracking_bitmask.java`; puestos tiempo/memoria 2/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1208_bitmask.py`; fuente que cubre `1208_bitmask_dp.py`; puestos tiempo/memoria 4/2, registros de otros autores 21/21.

- Rust: base didáctica preferida `1208_bitmask.rs`; fuente que cubre `1208_backtracking_bitmask.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1208_bitmask.cpp](1208_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K + K^2) | AC | 0.015 s | 976 KB | 11283611 |
| [1208_bitmask.go](1208_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K + K^2) | AC | 0.062 s | 3204 KB | 11283615 |
| [1208_bitmask.java](1208_bitmask.java) | Java 1.8 | bitmask | O(2^K + K^2) | AC | 0.109 s | 2688 KB | 11283617 |
| [1208_bitmask.py](1208_bitmask.py) | Python 3.12 x64 | bitmask | O(2^K + K^2) | AC | 0.078 s | 456 KB | 11283616 |
| [1208_bitmask.rs](1208_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K + K^2) | AC | 0.046 s | 684 KB | 11283620 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1208_backtracking_bitmask.cpp](1208_backtracking_bitmask.cpp) \* | G++ 13.2 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.015 s | 176 KB | 11308198 |
| [1208_backtracking_bitmask.go](1208_backtracking_bitmask.go) | Go 1.14 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.031 s | 1104 KB | 11308199 |
| [1208_backtracking_bitmask.java](1208_backtracking_bitmask.java) \* | Java 1.8 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.125 s | 448 KB | 11308200 |
| [1208_backtracking_bitmask.rs](1208_backtracking_bitmask.rs) | Rust 1.75 x64 | backtracking, bitmask | O(K 2^K + K^2) | AC | 0.015 s | 224 KB | 11308202 |
| [1208_bitmask_dp.py](1208_bitmask_dp.py) \* | PyPy 3.10 x64 | bitmask, dp | O(K^2 + 2^(K/2)) time, O(2^(K/2)+K) memory | AC | 0.125 s | 296 KB | 11309782 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
