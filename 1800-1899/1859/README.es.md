# 1859. Última temporada de Team.GOV

[Timus 1859](https://acm.timus.ru/problem.aspx?space=1&num=1859) · dificultad 3827 · greedy

Problema original de Mikhail Rubinchik (idea de Dmitry Kuznetsov), del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una delegación de 6n personas viaja en n bloques de un coche cama; cada
bloque tiene cuatro plazas de compartimento y dos laterales. Cada
persona quiere un tipo de plaza, y cada una quiere viajar en el mismo
bloque que todos sus amigos. Repartir la delegación en bloques sin
decepcionar a nadie; se sabe que hay solución.

## Entrada

n (1 ≤ n ≤ 1000), una cadena de 6n bits (1 para plaza de compartimento,
0 para lateral), luego m (0 ≤ m ≤ 15n) y los m pares de amigos.

## Salida

n líneas con las seis personas de cada bloque. Se acepta cualquier
reparto válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
001111001111
2
1 2
7 8
```

Salida:

```
1 2 3 4 5 6
7 8 9 10 11 12
```

## Solución

La amistad une a las personas en grupos que deben compartir bloque, y un
grupo solo importa por (a, b): a personas que quieren plaza de
compartimento y b que quieren lateral. Con solo dos plazas laterales,
un bloque lleva o bien un grupo con b = 2, o bien dos grupos con b = 1
(las mitades), y las plazas de compartimento que quedan las ocupan los
grupos con b = 0, los rellenos.

Rellenar es empaquetar en una dimensión rellenos de tamaños 1 … 4 en
las plazas de compartimento libres de los bloques. Los de cuatro
necesitan un bloque con 4 libres. Uno de tres va primero a un bloque
con 3 libres: intercambiarlo con el contenido de un bloque con 4 libres
nunca empeora. Los de dos caben después en lo que queda (un bloque con 2
o 3 libres toma uno, uno con 4 toma dos), y los de uno llenan el resto.
Así, para números dados c₄, c₃, c₂ de bloques con 4, 3 y 2 plazas
libres, los rellenos caben exactamente cuando se cumplen tres
desigualdades.

Falta cómo emparejar las mitades: un par (a₁, a₂) deja 4 − a₁ − a₂
plazas libres. Juntar las plazas libres de dos bloques en uno nunca
estorba, y eso decide casi todo. Un tres emparejado con un cero, con un
uno emparejado en otra parte, se puede cambiar por un par (3, 1) y un
par con un cero, así que los treses toman tantos unos como pueden. Dos
pares (0, 2) pasan a ser (2, 2) y (0, 0), así que queda como mucho un
(0, 2). Lo que queda por elegir es el número de pares (1, 2) y de pares
(1, 1). Para cada número de pares (1, 2) las desigualdades limitan los
pares (1, 1) a un intervalo en el que el sitio para los de dos primero
crece y luego decrece, así que basta comprobar el punto de giro y sus
vecinos. Hay como mucho 2000 mitades, así que la búsqueda es lineal, y
luego los bloques se construyen y se rellenan en el mismo orden que
supuso la comprobación. `O(n + m)`.

En el ejemplo los grupos {1, 2} y {7, 8} quieren cada uno las dos plazas
laterales de un bloque, y todos los demás son rellenos que quieren
plaza de compartimento; cuatro cualesquiera completan cada bloque.

Trampas:

- un tres no debe ir a un bloque con 4 libres mientras quede abierto un
  bloque con exactamente 3;
- emparejar las mitades con avidez por tamaño falla: (1, 1) con (0, 0)
  y dos pares (1, 0) dejan plazas libres distintas, y cuál hace falta
  depende de los rellenos;
- la respuesta no es única, así que la salida la comprueba un
  verificador.

Los repartos pasan un verificador en 10 000 delegaciones aleatorias de
hasta 36 personas, la mitad formadas por grupos con una plaza lateral, y
en las pruebas más grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1859_greedy.cpp](1859_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.031 s | 692 KB |
| [1859_greedy.go](1859_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.062 s | 1908 KB |
| [1859_greedy.java](1859_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.125 s | 3364 KB |
| [1859_greedy.py](1859_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.109 s | 2564 KB |
| [1859_greedy.rs](1859_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.046 s | 812 KB |
