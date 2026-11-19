# 1023. Elegir el límite de jugada que hace ganar al segundo jugador

[Timus 1023](https://acm.timus.ru/problem.aspx?space=1&num=1023) · dificultad 218 · games, number_theory

Problema original de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores retiran por turnos de 1 a `L` botones de un montón de `K`
botones; gana quien toma el último. El primer jugador ha elegido `K`
(`3 ≤ K ≤ 10^8`); ahora el segundo elige `L` con `2 ≤ L < K`. Encuentra el
menor `L` con el que el segundo jugador gana contra cualquier juego del
primero, o imprime 0 si no existe.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`K`.

## Salida

El menor `L` ganador, o 0.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1023_games_number_theory_optimized.java` (Java 1.8): 14 pruebas del repositorio.

- `1023_games_number_theory_optimized.py` (PyPy 3.10 x64): 14 pruebas del repositorio; 1003 comparaciones adicionales de fuente exacta.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
35
```

Salida:

```
4
```

## Solución

Con jugadas de `1..L`, las posiciones perdedoras para quien mueve
son exactamente los múltiplos de `L + 1`, incluido el montón vacío.
Desde un múltiplo positivo, cualquier movimiento legal deja un no múltiplo.
Desde un no múltiplo, retirar el resto módulo `L + 1` deja un múltiplo;
es una jugada legal y no supera el montón. La inducción demuestra la
afirmación. El segundo puede forzar la victoria si y solo si `(L + 1)`
divide a `K`.

Buscamos el menor divisor `d ≥ 3`, y respondemos `L = d − 1`. `d = K`
siempre es válido, así que una entrada válida nunca produce cero.
Las versiones sencillas prueban todos los enteros `3..sqrt(K)` en orden.
Si ninguno divide, el factor complementario menor de un divisor superior
a la raíz solo puede ser 1 o 2. Quedan `K/2`, si es entero y al menos 3,
o `K` en otro caso. En particular, `K = 4` requiere `d = 4`, no 2.
El primer divisor encontrado es mínimo, lo que demuestra la respuesta.
Tiempo `O(sqrt(K))`, espacio auxiliar `O(1)`. Se conservan sin cambios
las cinco bases Accepted originales.

## Soluciones optimizadas

Se conserva la prueba por el menor divisor legal: respuesta d-1 con d>=3mínimo divisor de K. Primero3,4y5; los restantes candidatos son coprimos con30 y los saltos(4,2,4,2,4,6,2,6) recorren todos los posibles factores pequeños restantes. Si no aparece ninguno hasta sqrt(K), queda K/2si es par, o K. Python prueba cuatro candidatos sucesivos por vuelta, manteniendo orden y condiciones exactas, reduciendo bucle caliente/JIT sin importar su módulo de control. Java conserva la prueba compacta de impares. Tiempo O(sqrt(K)), estado constante;1003comprobaciones adicionales, con primos grandes y compuestos máximos, coinciden con búsqueda directa independiente.

- `1023_games_number_theory_optimized.java`: 0.109 s / 392 KB; base `1023_games_number_theory.java`: 0.109 s / 1576 KB; cambio respecto a la base: tiempo -0.0%, memoria -75.1%.
- `1023_games_number_theory_optimized.py`: 0.140 s / 280 KB; base `1023_games_number_theory.py`: 0.078 s / 400 KB; cambio respecto a la base: tiempo +79.5%, memoria -30.0%.

`1023_games_number_theory_optimized.rs`. Se conserva la búsqueda del menor divisor admisible, incluido el caso alternativo par. El límite d<=K/d evita calcular el cuadrado de d. Solo se guardan el divisor actual y la entrada: O(√K) tiempo y O(1) espacio auxiliar. Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1023_games_number_theory.rs`: tiempo 0.015 s → 0.015 s; memoria 220 KB → 56 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1023_games_number_theory_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1023_games_number_theory.cpp](1023_games_number_theory.cpp) | G++ 13.2 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 128 KB | 11278278 |
| [1023_games_number_theory.go](1023_games_number_theory.go) | Go 1.14 x64 | games, number_theory | O(sqrt(K)) | AC | 0.031 s | 1072 KB | 11278279 |
| [1023_games_number_theory.java](1023_games_number_theory.java) | Java 1.8 | games, number_theory | O(sqrt(K)) | AC | 0.109 s | 1576 KB | 11278281 |
| [1023_games_number_theory.py](1023_games_number_theory.py) | Python 3.12 x64 | games, number_theory | O(sqrt(K)) | AC | 0.078 s | 400 KB | 11278280 |
| [1023_games_number_theory.rs](1023_games_number_theory.rs) | Rust 1.75 x64 | games, number_theory | O(sqrt(K)) | AC | 0.015 s | 220 KB | 11278282 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1023_games_number_theory_optimized.java](1023_games_number_theory_optimized.java) | Java 1.8 | games, number_theory | O(sqrt(K)) time; O(1) space | AC | 0.109 s | 392 KB | 11308324 |
| [1023_games_number_theory_optimized.py](1023_games_number_theory_optimized.py) \* | PyPy 3.10 x64 | games, number_theory | O(sqrt(K)) time; O(1) space | AC | 0.140 s | 280 KB | 11309754 |
| [1023_games_number_theory_optimized.rs](1023_games_number_theory_optimized.rs) \* | Rust 1.75 x64 | games, number_theory | O(√K) | AC | 0.015 s | 56 KB | 11325081 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
