# 1255. Meter ataúdes de 1 × K en un cuadrado

[Timus 1255](https://acm.timus.ru/problem.aspx?space=1&num=1255) · dificultad 282 · math

Problema original de Stanislav Vasilyev y Alexey Lakhtin, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

¿Cuántos rectángulos de 1 × K (ataúdes) caben, sin solaparse y paralelos
a los lados, en un cuadrado de N × N (1 < N, K < 10 000)?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K.

## Salida

El mayor número de ataúdes.

## Evaluación

Comparar un token entero exacto, ignorando espacios de formato. El nuevo código Python exacto pasó 16 pruebas del repositorio con PyPy 3.10. Las otras variantes conservan sus propias pruebas de destino y Accepted exactos. La salida se compara según el verificador del problema.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
```

Salida:

```
8
```

## Solución

Si K > N no cabe nada. Si no, se escribe N = qK + r con 0 ≤ r < K y
s = min(r, K − r). La respuesta es

```text
(N² − s²) / K
```

y siempre es entera, porque N ≡ r y por tanto N² ≡ r² ≡ (K − r)² módulo K.

Caben tantos:

- con r ≤ K/2, ataúdes tumbados a lo largo de las filas llenan las
  primeras qK columnas de cada fila, y ataúdes de pie a lo largo de las
  columnas llenan las últimas r columnas en todas las filas menos r,
  dejando vacía una esquina de r × r;
- con r > K/2, cuatro bloques de ataúdes dispuestos como un molinillo
  alrededor del centro dejan un hueco de (K − r) × (K − r).

No caben más: se colorea cada casilla con `(fila + columna) mod K`. Un
ataúd cubre K casillas seguidas de una fila o columna, así que
exactamente una de cada color, y el número de ataúdes es como mucho el
tamaño de la clase de color más pequeña, que contando por las diagonales
resulta ser exactamente (N² − s²) / K. `O(1)`.

Detalles a tener en cuenta:

- el cuadrado sobrante tiene lado min(r, K − r), no r: con N = 7, K = 4,
  r = 3 pero solo queda un hueco de 1 × 1 y caben 12 ataúdes (prueba 08);
- N² es como máximo 99 980 001 (N = 9999, prueba 03), que aún cabe en 32 bits.

La fórmula se comparó con una búsqueda exhaustiva para todos los N y K
de 2 a 7.

## Soluciones optimizadas

Se usa la misma fórmula entera del cuadrado de esquina: r=N mod K, s=min(r,K-r); si N>=K, (N*N-s*s)//K; en caso contrario cero. No hay redondeos ni tabla de respuestas. El archivo compacto lee el flujo de texto existente y escribe directamente el entero exacto. Su envío propio en PyPy acredita el ahorro; se declaran el intérprete y el aumento temporal. Se conservan las cinco bases.

- `1255_math_optimized.java`: 0.109 s / 320 KB; base `1255_math.java`: 0.125 s / 1600 KB; cambio respecto a la base: tiempo -12.8%, memoria -80.0%.
- `1255_math_optimized.py`: 0.140 s / 248 KB; base `1255_math.py`: 0.078 s / 376 KB; cambio respecto a la base: tiempo +79.5%, memoria -34.0%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1255_math.cpp`; fuente que cubre `1255_math.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 31/31.

- Go: base didáctica preferida `1255_math.go`; fuente que cubre `1255_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1255_math.java`; fuente que cubre `1255_math_optimized.java`; puestos tiempo/memoria 3/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1255_math.py`; fuente que cubre `1255_math_optimized.py`; puestos tiempo/memoria 6/1, registros de otros autores 7/7.

- Rust: base didáctica preferida `1255_math.rs`; fuente que cubre `1255_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1255_math.cpp](1255_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11284031 |
| [1255_math.go](1255_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1132 KB | 11284034 |
| [1255_math.java](1255_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1600 KB | 11284037 |
| [1255_math.py](1255_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 376 KB | 11284036 |
| [1255_math.rs](1255_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 220 KB | 11284039 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1255_math_optimized.java](1255_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 320 KB | 11309313 |
| [1255_math_optimized.py](1255_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.140 s | 248 KB | 11309692 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
