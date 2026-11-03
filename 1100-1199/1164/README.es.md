# 1164. ¿Qué letras quedan tras encontrar todas las palabras de una sopa de letras?

[Timus 1164](https://acm.timus.ru/problem.aspx?space=1&num=1164) · dificultad 207 · strings

Problema original de Alex Selivanov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula de `N×M` letras mayúsculas (`2 ≤ N, M ≤ 10`) esconde
`P ≤ 100` palabras. Cada palabra ocupa un camino de casillas vecinas por
un lado, y ninguna casilla pertenece a dos palabras ni dos veces a la
misma. Siempre existe una colocación válida. Hay que imprimir, en orden
alfabético, las letras de las casillas que no usa ninguna palabra.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, `M` y `P`, luego las `N` filas de la cuadrícula y luego las `P`
palabras.

## Salida

Las letras sobrantes, ordenadas, en una línea.

## Evaluación

Comparar exactamente las mayúsculas restantes; si no quedan letras, se admite salida vacía. El nuevo código Python exacto pasó 11 pruebas del repositorio con PyPy 3.10. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 2
EBG
GEE
EGE
BEG
GEE
```

Salida:

```
EEG
```

## Solución

No hace falta buscar caminos. Para cada letra `c`, sea `G[c]`
su número de celdas en la cuadrícula y `U[c]` sus apariciones en las
palabras. Cualquier colocación válida usa exactamente `U[c]` celdas
distintas con `c`: un camino no repite celdas y dos palabras no se
superponen. Por tanto, siempre quedan `G[c] − U[c]` copias, con
independencia de la geometría. La existencia garantizada de colocación
asegura diferencias no negativas.

Contamos las letras de la cuadrícula, restamos las palabras con sus
multiplicidades y emitimos cada letra de `A` a `Z` tantas veces como
quede. Así obtenemos exactamente el multiconjunto sobrante ordenado.
Las palabras repetidas consumen sus letras por separado. Si se usan
todas las celdas, imprimimos una línea vacía. La garantía implica además
longitud total `W ≤ N M ≤ 100`, y cada palabra tiene como máximo 100 letras.

Tiempo `O(N M + W + 26)`. Las bases nativas guardan 26 contadores;
la base Python legible usa `Counter`. Incluyendo entrada y salida
almacenadas, `O(N M + W)` acota el espacio de todas las versiones;
las versiones en flujo retienen menos entrada. Se conservan sin cambios
las cinco fuentes Accepted originales.

## Soluciones optimizadas

Toda colocación consume el mismo multiconjunto de letras. Se conservan los contadores claros y el C++ compacto. Python cuenta cada una de las 26 mayúsculas en la cuadrícula y las palabras concatenadas y emite las diferencias positivas en orden. El alfabeto constante mantiene tiempo lineal. Evita Counter y diccionarios separados, aunque conserva las cadenas. Usa flujos de texto existentes y escritura directa. La mejora confirmada es solo de memoria; el mayor tiempo se declara abajo.

- `1164_strings_optimized.cpp`: 0.015 s / 104 KB; base `1164_strings.cpp`: 0.015 s / 380 KB; cambio respecto a la base: tiempo -0.0%, memoria -72.6%.
- `1164_strings_optimized.py`: 0.109 s / 260 KB; base `1164_strings.py`: 0.078 s / 436 KB; cambio respecto a la base: tiempo +39.7%, memoria -40.4%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1164_strings.cpp`; fuente que cubre `1164_strings_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 46/46.

- Go: base didáctica preferida `1164_strings.go`; fuente que cubre `1164_strings.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1164_strings.java`; fuente que cubre `1164_strings.java`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Python/PyPy: base didáctica preferida `1164_strings.py`; fuente que cubre `1164_strings_optimized.py`; puestos tiempo/memoria 7/2, registros de otros autores 12/12.

- Rust: base didáctica preferida `1164_strings.rs`; fuente que cubre `1164_strings.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1164_strings.cpp](1164_strings.cpp) | G++ 13.2 x64 | strings | O(N M + W) | AC | 0.015 s | 380 KB | 11283052 |
| [1164_strings.go](1164_strings.go) | Go 1.14 x64 | strings | O(N M + W) | AC | 0.031 s | 1184 KB | 11283056 |
| [1164_strings.java](1164_strings.java) | Java 1.8 | strings | O(N M + W) | AC | 0.109 s | 1640 KB | 11283063 |
| [1164_strings.py](1164_strings.py) | Python 3.12 x64 | strings | O(N M + W) | AC | 0.078 s | 436 KB | 11283059 |
| [1164_strings.rs](1164_strings.rs) | Rust 1.75 x64 | strings | O(N M + W) | AC | 0.015 s | 220 KB | 11283064 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1164_strings_optimized.cpp](1164_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(N M + W) | AC | 0.015 s | 104 KB | 11308330 |
| [1164_strings_optimized.py](1164_strings_optimized.py) \* | PyPy 3.10 x64 | strings | O(N M + W) | AC | 0.109 s | 260 KB | 11309679 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
