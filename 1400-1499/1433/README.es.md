# 1433. Tetraedros

[Timus 1433](https://acm.timus.ru/problem.aspx?space=1&num=1433) · dificultad 264 · bruteforce, math

Problema original de Pavel Egorov y Stanislav Vasiliev, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos tetraedros regulares del mismo tamaño tienen cada cara pintada de
R, G, B o Y. Los colores se dan en el mismo orden para ambos: la base,
la cara delantera izquierda, la delantera derecha y la trasera. Hay que
imprimir «equal» si un tetraedro puede girarse hasta verse exactamente
como el otro, y «different» si no.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos líneas de cuatro letras.

## Salida

«equal» o «different».

## Evaluación

Comparar el token exacto en minúsculas equal o different. El nuevo código Python exacto pasó 12 pruebas del repositorio con PyPy 3.10. Además 1600 pares de colores con grupo de rotaciones independiente. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
RGRB
GRRB
```

Salida:

```
equal
```

## Solución

Un giro del tetraedro permuta sus cuatro caras, y los giros dan
exactamente las 12 permutaciones pares: un giro sobre un eje que pasa
por un vértice mueve tres caras en ciclo, medio giro sobre un eje que
pasa por dos aristas opuestas intercambia dos pares, y una permutación
impar, como un solo intercambio, sería una imagen especular. Así que se
prueban los 24 órdenes de las caras, se conservan los que tienen un
número par de inversiones y se mira si alguno convierte la primera
coloración en la segunda. `O(1)`.

Detalles a tener en cuenta:

- las imágenes especulares son distintas: con cuatro colores distintos,
  intercambiar dos caras no es un giro (pruebas 03, 11);
- con un color repetido, cualquier disposición de los mismos colores es
  igual, porque intercambiar las dos caras iguales corrige la paridad
  (pruebas 05, 07, 08, 12).

## Soluciones optimizadas

Las bases siguen enumerando las doce rotaciones propias. Las variantes matemáticas comparan los multiconjuntos de colores. Si se repite un color, intercambiar dos caras indistinguibles cambia la paridad sin cambiar la coloración: siempre existe un representante par. Con cuatro colores distintos la permutación es única y corresponde a una rotación propia si su número de inversiones es par. Se evita construir todas las coloraciones rotadas. Son cuatro caras y comparaciones exactas. Python también usa flujos de texto existentes.

- `1433_math.cpp`: 0.015 s / 104 KB; base `1433_bruteforce.cpp`: 0.015 s / 360 KB; cambio respecto a la base: tiempo -0.0%, memoria -71.1%.
- `1433_math.java`: 0.093 s / 348 KB; base `1433_bruteforce.java`: 0.125 s / 1568 KB; cambio respecto a la base: tiempo -25.6%, memoria -77.8%.
- `1433_math.py`: 0.109 s / 284 KB; base `1433_bruteforce.py`: 0.078 s / 440 KB; cambio respecto a la base: tiempo +39.7%, memoria -35.5%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1433_bruteforce.cpp`; fuente que cubre `1433_math.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 48/48.

- Go: base didáctica preferida `1433_bruteforce.go`; fuente que cubre `1433_bruteforce.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1433_bruteforce.java`; fuente que cubre `1433_math.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1433_bruteforce.py`; fuente que cubre `1433_math.py`; puestos tiempo/memoria 8/2, registros de otros autores 15/15.

- Rust: base didáctica preferida `1433_bruteforce.rs`; fuente que cubre `1433_bruteforce.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1433_bruteforce.cpp](1433_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 360 KB | 11286216 |
| [1433_bruteforce.go](1433_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1084 KB | 11286217 |
| [1433_bruteforce.java](1433_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1568 KB | 11286219 |
| [1433_bruteforce.py](1433_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 440 KB | 11286218 |
| [1433_bruteforce.rs](1433_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 224 KB | 11286220 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1433_math.cpp](1433_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 104 KB | 11309265 |
| [1433_math.java](1433_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 348 KB | 11309266 |
| [1433_math.py](1433_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 284 KB | 11309683 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
