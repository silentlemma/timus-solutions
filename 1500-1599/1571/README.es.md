# 1571. Intérpretes

[Timus 1571](https://acm.timus.ru/problem.aspx?space=1&num=1571) · dificultad 451 · constructive

Problema original de Sergey Pupyrev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de N ≤ 100 equipos de obra habla un idioma. Un intérprete sabe
dos idiomas cualesquiera. Cada dos equipos deben poder hablar, y ningún
otro equipo debe entender su conversación. Hay que imprimir el menor
número de intérpretes con sus idiomas como `idioma1-idioma2`, o
`Impossible`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego el idioma de cada equipo.

## Salida

El número de intérpretes y sus pares de idiomas, o `Impossible`. Se
acepta cualquier conjunto óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
russian
french
german
```

Salida:

```
3
russian-english
english-german
english-french
```

## Solución

Si dos equipos comparten idioma, un tercer equipo, si lo hay, no puede
hablar con el primero sin que el segundo lo entienda; con solo esos dos
equipos no hace falta nadie. Si no, sean distintos los k idiomas. Un
equipo no necesita a nadie, y dos equipos necesitan un intérprete de
sus dos idiomas.

Para k ≥ 3, una conversación que pasa por el idioma de otro equipo la
oye ese equipo, así que entre cada dos equipos los intérpretes deben
formar una cadena cuyos idiomas interiores no hable ningún equipo. Si
los intérpretes usaran solo los idiomas de los equipos, formarían un
grafo conexo sobre esos k idiomas, y con solo k − 1 aristas sería un
árbol, donde alguna cadena pasa por un tercer idioma. Así que hacen
falta k intérpretes, y k bastan: el idioma de cada equipo emparejado con
un idioma que nadie habla, como english. Si un equipo habla english, el
idioma central es el primer nombre libre de una o dos letras: los
idiomas de la respuesta tampoco pueden pasar de diez letras, y 100
equipos no pueden ocupar los 702 nombres así. `O(N)`.

Detalles a tener en cuenta:

- dos equipos de un mismo idioma no necesitan a nadie, pero tres equipos
  con un idioma repetido son imposibles (pruebas 03, 05);
- un equipo puede hablar english, y un nombre inventado más largo para
  el idioma central se rechaza (pruebas 06, 08);
- se aceptan otras respuestas, como un triángulo de pares directos para
  tres equipos, así que un verificador comprueba la privacidad.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1571_constructive.cpp](1571_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 436 KB |
| [1571_constructive.go](1571_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 1144 KB |
| [1571_constructive.java](1571_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.156 s | 1712 KB |
| [1571_constructive.py](1571_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.078 s | 548 KB |
| [1571_constructive.rs](1571_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 456 KB |
