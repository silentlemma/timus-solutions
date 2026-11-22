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

`1195_games_optimized.java`. Java conserva el mismo negamax exacto de tres jugadas. Dos máscaras de nueve bits representan las fichas; las máscaras de filas, columnas y diagonales detectan victorias y una jugada ganadora retorna de inmediato. Siempre quedan tres casillas vacías, por lo que no hace falta memoización. Un búfer de entrada de 64 bytes sustituye las lecturas individuales del flujo; las tres respuestas permanecen iguales. Tiempo y espacio auxiliar O(1) en este tablero fijo. Los 1372 tableros válidos con seis fichas se compararon con un solucionador independiente sobre el tablero.

Accepted exacto Java 1.8 #11327339: 0.093 s / 372 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 3/25, memoria 2/25. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11309258 era 0.109 s / 352 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1195_games_optimized.java`: 0.093 s / 372 KB; base didáctica conservada `1195_games.java`: 0.109 s / 1544 KB.

`1195_games_optimized.rs`. Mantiene negamax en posición tras seis jugadas. Dos máscaras de nueve bits sustituyen vector mutable; ocho máscaras ganadoras sustituyen comparar ternas, con retorno inmediato al ganar. Sin memoización ni otras reglas. O(E!) búsqueda peor caso y O(E) pila para E huecos, acotados por 3×3. Entrada/salida por bytes conserva mensajes Crosses/Draw/Ouths exactos.

Frente a `1195_games.rs`: tiempo 0.046 s → 0.015 s; memoria 212 KB → 56 KB.

Se conservan minimax completo y las ocho líneas ganadoras. La entrada legal contiene tres cruces y tres círculos sin ganador: quedan solo tres casillas, sin tabla de todas las posiciones. Probar jugada, ganar inmediatamente si completa línea; en otro caso negar el resultado rival y maximizar. Tablero lleno es empate. Las versiones mutables restauran la casilla antes de todo retorno temprano. Python usa dos máscaras de nueve bits y otra de casillas libres, con el mismo árbol. La E/S directa reduce escáneres/flujos. Tres niveles fijos cuestan O(1); el nuevo Python se verificó en las1372posiciones legales con seis marcas.

- `1195_games_optimized.cpp`: 0.015 s / 100 KB; base `1195_games.cpp`: 0.015 s / 352 KB; cambio respecto a la base: tiempo -0.0%, memoria -71.6%.

- `1195_games_optimized.py`: 0.125 s / 280 KB; base `1195_games.py`: 0.078 s / 528 KB; cambio respecto a la base: tiempo +60.3%, memoria -47.0%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1195_games_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1195_games_optimized.java](1195_games_optimized.java) \* | Java 1.8 | games | O(1) | AC | 0.093 s | 372 KB | 11327339 |
| [1195_games_optimized.py](1195_games_optimized.py) \* | PyPy 3.10 x64 | games | O(1) | AC | 0.125 s | 280 KB | 11309730 |
| [1195_games_optimized.rs](1195_games_optimized.rs) \* | Rust 1.75 x64 | games | O(E!) search; O(E) stack | AC | 0.015 s | 56 KB | 11325545 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
