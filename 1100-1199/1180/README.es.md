# 1180. Quién gana cuando las piedras se toman en potencias de dos

[Timus 1180](https://acm.timus.ru/problem.aspx?space=1&num=1180) · dificultad 89 · games

Problema original de Dmitry Filimonenkov, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N ≤ 10²⁵⁰` piedras. Dos jugadores retiran por turnos una potencia de
dos (1, 2, 4, 8, …) de piedras; gana quien se lleva la última. Hay que
decir quién gana con juego perfecto y, si es el primero, el menor número
de piedras que puede tomar en la primera jugada sin perder la victoria.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, con hasta 251 dígitos.

## Salida

`2`, o `1` y la menor primera jugada ganadora.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
1
2
```

## Solución

Ninguna potencia de dos es divisible entre 3, así que desde un múltiplo
de 3 toda jugada deja un montón que no lo es. Desde cualquier otro montón,
tomar 1 o 2 piedras, el resto módulo 3, deja un múltiplo de 3. El cero es
múltiplo de 3, así que quien deja siempre un múltiplo de 3 se lleva la
última piedra. El segundo jugador gana exactamente cuando `N` es divisible
entre 3; si no, gana el primero, y la menor jugada ganadora es `N mod 3`,
porque ninguna otra jugada de 1 o 2 deja un múltiplo de 3. `N mod 3` es la
suma de dígitos módulo 3. `O(dígitos)`.

Detalles a tener en cuenta:

- `N` tiene hasta 251 dígitos, así que un entero de 64 bits no basta;
- la jugada ganadora debe ser la menor, y tanto 1 como 2 son potencias de
  dos, así que es el propio resto.

Las respuestas se comprobaron contra una búsqueda directa del juego para
todo `N` hasta 399.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) suman las cifras una a una a
medida que las leen con `getchar` y `System.in.read`, sin guardar el
número como cadena, y escriben la breve respuesta byte a byte. C++:
88 KB en lugar de 384 KB, con el mismo tiempo; Java: 0.093 s en lugar de
0.125 s y 328 KB en lugar de 1568 KB.

## Notas por lenguaje

- Todos los lenguajes suman los dígitos módulo 3 leyéndolos como texto.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1180_games.cpp](1180_games.cpp) | G++ 13.2 x64 | games | O(digits) | AC | 0.015 s | 384 KB | 11283296 |
| [1180_games.go](1180_games.go) | Go 1.14 x64 | games | O(digits) | AC | 0.015 s | 1104 KB | 11283304 |
| [1180_games.java](1180_games.java) | Java 1.8 | games | O(digits) | AC | 0.125 s | 1568 KB | 11283311 |
| [1180_games.py](1180_games.py) | Python 3.12 x64 | games | O(digits) | AC | 0.078 s | 400 KB | 11283308 |
| [1180_games.rs](1180_games.rs) | Rust 1.75 x64 | games | O(digits) | AC | 0.015 s | 212 KB | 11283312 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1180_games_optimized.cpp](1180_games_optimized.cpp) \* | G++ 13.2 x64 | games | O(digits) | AC | 0.031 s | 88 KB | 11303574 |
| [1180_games_optimized.java](1180_games_optimized.java) | Java 1.8 | games | O(digits) | AC | 0.093 s | 328 KB | 11303452 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
