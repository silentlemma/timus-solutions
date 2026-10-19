# 1856. Guerra y paz

[Timus 1856](https://acm.timus.ru/problem.aspx?space=1&num=1856) · dificultad 3485 · games

Problema original de Fedor Fominykh, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ejército de liches está repartido entre las n guarniciones. Cada uno
de dos hechizos de señal manda a la vez las tropas de cada guarnición i
a una guarnición fija, aᵢ con el primero y bᵢ con el segundo. Cada día a
mediodía Vidomina lanza uno de los hechizos, intentando reunir todo el
ejército en una guarnición, y cada medianoche Korbu lanza uno,
intentando impedirlo; empieza Vidomina. Si ambos juegan de forma
óptima, ¿se puede reunir el ejército?

## Entrada

n (2 ≤ n ≤ 1000), luego los pares aᵢ, bᵢ de cada guarnición.

## Salida

"War" si Vidomina puede reunir el ejército, "Peace" si no.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 1
1 2
```

Salida:

```
Peace
```

### Ejemplo 2

Entrada:

```
2
2 2
2 1
```

Salida:

```
War
```

## Solución

Las guarniciones ocupadas forman un conjunto que los hechizos llevan
hacia delante y que nunca crece. El ejército se puede reunir
exactamente cuando todo par de guarniciones se puede forzar a juntarse.
Si algún par (u, v) puede mantenerse separado para siempre, las tropas
que empiezan allí nunca se encuentran. Si todo par se puede juntar,
Vidomina toma dos guarniciones ocupadas, sigue la estrategia de ese par
hasta que se unan y repite con menos guarniciones ocupadas cada vez.

Así que el juego se juega sobre pares, como mucho 499 500. Un par está
ganado para Vidomina cuando uno de sus hechizos o bien lo une o bien
deja a Korbu solo respuestas que lo unen o llevan a pares ya ganados.
Se resuelve hacia atrás: para cada par y cada hechizo de ella se
cuentan las respuestas de Korbu que mantienen el par separado, se
listan para cada par las jugadas (par, hechizo) que llevan a él, y se
empieza por los pares con un hechizo de cuenta cero. Cuando un par se
gana, cada jugada que lleva a él pierde una respuesta abierta, y una
cuenta que llega a cero gana su par. La respuesta es "War" si se ganan
todos los pares. `O(n²)` en tiempo y memoria.

En el primer ejemplo ambos hechizos son permutaciones, así que las dos
guarniciones nunca se unen. En el segundo, el primer hechizo manda las
dos guarniciones a la guarnición 2 de inmediato.

Trampas:

- la respuesta de Korbu puede unir el par por sí misma; esa respuesta
  no está abierta;
- reunir par a par funciona porque el conjunto ocupado nunca crece,
  aunque Korbu mueva entre medias las demás tropas;
- el espacio de estados de conjuntos enteros es demasiado grande;
  bastan los pares.

Las respuestas coinciden con una búsqueda del juego sobre todos los
conjuntos de guarniciones en trescientos casos de hasta seis
guarniciones y con una implementación aceptada independiente en las
pruebas grandes. La solución en Python corre en PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1856_games.cpp](1856_games.cpp) | G++ 13.2 x64 | games | O(n^2) | AC | 0.093 s | 37828 KB |
| [1856_games.go](1856_games.go) | Go 1.14 x64 | games | O(n^2) | AC | 0.187 s | 56936 KB |
| [1856_games.java](1856_games.java) | Java 1.8 | games | O(n^2) | AC | 0.234 s | 38620 KB |
| [1856_games.py](1856_games.py) | PyPy 3.10 x64 | games | O(n^2) | AC | 0.500 s | 50420 KB |
| [1856_games.rs](1856_games.rs) | Rust 1.75 x64 | games | O(n^2) | AC | 0.140 s | 39544 KB |
