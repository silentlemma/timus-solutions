# 1487. Fútbol chino

[Timus 1487](https://acm.timus.ru/problem.aspx?space=1&num=1487) · dificultad 1241 · graphs

Problema original de Sergey Pupyrev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N equipos (2 ≤ N ≤ 1000) han jugado algunos partidos sin empates, dados
como una tabla de victorias, y los resultados son transitivos: si A
ganó a B y B ganó a C, A ya ha ganado a C o sin duda le ganará. A es más
fuerte que B si A ganó a B o a algún equipo más fuerte que B. A juega
mejor que B si A no
es más débil que ningún equipo más fuerte que B. Hay que responder
Q ≤ 50000 preguntas «¿juega A mejor que B?» con «YES» o «No».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N en la primera línea, seguido de N filas de exactamente N caracteres.
Un 1 en la fila i, columna j indica que el equipo i ha ganado al j;
las demás entradas son 0. Cada pareja ha jugado como máximo una vez.
Después viene Q y luego Q líneas A B, con 1 ≤ A, B ≤ N y A ≠ B;
los equipos están numerados del 1 al N.

## Salida

«YES» o «No» para cada pregunta.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
011
000
000
2
2 3
1 3
```

Salida:

```
No
YES
```

## Solución

«Más fuerte» es alcanzabilidad por las victorias, y las victorias forman
un grafo acíclico porque los resultados son transitivos. A no es más
débil que C cuando C no alcanza a A. Así que A juega mejor que B cuando
ningún equipo que alcanza a B alcanza también a A: los dos conjuntos de
equipos más fuertes son disjuntos.

Esos conjuntos son conjuntos de bits. Tomando los equipos en orden
topológico (algoritmo de Kahn sobre las victorias), el conjunto de un
equipo es la unión de los conjuntos de los equipos que le ganaron, más
esos equipos. Es una unión de conjuntos de bits por partido. Cada pregunta
es entonces una intersección. Con W palabras de almacenamiento por
conjunto, el tiempo en el peor caso es `O(N²·W + Q·W)`. C++ usa conjuntos
`std::bitset` fijos de 1000 bits; Go, Java y Rust usan ⌈N/64⌉ palabras de
64 bits. Python usa máscaras enteras de precisión arbitraria, por lo que
W cuenta los dígitos de la representación interna del entero.

Detalles a tener en cuenta:

- las respuestas son «YES» y «No», con distinto uso de mayúsculas
  (todas las pruebas);
- todo equipo juega mejor que uno sin nadie más fuerte, aunque le haya
  perdido (pruebas 02, 03);
- un ganador común por encima de ambos equipos da «No» en los dos
  sentidos (prueba 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1487_graphs.cpp](1487_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^2 W + Q W) | AC | 0.125 s | 2904 KB |
| [1487_graphs.go](1487_graphs.go) | Go 1.14 x64 | graphs | O(N^2 W + Q W) | AC | 0.140 s | 11660 KB |
| [1487_graphs.java](1487_graphs.java) | Java 1.8 | graphs | O(N^2 W + Q W) | AC | 0.156 s | 15288 KB |
| [1487_graphs.py](1487_graphs.py) | Python 3.12 x64 | graphs | O(N^2 W + Q W) | AC | 0.515 s | 20988 KB |
| [1487_graphs.rs](1487_graphs.rs) | Rust 1.75 x64 | graphs | O(N^2 W + Q W) | AC | 0.062 s | 8396 KB |
