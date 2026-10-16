# 1804. Las Ametralladoras en la eliminatoria

[Timus 1804](https://acm.timus.ru/problem.aspx?space=1&num=1804) · dificultad 411 · implementation

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos equipos juegan un partido en casa y otro fuera. Pasa el que marca
más goles en total; con totales iguales, el que marca más en el campo
rival; si también empatan, decide una moneda. Ningún equipo marca más
de 30 en un partido. Dado el primer partido, hallar el menor número de
goles que las Ametralladoras deben marcar en el segundo para tener
alguna opción de pasar, y el mayor que aún deja una opción a las
rivales.

## Entrada

t (1 ≤ t ≤ 200), luego t líneas de la forma "The Machinegunners played
where game, scored x goals, and conceded y goals.", donde where es home
o away, 0 ≤ x, y ≤ 30.

## Salida

Para cada línea, los dos números.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
The Machinegunners played home game, scored 28 goals, and conceded 0 goals.
The Machinegunners played home game, scored 1 goals, and conceded 1 goals.
```

Salida:

```
0 1
1 29
```

## Solución

Se prueban todos los resultados del segundo partido, g goles de las
Ametralladoras y o de las rivales, 31 × 31 pares. Se comparan los pares
(total, goles fuera) de ambos equipos. Las Ametralladoras pueden pasar
si el suyo es al menos el de las rivales y pueden quedar fuera si es
como mucho, así que un empate completo permite ambas cosas. El primer g
que puede pasar y el último g que puede fallar son las respuestas. Los
goles fuera son la g de las Ametralladoras y la y de las rivales si el
primer partido fue en casa, y si no, x y o. `O(t)`, con 961 pares cada
uno.

En la primera línea, tras 28:0 en casa, incluso 0:28 fuera es un
empate completo, así que 0 goles dejan una opción. Con 1 gol, 1:30
todavía pierde, pero con 2 goles el peor caso, 2:30, gana por goles
fuera.

Trampas:

- un empate en ambos criterios va a la moneda, así que cuenta como
  opción de pasar y como opción de fallar;
- de qué equipo salen del segundo partido los goles fuera depende de
  dónde se jugó el primero;
- los goles de un partido no pasan de 30.

Las respuestas coinciden con una implementación aceptada independiente
en 600 primeros partidos aleatorios y en todos los resultados extremos
y ajustados en ambos campos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1804_implementation.cpp](1804_implementation.cpp) | G++ 13.2 x64 | implementation | O(t) | AC | 0.031 s | 388 KB |
| [1804_implementation.go](1804_implementation.go) | Go 1.14 x64 | implementation | O(t) | AC | 0.015 s | 1216 KB |
| [1804_implementation.java](1804_implementation.java) | Java 1.8 | implementation | O(t) | AC | 0.109 s | 2600 KB |
| [1804_implementation.py](1804_implementation.py) | Python 3.12 x64 | implementation | O(t) | AC | 0.156 s | 520 KB |
| [1804_implementation.rs](1804_implementation.rs) | Rust 1.75 x64 | implementation | O(t) | AC | 0.015 s | 268 KB |
