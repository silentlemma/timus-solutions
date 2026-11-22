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

## Soluciones optimizadas

La implementación rápida conserva la comparación lexicográfica de goles totales y goles fuera de casa, pero solo prueba los extremos del rival. Fijados nuestros goles g, aumentar los del rival nunca mejora nuestra situación. Por tanto, existe una posibilidad de avanzar exactamente si existe contra 0 goles, y una posibilidad de quedar eliminado exactamente si existe contra 30. Se recorren nuestros 31 resultados y se conservan el primero que permite avanzar y el último que permite perder. El empate completo permite ambos desenlaces por la moneda. Son 62 comparaciones por caso en lugar de hasta 961 parejas; con el límite de goles fijo, el tiempo sigue siendo O(t).

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 44 KB frente a 268 KB.

## Notas por lenguaje

Los cinco archivos base siguen enumerando todos los resultados del segundo partido. Los rápidos conservan las reglas de comparación y solo prueban los dos extremos del rival. Java y Python analizan la frase fija línea por línea. Go usa manejadores estándar y Rust E/S acotada del C runtime con entrada C. Sus búferes de 2048 bytes contienen las 200 respuestas, cada una con dos números entre 0 y 30 y separadores.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1804_implementation.cpp](1804_implementation.cpp) | G++ 13.2 x64 | implementation | O(t) | AC | 0.015 s | 364 KB | 11328305 |
| [1804_implementation.go](1804_implementation.go) | Go 1.14 x64 | implementation | O(t) | AC | 0.015 s | 1216 KB | 11289992 |
| [1804_implementation.java](1804_implementation.java) | Java 1.8 | implementation | O(t) | AC | 0.14 s | 2548 KB | 11328306 |
| [1804_implementation.py](1804_implementation.py) | Python 3.12 x64 | implementation | O(t) | AC | 0.14 s | 552 KB | 11328307 |
| [1804_implementation.rs](1804_implementation.rs) | Rust 1.75 x64 | implementation | O(t) | AC | 0.031 s | 268 KB | 11328308 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1804_implementation_optimized.cpp](1804_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(t) | AC | 0.015 s | 116 KB | 11314652 |
| [1804_implementation_optimized.go](1804_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(t) | AC | 0.015 s | 336 KB | 11314653 |
| [1804_implementation_optimized.java](1804_implementation_optimized.java) | Java 1.8 | implementation | O(t) | AC | 0.093 s | 1088 KB | 11314657 |
| [1804_implementation_optimized.py](1804_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(t) | AC | 0.078 s | 420 KB | 11314659 |
| [1804_implementation_optimized.rs](1804_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(t) | AC | 0.031 s | 44 KB | 11314666 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
