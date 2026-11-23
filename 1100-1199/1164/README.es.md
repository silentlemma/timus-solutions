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

`1164_strings_optimized.java`. Java conserva 26 balances de letras: añade la cuadrícula, resta las palabras y emite los saldos positivos alfabéticamente. Toda colocación válida consume el mismo multiconjunto, sin buscar caminos. countLetters recorre directamente los bytes mayúsculos del token en un búfer recargable de 1024 bytes, sin cadenas por palabra, decodificación UTF-8 ni arreglos de caracteres. La respuesta aún usa StringBuilder. Con W letras de palabras y A letras de salida: tiempo O(N*M+W+A), espacio auxiliar O(A+26) más el búfer fijo. Conserva las bases didácticas.

Accepted exacto Java 1.8 #11327328: 0.093 s / 456 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 4/32, memoria 2/32. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11324785 era 0.109 s / 500 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1164_strings_optimized.java`: 0.093 s / 456 KB; base didáctica conservada `1164_strings.java`: 0.109 s / 1640 KB.

`1164_strings_optimized.rs`. Conserva 26 balances: añade letras del tablero y resta palabras. Procesa en flujo y emite restantes en orden sin texto completo ni cadena de respuesta. O(I+A) tiempo para I bytes y A letras, alfabeto constante.

Frente a `1164_strings.rs`: tiempo 0.015 s → 0.015 s; memoria 220 KB → 60 KB.

Toda colocación consume el mismo multiconjunto de letras. Se conservan los contadores claros y el C++ compacto. Python cuenta cada una de las 26 mayúsculas en la cuadrícula y las palabras concatenadas y emite las diferencias positivas en orden. El alfabeto constante mantiene tiempo lineal. Evita Counter y diccionarios separados, aunque conserva las cadenas. Usa flujos de texto existentes y escritura directa. La mejora confirmada es solo de memoria; el mayor tiempo se declara abajo.

- `1164_strings_optimized.cpp`: 0.015 s / 104 KB; base `1164_strings.cpp`: 0.015 s / 380 KB; cambio respecto a la base: tiempo -0.0%, memoria -72.6%.
- `1164_strings_optimized.py`: 0.109 s / 260 KB; base `1164_strings.py`: 0.078 s / 436 KB; cambio respecto a la base: tiempo +39.7%, memoria -40.4%.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1164_strings_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328513 (Go 1.14 x64): **0.015 s / 968 KB**. Comparación archivada: `1164_strings.go` (Go 1.14 x64) — 0.031 s / 1184 KB (#11283056).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1164_strings_optimized.py](1164_strings_optimized.py) | PyPy 3.10 x64 | strings | O(N M + W) | AC | 0.109 s | 260 KB | 11309679 |
| [1164_strings_optimized.java](1164_strings_optimized.java) | Java 1.8 | strings | O(N M + W + A) time; O(A + 26) space + fixed buffer | AC | 0.093 s | 456 KB | 11327328 |
| [1164_strings_optimized.rs](1164_strings_optimized.rs) | Rust 1.75 x64 | strings | O(I+A) time; O(26) space | AC | 0.015 s | 60 KB | 11325544 |
| [1164_strings_optimized.go](1164_strings_optimized.go) | Go 1.14 x64 | strings | O(N M + W) | AC | 0.015 s | 968 KB | 11328513 |
