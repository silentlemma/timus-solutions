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

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1023_games_number_theory.cpp`; fuente que cubre `1023_games_number_theory.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 111/111.

- Go: base didáctica preferida `1023_games_number_theory.go`; fuente que cubre `1023_games_number_theory.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1023_games_number_theory.java`; fuente que cubre `1023_games_number_theory_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 15/15.

- Python/PyPy: base didáctica preferida `1023_games_number_theory.py`; fuente que cubre `1023_games_number_theory_optimized.py`; puestos tiempo/memoria 15/1, registros de otros autores 16/16.

- Rust: base didáctica preferida `1023_games_number_theory.rs`; fuente que cubre `1023_games_number_theory.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

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

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
