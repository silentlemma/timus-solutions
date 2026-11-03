# 1087. Un juego de quitar piedras en el que tomar la última pierde

[Timus 1087](https://acm.timus.ru/problem.aspx?space=1&num=1087) · dificultad 278 · games

Problema original de Anton Botov, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un montón tiene `n` piedras (`1 ≤ n ≤ 10000`). Dos jugadores quitan por
turnos `k₁`, `k₂`, … o `kₘ` piedras (`1 ≤ m ≤ 50`, `1 ≤ kᵢ ≤ n`); siempre
es posible mover. Quien toma la última piedra pierde. Imprime 1 si el
primer jugador gana con juego perfecto, y 2 si no.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y `m`, y luego `k₁ … kₘ`.

## Salida

1 o 2.

## Evaluación

La salida se compara por tokens. El candidato Python real coincide
con minimax recursivo independiente en 3711 partidas: tamaños 1 a 35,
movimiento 1 y subconjuntos de 2 a 8, con entradas duplicadas y reordenadas.
El oráculo sigue al jugador real y concede al contrario la victoria si
se toma la última piedra, sin la convención artificial del montón vacío.
Los tres candidatos reales pasaron además 12 entradas del repositorio
cada uno en Docker y tienen sus propios Accepted exactos. Las 3711
comprobaciones fueron ejecuciones Python, no 3711 de C++ y Java.

## Ejemplos

### Ejemplo 1

Entrada:

```
17 3
1 3 4
```

Salida:

```
2
```

## Solución

Sea `win[x]` que quien mueve con `x` piedras puede forzar la victoria.
Una jugada ganadora retira `k < x` y deja una posición perdedora:
existe tal `k` con `win[x − k] = false`. Retirar exactamente `x` pierde
inmediatamente y no puede ser ganador. Llenamos por `x` creciente;
toda dependencia es menor, así que la inducción prueba recurrencia y respuesta.

Las bases usan la convención equivalente `win[0] = true`: el jugador
anterior acaba de retirar la última piedra y perder. Pueden probar
`k ≤ x`, pues esa última jugada aporta `not win[0] = false`.
La garantía de jugada legal rige antes del final; no exige que aparezca
literalmente el movimiento 1. Repetir tamaños no cambia el resultado.
Tiempo `O(n m)`, almacenamiento lógico `O(n + m)`. Se conservan
sin cambios las cinco bases Accepted originales.

## Soluciones optimizadas

El método Python con bits procesa las posiciones perdedoras en orden creciente en vez de recorrer cada jugada en cada estado. Un desplazamiento de entero grande marca como ganadoras todas las posiciones que permiten llegar a una perdedora. Las posiciones menores ya están clasificadas, conservando la inducción de la DP escalar. El estado vacío no genera transiciones ganadoras: retirar la última piedra pierde. La normalización por la jugada mínima usa la prueba de la solución simple.

N' es la cantidad normalizada de piedras, M el número de jugadas, L las posiciones perdedoras y w la anchura de palabra del entero grande.

- `1087_games_optimized.cpp`: 0.015 s / 132 KB; base `1087_games.cpp`: 0.015 s / 204 KB; cambio respecto a la base: tiempo -0.0%, memoria -35.3%.
- `1087_games_optimized.java`: 0.125 s / 440 KB; base `1087_games.java`: 0.109 s / 1652 KB; cambio respecto a la base: tiempo +14.7%, memoria -73.4%.
- `1087_games_bitmask.py`: 0.062 s / 456 KB; base `1087_games.py`: 0.093 s / 568 KB; cambio respecto a la base: tiempo -33.3%, memoria -19.7%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1087_games.cpp`; versión que cubre `1087_games_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 92/92.

- Go: base didáctica preferida `1087_games.go`; versión que cubre `1087_games.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1087_games.java`; versión que cubre `1087_games_optimized.java`; puestos tiempo/memoria 4/1, registros de otros autores 5/5.

- Python/PyPy: base didáctica preferida `1087_games.py`; versión que cubre `1087_games_bitmask.py`; puestos tiempo/memoria 1/1, registros de otros autores 22/22.

- Rust: base didáctica preferida `1087_games.rs`; versión que cubre `1087_games.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1087_games.cpp](1087_games.cpp) | G++ 13.2 x64 | games | O(n·m) | AC | 0.015 s | 204 KB | 11279057 |
| [1087_games.go](1087_games.go) | Go 1.14 x64 | games | O(n·m) | AC | 0.031 s | 1092 KB | 11279058 |
| [1087_games.java](1087_games.java) | Java 1.8 | games | O(n·m) | AC | 0.109 s | 1652 KB | 11279060 |
| [1087_games.py](1087_games.py) | Python 3.12 x64 | games | O(n·m) | AC | 0.093 s | 568 KB | 11279059 |
| [1087_games.rs](1087_games.rs) | Rust 1.75 x64 | games | O(n·m) | AC | 0.015 s | 228 KB | 11279063 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1087_games_optimized.cpp](1087_games_optimized.cpp) | G++ 13.2 x64 | games | O((M+L) ceil(N'/w)) | AC | 0.015 s | 132 KB | 11308397 |
| [1087_games_optimized.java](1087_games_optimized.java) \* | Java 1.8 | games | O((M+L) ceil(N'/w)) | AC | 0.125 s | 440 KB | 11308400 |
| [1087_games_bitmask.py](1087_games_bitmask.py) | Python 3.12 x64 | games, bitmask | O((M+L) ceil(N'/w)) | AC | 0.062 s | 456 KB | 11309361 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
