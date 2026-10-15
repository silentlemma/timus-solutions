# 1693. El problema de Loyd

[Timus 1693](https://acm.timus.ru/problem.aspx?space=1&num=1693) · dificultad 10340 · constructive

Problema original de Sam Loyd e Igor Chevdar, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cortar un tablero de ajedrez de n × n por las líneas de la cuadrícula
en tantas piezas conexas como sea posible de modo que no haya dos
iguales. Las piezas que solo difieren en un giro son iguales, pero los
colores de las casillas cuentan: una casilla negra y una blanca son dos
piezas distintas.

## Entrada

n (1 ≤ n ≤ 30).

## Salida

El número de piezas y luego n filas de n letras minúsculas. Cada pieza
se escribe con una letra, y las piezas que se tocan usan letras
distintas. Se acepta cualquier corte óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
18
aaaacaaa
bbbcccba
baddabbb
aacdacba
accdacaa
babdccbb
baaadbba
babbaaaa
```

## Solución

**La cota.** Se cuentan las piezas coloreadas de cada área salvo giro:
2 de área 1, 1 de área 2, 4 de área 3, 10 de área 4, 36 de área 5, 110
de área 6 y 392 de área 7. Piezas distintas suman al menos la suma de
las k áreas más pequeñas, así que k no supera el mayor número cuya suma
de áreas mínimas cabe en n². Para n = 8 son 2 + 1 + 4 + 10 = 17 piezas
de área hasta 4, 56 casillas en total, y una pieza más con las 8
casillas restantes: 18.

**La construcción.** La cota siempre se alcanza: cada pieza de las
áreas más pequeñas se usa una vez, y el área sobrante se une en una
pieza mayor, única porque es la única de ese tamaño. Pero empaquetar
exactamente hasta 162 piezas en el cuadrado es una búsqueda difícil.
Por eso los cortes de los 30 tamaños se encontraron una vez, de
antemano, con una búsqueda en profundidad aleatoria con reinicios, y el
programa imprime el tablero guardado para el n dado. `O(n²)`.

Cada tablero guardado se comprobó de forma independiente: sus regiones
de una letra son piezas conexas, todas distintas salvo giro con los
colores incluidos, y su número es igual a la cota anterior. Las
cantidades de piezas por área se recalcularon enumerando poliominós.

Trampas:

- los colores cuentan, así que hay dos casillas sueltas, no una;
- solo los giros identifican piezas, las reflexiones no;
- una letra puede repetirse en piezas que no se tocan.

El verificador reconstruye las piezas a partir de las letras y
comprueba su número y que sean distintas dos a dos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1693_constructive.cpp](1693_constructive.cpp) | G++ 13.2 x64 | constructive | O(n²) | AC | 0.015 s | 140 KB |
| [1693_constructive.go](1693_constructive.go) | Go 1.14 x64 | constructive | O(n²) | AC | 0.031 s | 1084 KB |
| [1693_constructive.java](1693_constructive.java) | Java 1.8 | constructive | O(n²) | AC | 0.156 s | 1784 KB |
| [1693_constructive.py](1693_constructive.py) | Python 3.12 x64 | constructive | O(n²) | AC | 0.078 s | 1100 KB |
| [1693_constructive.rs](1693_constructive.rs) | Rust 1.75 x64 | constructive | O(n²) | AC | 0.015 s | 220 KB |
