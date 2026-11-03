# 1081. La K-ésima cadena binaria sin dos unos seguidos

[Timus 1081](https://acm.timus.ru/problem.aspx?space=1&num=1081) · dificultad 271 · dp

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Considera todas las cadenas de longitud `N` (`0 < N < 44`) formadas por 0
y 1 sin dos unos seguidos, ordenadas lexicográficamente. Imprime la
`K`-ésima (`0 < K < 10^9`), o `-1` si hay menos de `K`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`.

## Salida

La cadena, o `-1`.

## Evaluación

Comparar la cadena binaria de N caracteres, o -1 si el rango no existe. El nuevo código Python exacto pasó 15 pruebas del repositorio con PyPy 3.10. Además 239 comprobaciones exhaustivas de cadenas cortas y rangos. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
```

Salida:

```
000
```

## Solución

Sea `count[r]` el número de cadenas válidas de longitud `r`: una cadena
empieza o bien con 0 y cualquier resto válido, o bien con `10` y
cualquier resto válido, así que `count[r] = count[r − 1] + count[r − 2]`
con `count[0] = 1` y `count[1] = 2`, los números de Fibonacci.

La respuesta se construye de izquierda a derecha. Si el carácter anterior
es 1, este debe ser 0. Si no, las cadenas con 0 aquí van primero en el
orden, y hay `count[rest]` de ellas, donde `rest` es el número de
posiciones después de esta (el 0 no restringe el siguiente carácter). Si
`K ≤ count[rest]`, se escribe 0; si no, se resta `count[rest]` a `K` y se
escribe 1. Si desde el principio `K > count[N]`, se imprime `-1`. `O(N)`.

Detalles a tener en cuenta:

- `count[43] = 1 134 903 170` es mayor que cualquier `K`, así que para
  `N = 43` siempre hay respuesta; aun así los conteos se guardan en
  enteros de 64 bits;
- tras un 1 el siguiente carácter es forzoso y `K` no cambia;
- las cadenas se cuentan desde `K = 1`, la cadena de solo ceros.

Las respuestas se comprobaron con la lista ordenada de todas las cadenas
válidas para `N ≤ 20`, y para cadenas más largas calculando de vuelta la
posición de la respuesta con un conteo memorizado.

## Soluciones optimizadas

Se conserva la tabla clara de Fibonacci. Las variantes compactas retienen dos conteos vecinos y revierten la recurrencia al reconstruir. Si el rango residual desde cero alcanza el conteo con prefijo cero, lo restan y emiten uno; en otro caso cero. Tras un uno, el intervalo residual queda por debajo del siguiente conteo cero, forzando el siguiente bit sin caso especial. El total detecta rangos inválidos. Python acumula bits en un entero y lo formatea con N posiciones: conserva la respuesta de O(N) bits, sin tabla de conteos.

- `1081_dp_optimized.java`: 0.078 s / 372 KB; base `1081_dp.java`: 0.125 s / 1640 KB; cambio respecto a la base: tiempo -37.6%, memoria -77.3%.
- `1081_dp_optimized.py`: 0.125 s / 284 KB; base `1081_dp.py`: 0.093 s / 476 KB; cambio respecto a la base: tiempo +34.4%, memoria -40.3%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1081_dp.cpp`; fuente que cubre `1081_dp.cpp`; puestos tiempo/memoria 1/6, registros de otros autores 93/93.

- Go: base didáctica preferida `1081_dp.go`; fuente que cubre `1081_dp.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1081_dp.java`; fuente que cubre `1081_dp_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1081_dp.py`; fuente que cubre `1081_dp_optimized.py`; puestos tiempo/memoria 22/2, registros de otros autores 22/22.

- Rust: base didáctica preferida `1081_dp.rs`; fuente que cubre `1081_dp.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1081_dp.cpp](1081_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 200 KB | 11279006 |
| [1081_dp.go](1081_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.015 s | 1084 KB | 11279009 |
| [1081_dp.java](1081_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1640 KB | 11279012 |
| [1081_dp.py](1081_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 476 KB | 11279010 |
| [1081_dp.rs](1081_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 216 KB | 11279014 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1081_dp_optimized.java](1081_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.078 s | 372 KB | 11309292 |
| [1081_dp_optimized.py](1081_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.125 s | 284 KB | 11309684 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
