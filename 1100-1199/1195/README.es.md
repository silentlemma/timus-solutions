# 1195. Quién gana una partida inacabada de tres en raya

[Timus 1195](https://acm.timus.ru/problem.aspx?space=1&num=1195) · dificultad 260 · games

Problema original de Leonid Volkov y Oleg Kats, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de tres en raya de 3×3 tiene exactamente tres cruces y tres
círculos y todavía ninguna línea completa; las cruces empezaron, así que
ahora les toca a ellas. Hay que hallar el resultado con juego perfecto de
ambos bandos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Tres líneas de `X`, `O` y `#` para una casilla vacía.

## Salida

`Crosses win`, `Ouths win` o `Draw`.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1195_games_optimized.cpp` (G++ 13.2 x64): 15 pruebas del repositorio; 1372 comparaciones adicionales de fuente exacta.

- `1195_games_optimized.java` (Java 1.8): 15 pruebas del repositorio; 1372 comparaciones adicionales de fuente exacta.

- `1195_games_optimized.py` (PyPy 3.10 x64): 15 pruebas del repositorio; 1372 comparaciones adicionales de fuente exacta.

## Ejemplos

### Ejemplo 1

Entrada:

```
XXO
#X#
#OO
```

Salida:

```
Ouths win
```

### Ejemplo 2

Entrada:

```
O#O
#X#
XOX
```

Salida:

```
Draw
```

### Ejemplo 3

Entrada:

```
XX#
XOO
#O#
```

Salida:

```
Crosses win
```

## Solución

Solo quedan tres casillas vacías, así que todo el árbol de juego tiene a
lo sumo `3·2·1` partidas. Lo resuelve un minimax sencillo: el bando que
juega prueba cada casilla vacía; una jugada que completa una línea gana,
y si no, el resultado es el contrario del mejor resultado del rival desde
ahí; un tablero lleno es tablas. `O(1)`.

Detalles a tener en cuenta:

- siempre juegan las cruces, porque ambos bandos han hecho tres jugadas;
- la comprobación de línea completa debe mirar la marca recién puesta, no
  las dos;
- la respuesta para los círculos se escribe `Ouths win`.

Las respuestas se compararon con una solución escrita aparte en los 1372
tableros con tres cruces, tres círculos y ninguna línea completa.

## Soluciones optimizadas

Se conservan minimax completo y las ocho líneas ganadoras. La entrada legal contiene tres cruces y tres círculos sin ganador: quedan solo tres casillas, sin tabla de todas las posiciones. Probar jugada, ganar inmediatamente si completa línea; en otro caso negar el resultado rival y maximizar. Tablero lleno es empate. Las versiones mutables restauran la casilla antes de todo retorno temprano. Python usa dos máscaras de nueve bits y otra de casillas libres, con el mismo árbol. La E/S directa reduce escáneres/flujos. Tres niveles fijos cuestan O(1); el nuevo Python se verificó en las1372posiciones legales con seis marcas.

- `1195_games_optimized.cpp`: 0.015 s / 100 KB; base `1195_games.cpp`: 0.015 s / 352 KB; cambio respecto a la base: tiempo -0.0%, memoria -71.6%.
- `1195_games_optimized.java`: 0.109 s / 352 KB; base `1195_games.java`: 0.109 s / 1544 KB; cambio respecto a la base: tiempo -0.0%, memoria -77.2%.
- `1195_games_optimized.py`: 0.125 s / 280 KB; base `1195_games.py`: 0.078 s / 528 KB; cambio respecto a la base: tiempo +60.3%, memoria -47.0%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1195_games.cpp`; fuente que cubre `1195_games_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 54/54.

- Go: base didáctica preferida `1195_games.go`; fuente que cubre `1195_games.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1195_games.java`; fuente que cubre `1195_games_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1195_games.py`; fuente que cubre `1195_games_optimized.py`; puestos tiempo/memoria 18/5, registros de otros autores 24/24.

- Rust: base didáctica preferida `1195_games.rs`; fuente que cubre `1195_games.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1195_games.cpp](1195_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 352 KB | 11283475 |
| [1195_games.go](1195_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.015 s | 1084 KB | 11283476 |
| [1195_games.java](1195_games.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 1544 KB | 11283479 |
| [1195_games.py](1195_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 528 KB | 11283478 |
| [1195_games.rs](1195_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 212 KB | 11283480 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1195_games_optimized.cpp](1195_games_optimized.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 100 KB | 11309257 |
| [1195_games_optimized.java](1195_games_optimized.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 352 KB | 11309258 |
| [1195_games_optimized.py](1195_games_optimized.py) \* | PyPy 3.10 x64 | games | O(1) | AC | 0.125 s | 280 KB | 11309730 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
